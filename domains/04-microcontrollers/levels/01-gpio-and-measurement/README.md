# Microcontrollers Level 01 -- GPIO and Measurement

First firmware on real boards: driving pins on purpose and turning a sensor reading into a recorded measurement. GPIO is where the pull-up lesson from Domain 01 becomes a firmware problem instead of a wiring one.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 12 | [GPIO device](../../../../lessons/12-gpio-device/README.md) | Firmware inputs, outputs, debouncing | ✅ |
| 13 | [Temperature logger](../../../../lessons/13-temperature-logger/README.md) | Sampling and recorded measurements | ✅ |

## Why these two first

Inputs, outputs, and debounce first; sampling and logging second. Everything after this level — serial, PWM, RTOS — assumes you can trust a pin and keep a number.

## Where to go from here

- [Microcontrollers Level 02 -- Serial and Motor Control](../02-serial-and-motor-control/README.md) for protocols and drivers.
- Back to [Domain 04 overview](../../README.md).