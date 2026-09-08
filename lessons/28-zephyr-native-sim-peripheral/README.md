# Lesson 28: Zephyr Native Sim Peripheral

## What you are building

A Zephyr driver and simulated peripheral tested with `native_sim` on the host.

## What you will learn

Device-tree bindings, driver APIs, thread scheduling, hardware abstraction, host-based tests, and deterministic failure injection.

## Prerequisites

[Memory-Mapped GPIO Peripheral](../27-memory-mapped-gpio-peripheral/README.md).

## Tools and software

- Zephyr SDK and west
- `native_sim`
- C test application and device-tree overlay

## Build and test

Define the device-tree binding, implement the driver, and run it in native simulation. Test reads, writes, interrupts or simulated events, timeouts, and concurrent access without requiring hardware.

## What to build next

[Lesson 29: Yosys RTL Synthesis](../29-yosys-rtl-synthesis/README.md).
