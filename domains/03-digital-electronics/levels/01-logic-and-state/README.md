# Digital Electronics Level 01 -- Logic and State

Defined logic levels, gates, flip-flops, and what a reset is for. This is everything that hides inside a microcontroller once you stop thinking about it, studied on a breadboard where it is visible.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 10 | [Logic gates](../../../../lessons/10-logic-gates/README.md) | 74HC logic, truth tables, pull resistors | ✅ |
| 11 | [Flip-flop and counter](../../../../lessons/11-flip-flop-counter/README.md) | State, clocks, reset, bounce | ✅ |

## Why it matters

A counter mis-counting because of switch bounce is the same failure a UART receiver fights later at a different bit rate. Floating inputs, missing resets, and ignored bounce are the three mistakes this level exists to retire.

## Where to go from here

- [Domain 04 -- Microcontrollers](../../../04-microcontrollers/README.md) applies the same ideas in firmware.
- [Domain 08 -- FPGA and RTL](../../../08-fpga-and-rtl/README.md) if you want to keep designing logic directly.
- Back to [Domain 03 overview](../../README.md).