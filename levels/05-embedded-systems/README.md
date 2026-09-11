# Level 05 -- Embedded Systems

Moving from working demos to dependable firmware. STM32 peripherals, ESP32 networking, RTOS task scheduling, and the debugging that catches problems before they become product failures.

> [!NOTE]
> You do not need to finish Level 04 first. If you already handle GPIO and serial comfortably on a microcontroller, start here.

## What this level covers

- Vendor registers versus the HAL that hides them, and when to care
- Wi-Fi and MQTT, including the failure paths nobody puts on the slide
- RTOS primitives: tasks, queues, semaphores, and timing
- Fault recovery and the kind of logging that survives a crash

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 16 | [STM32 peripheral project](../../lessons/16-stm32-peripheral/README.md) | Timers, ADC, UART, debugging | ✅ |
| 17 | [ESP32 connected sensor](../../lessons/17-esp32-connected-sensor/README.md) | Networking and failure paths | ✅ |
| 18 | [RTOS sensor logger](../../lessons/18-rtos-sensor-logger/README.md) | Tasks, queues, timing, recovery | ✅ |
| -- | Custom peripheral | Register-based device over I2C/SPI/UART, both ends | 🚧 planned |
| -- | Bootloader exercise | Image validation, versioning, recoverable update | 🚧 planned |

## From demos to dependable firmware

```mermaid
flowchart LR
    A[Level 04 demos] --> B[STM32 registers and peripherals]
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

## Where to go from here

- [Level 06](../06-pcb-design/README.md) to move dependable firmware onto a dependable board.
- [Level 07](../07-hardware-interfaces/README.md) when "the protocol is fine" stops being a guess.

## Resources

- [Components](../../resources/components.md) for STM32 and ESP32 board choices.
- [Help](../../resources/help.md) when a bug has you looking at real-time code at 2am.