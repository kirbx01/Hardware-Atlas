# Embedded Level 01 -- STM32 and ESP32

Dependable firmware starts here: timers, ADC, and UART on a bare-metal STM32, then real networking with its failure paths on an ESP32. This is the move from demos to firmware that has to survive contact with the real world.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 16 | [STM32 peripheral project](../../../../lessons/16-stm32-peripheral/README.md) | Timers, ADC, UART, debugging | ✅ |
| 17 | [ESP32 connected sensor](../../../../lessons/17-esp32-connected-sensor/README.md) | Networking and failure paths | ✅ |

## Why registers before the HAL

A library init sequence is uncheckable until you know which register it set. Writing the register directly once makes every later HAL read a translation, not a leap of faith.

## Where to go from here

- [Embedded Level 02 -- RTOS](../02-rtos/README.md) to schedule the interrupts this level configured.
- Back to [Domain 05 overview](../../README.md).