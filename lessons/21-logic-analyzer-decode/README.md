# Lesson 21: Logic Analyzer Decode

## What you are building

A captured and decoded SPI or I2C transaction used to diagnose a timing or data-integrity problem.

## What you will learn

Sampling rate, bus timing, clock polarity and phase, I2C pull-ups, trigger setup, protocol decoding, and evidence-based debugging.

## Prerequisites

[UART and I2C Device](../14-uart-i2c-device/README.md) and [Two-Layer PCB Routing](../20-two-layer-pcb-routing/README.md).

## Tools and software

- Logic analyzer with suitable voltage limits
- Analyzer software such as PulseView or the vendor application
- Known-good peripheral and test firmware

## Build and test

Capture a known-good transfer first. Then introduce one timing or wiring fault, compare decoded bytes and waveforms, and identify the violated requirement from the device datasheet. Do not connect a analyzer input beyond its voltage rating.

## What to build next

[Lesson 22: CAN Bus Node](../22-can-bus-node/README.md).
