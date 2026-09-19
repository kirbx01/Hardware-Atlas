# Domain 05 -- Embedded Systems

Moving from working demos to dependable firmware. STM32 peripherals, ESP32 networking, RTOS task scheduling, and the debugging that catches problems before they become product failures.

## Prerequisites

[Domain 04](../04-microcontrollers/README.md) or comfortable hands with GPIO and serial on a microcontroller. The timers and interrupts you noted there are the ones this domain schedules. You do not need to finish every Domain 04 lesson first — start here if the demos already feel easy.

## Core concepts

- Vendor registers versus the HAL that hides them, and when to care
- Wi-Fi and MQTT, including the failure paths nobody puts on the slide
- RTOS primitives: tasks, queues, semaphores, and timing
- Fault recovery and the kind of logging that survives a crash

AICTE's *Embedded Systems* (EC20) frames the same material from the product side: embedded memories, analog-digital signal conditioning at the interface, user interfacing, and the design trade-offs a fixed process and a thermal budget force on you. MQTT and the failure-path work here are the applied half of the *Computer Networks* (EC22) application layer. Interrupt-driven scheduling is the thread that runs through all of it — a queue exists precisely because an ISR outlived its use of a shared buffer.

## Levels

| Level | Name | Lessons | What it covers | Status |
|---|---|---|---|---|
| 01 | [STM32 and ESP32](levels/01-stm32-and-esp32/README.md) | 16–17 | Registers, timers, ADC, networking, failure paths | ✅ |
| 02 | [RTOS](levels/02-rtos/README.md) | 18 | Tasks, queues, timing, recovery | ✅ |
| 03 | [Custom peripheral](levels/03-custom-peripheral/README.md) | -- | Register-based device over I2C/SPI/UART, both ends | 🚧 planned |
| 04 | [Bootloader](levels/04-bootloader/README.md) | -- | Image validation, versioning, recoverable update | 🚧 planned |
| 05 | [Zephyr](levels/05-zephyr/README.md) | 28 | Simulated peripheral and driver on a native host target | ✅ |

## From demos to dependable firmware

```mermaid
flowchart LR
    A[Domain 04 demos] --> B[STM32 registers and peripherals]
    A --> C[ESP32 networking]
    A --> D[RTOS tasks]
    B --> E[Dependable firmware]
    C --> E
    D --> E
```

## Common mistakes

- Blocking the network task forever and calling it a timeout
- Sharing a buffer between tasks with no queue, then chasing corruption
- Using the watchdog to hide a missing recovery path
- Copying a HAL init sequence without checking which register did what

## Resources

- [Components](../../resources/components.md) for STM32 and ESP32 board choices.
- [Help](../../resources/help.md) when a bug has you looking at real-time code at 2am.
- [Opportunities](../../opportunities/README.md) for embedded and IoT roles at this depth.
- [Zephyr's native_sim board](https://docs.zephyrproject.org/latest/boards/native/native_sim/doc/index.html) for running RTOS code on the host before hardware exists.

## Where to go from here

- [Domain 06](../06-pcb-design/README.md) to move dependable firmware onto a dependable board.
- [Domain 07](../07-hardware-interfaces/README.md) when "the protocol is fine" stops being a guess.
- Back to [Domain 04](../04-microcontrollers/README.md) to wire the interrupts this domain schedules.
- **Related in [Opportunities](../../opportunities/README.md):** MITRE eCTF and CSAW Embedded Security Challenge (ESC) put secure-embedded design and attack on a team; ISEA-ISAP CTF is the national Indian equivalent.