# Lesson 15: PWM Motor Controller

## What you are building

A microcontroller-controlled small DC motor with adjustable PWM speed and a separate motor supply.

## What you will learn

PWM duty cycle, motor startup current, ground reference, flyback protection, driver selection, and electrical noise.

## Prerequisites

[Transistor Switch](../04-transistor-switch/README.md) and [GPIO Device](../12-gpio-device/README.md).

## Components and tools

- Development board
- Small motor and a suitable MOSFET or motor-driver IC
- Flyback diode if required by the driver topology
- Separate motor supply, common ground, wires, breadboard, multimeter

## Build

Use a driver stage rated for the motor's startup and stall current. Keep motor current out of the board's regulator. Add the required diode or integrated protection, and connect grounds deliberately.

## Test

Measure motor-supply voltage, board voltage, duty cycle, and current at startup and steady speed. Stop immediately if the driver or wiring heats unexpectedly. Test with the motor mechanically unloaded first.

## Resources

- [Raspberry Pi Pico PWM documentation](https://www.raspberrypi.com/documentation/pico-sdk/hardware.html#group_hardware_pwm)
- [Pololu motor driver application notes](https://www.pololu.com/category/115/motor-drivers)

## What to build next

[Lesson 16: STM32 Peripheral Project](../16-stm32-peripheral/README.md).
