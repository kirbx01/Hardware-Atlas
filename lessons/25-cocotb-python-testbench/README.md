# Lesson 25: cocotb Python Testbench

## What you are building

An automated Python verification environment for the UART receiver or ALU.

## What you will learn

Coroutine-based stimulus, assertions, randomized tests, coverage-minded scenarios, and simulator integration.

## Prerequisites

[UART RX FSM](../24-uart-rx-fsm/README.md).

## Tools and software

- Python
- cocotb
- Verilator or another supported simulator

## Build and test

Generate valid and invalid UART transactions, compare the design output with a Python reference model, and run the suite in automation. Keep failing seeds and waveform artifacts for debugging.

## What to build next

[Lesson 26: RISC-V Single-Cycle Datapath](../26-riscv-single-cycle-datapath/README.md).
