# Level 4: Microcontrollers

A development board is a learning instrument: it gives you a known power circuit, USB programming, clocking, and protection so you can focus on firmware and interfaces. Move to a bare MCU only when you understand what the board is providing.

## Project sequence

1. [GPIO device](../../lessons/12-gpio-device/README.md): button input, LED output, pull-up selection, and a debounced event.
2. [Temperature logger](../../lessons/13-temperature-logger/README.md): sample a sensor with an ADC or I2C, timestamp readings, and stream the data.
3. [UART and I2C device](../../lessons/14-uart-i2c-device/README.md): build a command-line interface, read a register map, and handle a missing device.
4. [PWM motor controller](../../lessons/15-pwm-motor-controller/README.md): use a proper driver stage, a flyback path where needed, and a separate motor supply.

Good starting boards include Arduino Uno R4 WiFi, Arduino Nano ESP32, Raspberry Pi Pico W, and STM32 development boards. Compare their official pinout, voltage, SDK, debugging, and library documentation before choosing one.

**Next:** [Level 5: Embedded Systems](../05-embedded/README.md).
