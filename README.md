# FanControl

**FanControl** is a Linux utility for controlling system fans on **HP Omen** and **HP Victus** laptops.

It allows you to:

* Enable or disable fan boost modes
* Monitor fan RPMs (CLI version)
* Toggle fan behavior programmatically or via hardware buttons (headless version)

### Components

* **fanboost-cli.py**
  Command-line interface for:

  * Toggling fan boost
  * Viewing current fan RPMs

* **fanboost-headless.py**
  For:

  * Toggling fans using a physical button
  * Background or automated usage
