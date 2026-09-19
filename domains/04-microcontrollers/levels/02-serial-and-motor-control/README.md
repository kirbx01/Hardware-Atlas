# Microcontrollers Level 02 -- Serial and Motor Control

UART and I2C as things you can see on pins, and PWM driving a motor with the current and back-EMF that come with it. The peripherals that every connected product quietly depends on.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 14 | [UART and I2C device](../../../../lessons/14-uart-i2c-device/README.md) | Serial protocols and error handling | ✅ |
| 15 | [PWM motor controller](../../../../lessons/15-pwm-motor-controller/README.md) | Drivers, current, motor noise | ✅ |

## Why this is the last stop before embedded

Timers, interrupts, and serial here are the exact peripherals the Embedded Systems domain schedules. Interrupt-driven operation already exists in a library call; this level is where you see the pin it came from.

## Where to go from here

- [Domain 05 -- Embedded Systems](../../../05-embedded-systems/README.md) for firmware that has to keep working when things fail.
- Back to [Domain 04 overview](../../README.md).