#!/usr/bin/env python3
import glob
import time
import os
import sys
import tty
import termios
import select

# Locate fan input files
fan1_files = glob.glob('/sys/devices/platform/hp-wmi/hwmon/hwmon*/fan1_input')
fan2_files = glob.glob('/sys/devices/platform/hp-wmi/hwmon/hwmon*/fan2_input')
pwm_enable_files = glob.glob('/sys/devices/platform/hp-wmi/hwmon/hwmon*/pwm1_enable')

if not fan1_files or not fan2_files or not pwm_enable_files:
    print("Error: Required fan or PWM files not found. Ensure your system has these files and you have permissions (run with sudo).")
    exit(1)

def read_fan_speed(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read().strip()
    except PermissionError:
        return "Permission denied"

def set_fan_state(state):
    for pwm_file in pwm_enable_files:
        try:
            with open(pwm_file, 'w') as f:
                f.write(str(state))
        except PermissionError:
            print(f"Permission denied writing {pwm_file}. Run with sudo.")

def key_pressed():
    """Check if a key was pressed (non-blocking)."""
    dr, dw, de = select.select([sys.stdin], [], [], 0)
    if dr:
        return sys.stdin.read(1)
    return None

# Save terminal settings and set raw mode
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setcbreak(fd)

try:
    while True:
        os.system('clear')  # clear the screen

        # Display fan speeds
        for f1 in fan1_files:
            print(f"FAN 1: {read_fan_speed(f1)} RPM")
        for f2 in fan2_files:
            print(f"FAN 2: {read_fan_speed(f2)} RPM")

        print("\nPress '0' to disable fans, '1' to enable fans, Ctrl+C to exit.")

        # Non-blocking key check
        key = key_pressed()
        if key:
            if key == '0':
                set_fan_state(2)  # disable fans
            elif key == '1':
                set_fan_state(0)  # enable fans

        time.sleep(0.5)  # adjust refresh rate here

except KeyboardInterrupt:
    print("\nExiting fan monitor.")

finally:
    # Restore terminal settings
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
