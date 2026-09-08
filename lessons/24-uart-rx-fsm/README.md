# Lesson 24: UART RX FSM

## What you are building

A clocked Verilog UART receiver with synchronization, sampling, framing checks, and an FSM.

## What you will learn

Clock-domain crossing, metastability risk, oversampling, state transitions, start-bit detection, and framing errors.

## Prerequisites

[Combinational Arithmetic RTL](../23-combinational-arithmetic-rtl/README.md).

## Tools and software

- Verilog simulator
- Icarus Verilog or Verilator
- GTKWave

## Build and test

Synchronize the asynchronous input before using it in the FSM. Simulate valid frames, baud mismatch, noise, false starts, and bad stop bits. Check that each byte is reported once and errors are visible.

## What to build next

[Lesson 25: cocotb Python Testbench](../25-cocotb-python-testbench/README.md).
