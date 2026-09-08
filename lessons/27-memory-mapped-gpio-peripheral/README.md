# Lesson 27: Memory-Mapped GPIO Peripheral

## What you are building

An RTL GPIO peripheral with control and status registers and a bare-metal C driver.

## What you will learn

Address decoding, register semantics, bus handshakes, read/write side effects, firmware headers, and hardware-software contracts.

## Prerequisites

[RISC-V Single-Cycle Datapath](../26-riscv-single-cycle-datapath/README.md).

## Build and test

Define the register map before writing RTL. Implement reset values, reads, writes, and invalid addresses. Test the RTL with bus transactions, then compile a small C driver against the same register definitions.

## What to build next

[Lesson 28: Zephyr Native Sim Peripheral](../28-zephyr-native-sim-peripheral/README.md).
