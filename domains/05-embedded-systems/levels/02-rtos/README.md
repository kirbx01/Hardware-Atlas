# Embedded Level 02 -- RTOS

Tasks, queues, semaphores, timing, and crash-surviving logging, built with an RTOS sensor logger. A queue exists precisely because an ISR outlived its use of a shared buffer — this level is where scheduling stops being a footnote.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 18 | [RTOS sensor logger](../../../../lessons/18-rtos-sensor-logger/README.md) | Tasks, queues, timing, recovery | ✅ |

## Why an RTOS moves this far down the stack

Interrupts are cheap; shared state is expensive. The discipline of queueing instead of sharing a buffer is the same in FreeRTOS here and Zephyr at [Embedded Level 05](../05-zephyr/README.md) — a task is a thread with a priority, not magic.

## Where to go from here

- [Embedded Level 03 -- Custom Peripheral](../03-custom-peripheral/README.md) for a register-based device over I2C/SPI/UART.
- [Embedded Level 05 -- Zephyr](../05-zephyr/README.md) to run the same RTOS ideas on a simulated target.
- Back to [Domain 05 overview](../../README.md).