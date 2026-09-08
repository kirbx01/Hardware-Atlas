# Lesson 14: UART and I2C Device

## What you are building

A serial command device that reports an I2C sensor reading and accepts a UART command such as `read`.

## What you will learn

UART framing, I2C addressing, pull-up resistors, register maps, timeouts, and handling a missing or disconnected peripheral.

## Prerequisites

[Temperature Logger](../13-temperature-logger/README.md).

## Components, tools, and software

- Development board
- I2C sensor breakout, 4.7k pull-ups if the breakout lacks them, breadboard and wires
- USB cable, SDK or Arduino/MicroPython environment, serial terminal, optional logic analyser

## Build

Connect common ground, supply, SDA, and SCL. Scan for the device only as a diagnostic, then use the sensor datasheet's address and register sequence. Implement a UART command parser with a timeout and an error response.

## Test

Record the address, raw bytes, converted value, and bus speed. Unplug the sensor and confirm the firmware reports an error rather than hanging. Use a second device or logic analyser if the readings are implausible.

## Resources

- [I2C-bus specification](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)
- [Arduino Wire library](https://docs.arduino.cc/language-reference/en/functions/communication/wire/)

## What to build next

[Lesson 15: PWM Motor Controller](../15-pwm-motor-controller/README.md).
