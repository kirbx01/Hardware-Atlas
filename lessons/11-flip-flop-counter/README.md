# Lesson 11: Flip-Flop and Counter

## What you are building

A clocked flip-flop followed by a binary counter, with the outputs shown on LEDs.

## What you will learn

State, edge-triggering, reset, switch bounce, binary counting, and the difference between combinational and sequential logic.

## Prerequisites

[Logic Gates](../10-logic-gates/README.md).

## Components and tools

- 74HC74 dual D flip-flop
- 74HC393 or similar binary counter
- 555 timer or a pushbutton clock
- LEDs, 1k ohm resistors, 10k pull resistors, 100nF capacitors
- Breadboard, wires, 5V supply, multimeter

## Build

Start with one flip-flop and a manual clock. Connect reset to a defined inactive level, then add the counter and LEDs. Add debouncing before using a pushbutton as a clock.

## Test

Check reset, then apply one clock edge at a time. Confirm the counter outputs follow 0000, 0001, 0010, and so on. Observe that a bouncing button can create several counts.

## Resources

- [Texas Instruments SN74HC74 datasheet](https://www.ti.com/lit/ds/symlink/sn74hc74.pdf)
- [Texas Instruments SN74HC393 datasheet](https://www.ti.com/lit/ds/symlink/sn74hc393.pdf)

## What to build next

[Lesson 12: GPIO Device](../12-gpio-device/README.md).
