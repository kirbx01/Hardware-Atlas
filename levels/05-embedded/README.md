# Level 5: Embedded Systems

This level is about dependable systems, not just a board that runs a demo once.

## Project sequence

1. [STM32 peripheral project](../../lessons/16-stm32-peripheral/README.md): configure GPIO, timer, ADC, and UART with a debugger and a clear hardware abstraction boundary.
2. [ESP32 connected sensor](../../lessons/17-esp32-connected-sensor/README.md): build a connected sensor node, separating application code from Wi-Fi and retry behaviour.
3. [RTOS sensor logger](../../lessons/18-rtos-sensor-logger/README.md): split sampling, communication, and logging into tasks; measure stack use and timing.
4. **Custom peripheral**: design a small register-based device over I2C, SPI, or UART and write both ends of the protocol.
5. **Bootloader exercise**: validate an image, handle a version, and provide a recovery path. Do this on a board you can reflash, not on safety-critical hardware.

Measure timing, reset causes, power rails, error paths, and behaviour after unplugging or reconnecting a peripheral. Read the MCU reference manual, not only a library example.

**Next:** [Level 6: PCB Design](../06-pcb-design/README.md) when that page is added.
