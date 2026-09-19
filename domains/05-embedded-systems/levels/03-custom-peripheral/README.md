# Embedded Level 03 -- Custom Peripheral

Design and drive a register-based device over I2C, SPI, or UART — both ends. You have written firmware against vendor peripherals; this level flips the table and makes you the vendor.

> [!WARNING]
> Planned level. No lesson files exist yet; the project format below is the target to aim at.

## What it will build

- A device exposing a small register map (status, data, control) over a serial bus you already drove in [Domain 04](../../../04-microcontrollers/README.md)
- Firmware on the other end that talks to it, treating it like any vendor peripheral
- A combined test: both ends on the bench, argued about with a logic analyzer

## Why it belongs here

Every vendor peripheral you have used is exactly this: registers behind a bus, described in a datasheet. Becoming the datasheet author for a small device is the fastest route to reading a real one fluently.

## Where to go from here

- [Embedded Level 04 -- Bootloader](../04-bootloader/README.md) to make that device update itself safely.
- Back to [Domain 05 overview](../../README.md).