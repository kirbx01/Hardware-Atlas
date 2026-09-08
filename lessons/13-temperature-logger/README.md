# Lesson 13: Temperature Logger

## What you are building

A board that samples a temperature sensor periodically and streams timestamped readings over USB serial.

## What you will learn

Sensor data sheets, ADC or I2C reads, sampling intervals, unit conversion, calibration, and recording data outside the firmware.

## Prerequisites

[GPIO Device](../12-gpio-device/README.md).

## Components, tools, and software

- Development board from Lesson 12
- TMP36 analog sensor or a documented I2C temperature sensor
- 100nF decoupling capacitor, breadboard, wires, USB cable
- Arduino IDE, MicroPython, or the board's official SDK; a serial terminal

## Build

Wire the sensor according to its datasheet. Sample once per second and print a line containing a timestamp, raw reading, converted temperature, and error status. Keep sensor power and ground short and clear.

## Test

Log for five minutes, touch the sensor briefly, and compare against a second thermometer. Record supply voltage and sensor part number. Do not claim accuracy better than the sensor and calibration support.

## Resources

- [Raspberry Pi Pico documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- [Arduino Nano ESP32 documentation](https://docs.arduino.cc/hardware/nano-esp32/)

## What to build next

[Lesson 14: UART and I2C Device](../14-uart-i2c-device/README.md).
