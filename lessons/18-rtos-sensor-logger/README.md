# Lesson 18: RTOS Sensor Logger

## What you are building

A small firmware system with separate sampling, communication, and logging tasks.

## What you will learn

Task boundaries, queues, timing, stack sizing, priorities, shared data, and failure recovery.

## Prerequisites

[STM32 Peripheral Project](../16-stm32-peripheral/README.md) or [ESP32 Connected Sensor](../17-esp32-connected-sensor/README.md).

## Components, tools, and software

- ESP32 or STM32 board supported by the chosen RTOS
- A sensor, USB cable, and serial output
- ESP-IDF FreeRTOS, Zephyr, or another documented RTOS environment

## Build

Create one periodic sampling task, one queue, and one logging task. Add communication only after the local path is stable. Make queue-full and sensor-failure behaviour explicit.

## Test

Measure task period jitter, queue depth, stack high-water mark, and behaviour when the consumer is delayed. Force a sensor error and confirm the system recovers without resetting the whole application.

## Resources

- [FreeRTOS documentation](https://www.freertos.org/Documentation/00-Overview)
- [Zephyr documentation](https://docs.zephyrproject.org/latest/)

## What to build next

A custom register-based peripheral, followed by a recoverable bootloader exercise.
