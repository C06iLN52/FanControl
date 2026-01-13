#!/usr/bin/env python3
import glob
import sys

# Locate pwm1_enable files
pwm_enable_files = glob.glob('/sys/devices/platform/hp-wmi/hwmon/hwmon*/pwm1_enable')

if not pwm_enable_files:
    print("Error: pwm1_enable not found. Are you on an HP system? Run with sudo.")
    sys.exit(1)

for pwm_file in pwm_enable_files:
    try:
        # Read current value
        with open(pwm_file, 'r') as f:
            current = f.read().strip()

        if current == '2':
            new = '0'
        elif current == '0':
            new = '2'
        else:
            print(f"{pwm_file}: unexpected value '{current}', skipping")
            continue

        # Write new value
        with open(pwm_file, 'w') as f:
            f.write(new)

        print(f"{pwm_file}: {current} → {new}")

    except PermissionError:
        print(f"Permission denied: {pwm_file} (run with sudo)")
