# Lesson 12: GPIO Device

## What you are building

A development-board project where a button controls an LED with software debouncing and a visible event counter.

## What you will learn

GPIO direction, pull-ups, active-low inputs, debounce timing, serial logging, and the difference between polling and event-driven code.

## Prerequisites

[Flip-Flop and Counter](../11-flip-flop-counter/README.md) and basic programming.

## Components, tools, and software

- Arduino Nano ESP32, Arduino Uno R4 WiFi, Raspberry Pi Pico W, or similar board
- LED, 220-1k ohm resistor, pushbutton, 10k resistor, breadboard, wires
- USB cable, board IDE or SDK, serial monitor

## Build

Connect the LED through its resistor to a GPIO and connect the button between a GPIO and ground. Configure the input pull-up if your board supports it. Print one event per press, not one message per loop iteration.

## Test

Count ten presses and compare the software count with your physical count. Disconnect the button and check that the input remains at a defined level. Confirm the LED resistor and board I/O voltage are suitable.

## Resources

- [Arduino digital I/O reference](https://docs.arduino.cc/language-reference/en/functions/digital-io/)
- [Raspberry Pi Pico SDK GPIO](https://www.raspberrypi.com/documentation/pico-sdk/hardware.html#group_hardware_gpio)

## What to build next

[Lesson 13: Temperature Logger](../13-temperature-logger/README.md).
