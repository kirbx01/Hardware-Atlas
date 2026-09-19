# Hardware Interfaces Level 01 -- Bus-Level Debugging

SPI, I2C, and CAN at the electrical level: idle states, clocking, acknowledging, termination, and pull-ups. Verified with a logic analyzer, not vibes — what the library says should be on the wire versus what a probe actually sees.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 21 | [Logic analyzer decode](../../../../lessons/21-logic-analyzer-decode/README.md) | Debug SPI or I2C timing and data | ✅ |
| 22 | [CAN bus node](../../../../lessons/22-can-bus-node/README.md) | Terminated CAN link and error inspection | ✅ |

## Why the analyzer is the whole point

Decoding at a baud rate that is close but not the actual one, missing pull-ups, and calling reflections interference are all debugging stories that end the moment you look at the pins instead of the code.

## Where to go from here

- [Domain 08 -- FPGA and RTL](../../../08-fpga-and-rtl/README.md) to implement an interface as RTL instead of reading one.
- Back to [Domain 07 overview](../../README.md).