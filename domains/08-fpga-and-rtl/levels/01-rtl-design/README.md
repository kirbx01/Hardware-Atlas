# FPGA and RTL Level 01 -- RTL Design

Synchronous RTL for a synthesizable ALU and a UART receiver state machine. Combinational versus sequential, FSMs including the states nobody planned, and the latches you did not ask for.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 23 | [Combinational arithmetic RTL](../../../../lessons/23-combinational-arithmetic-rtl/README.md) | Build and simulate a synthesizable ALU | ✅ |
| 24 | [UART RX FSM](../../../../lessons/24-uart-rx-fsm/README.md) | Synchronize and receive asynchronous serial data | ✅ |

## Why "it compiled" is not a checkpoint

Compiling means the syntax is fine. It says nothing about whether the design is right — that is what the simulation and the synthesis report are for.

## Where to go from here

- [FPGA and RTL Level 02 -- Verification](../02-verification/README.md) to make the checking automatic.
- Back to [Domain 08 overview](../../README.md).