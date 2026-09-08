# Lesson 16: STM32 Peripheral Project

## What you are building

An STM32 board that samples an ADC input, toggles a timer-driven GPIO, and reports measurements over UART while you debug it with a probe.

## What you will learn

Reference manuals, clock trees, timers, ADC configuration, interrupts, UART, and source-level debugging.

## Prerequisites

Levels 1 to 4, C basics, and the ability to read a pinout and reference manual.

## Components, tools, and software

- STM32 development board with documented debug interface
- Potentiometer or sensor, LED and resistor, USB-UART if the board lacks one
- USB cable, STM32CubeIDE or another supported toolchain, ST-LINK or onboard debugger

## Build

First flash a known-good GPIO example. Add one peripheral at a time: timer, ADC, then UART. Keep application code separate from peripheral setup so each measurement has a clear owner.

## Test

Set breakpoints, inspect ADC samples, measure the timer period, and verify UART framing. Record clock configuration and the exact board revision. Confirm reset and error behaviour after unplugging the sensor.

## Resources

- [ST STM32 documentation](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html)
- [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html)

## What to build next

[Lesson 17: ESP32 Connected Sensor](../17-esp32-connected-sensor/README.md).
