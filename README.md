# FanControl

**FanControl** is a Linux utility for controlling system fans on **HP Omen** and **HP Victus** laptops.

It allows you to:

* Enable or disable fan boost modes
* Monitor fan RPMs (CLI version)
* Toggle fan behavior programmatically or via hardware buttons (headless version)

### Compatibility & Testing

This project has **only been tested on the HP Victus 15-fb3xxx series**.
While it *might* work on other HP Omen or Victus models, behavior can vary depending on firmware or embedded controller implementation

If you run this on unsupported models:

* Fan control may partially work or not work at all
* Incorrect EC behavior could cause instability
* Use at your own risk and test carefully

### Components

* **fanboost-cli.py**
  Command-line interface for:

  * Toggling fan boost
  * Viewing current fan RPMs

* **fanboost-headless.py**
  For:

  * Toggling fans using a physical button
  * Background or automated usage
