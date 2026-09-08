# Lesson 22: CAN Bus Node

## What you are building

Two CAN nodes using a controller and transceiver, with termination and error handling.

## What you will learn

CAN frames, arbitration, bit timing, differential signalling, bus termination, error counters, and fault isolation.

## Prerequisites

[Logic Analyzer Decode](../21-logic-analyzer-decode/README.md) and Level 4 UART/I2C work.

## Components and tools

- Two CAN controller/transceiver nodes, such as MCP2515 with a suitable TJA1050-based transceiver module
- 120 ohm termination as required by the bus topology
- Development boards, twisted-pair wiring, multimeter, and logic analyzer

## Build and test

Configure both nodes for the same bit rate, connect a short terminated bus, exchange frames, and log acknowledgements and error states. Confirm that termination is present only at the physical bus ends and follow each component datasheet.

## What to build next

[Lesson 23: Combinational Arithmetic RTL](../23-combinational-arithmetic-rtl/README.md).
