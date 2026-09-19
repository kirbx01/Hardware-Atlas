# Embedded Level 05 -- Zephyr

A Zephyr RTOS application built and run entirely as a native host binary against a simulated GPIO peripheral. Peripherals are described in a devicetree, firmware talks to a driver API, and the whole system runs on your laptop before hardware is in the room.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 28 | [Zephyr native-sim peripheral](../../../../lessons/28-zephyr-native-sim-peripheral/README.md) | Test a simulated peripheral and driver on the host | ✅ |

## Why Zephyr gets its own level

Zephyr is a different way of structuring firmware: declarative hardware description instead of `#define`s, a driver API instead of raw registers. The hardware-side peripheral design from [Lesson 27](../../../../lessons/27-memory-mapped-gpio-peripheral/README.md) finally meets the software-side driver model a real embedded OS expects — and `native_sim` lets you develop and test all of it for hours before a physical board exists.

## Where to go from here

- [Domain 06 -- PCB Design](../../../06-pcb-design/README.md) to put this dependable firmware onto a dependable board.
- [Domain 07 -- Hardware Interfaces](../../../07-hardware-interfaces/README.md) when "the protocol is fine" stops being a guess.
- Back to [Domain 05 overview](../../README.md).