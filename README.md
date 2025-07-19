# Technic Move Hub Python Library

A Python library for controlling the LEGO Technic Move Hub via Bluetooth Low Energy (BLE). This library aims to provide a simple, synchronous interface for controlling your LEGO Move Hub.

## Features

* Connect and disconnect from the LEGO Technic Move Hub.
* Set the LED color.
* Control motors (A, B, C) with speed and direction (forward/backward).
* Handles asynchronous BLE communication internally, providing a synchronous API for the user.
* Graceful program exit if the hub is not connected when a command is issued.

## Installation

You can install this library directly from PyPI using pip:

```bash
pip install technicmovehub