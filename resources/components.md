# Components

Do not buy a warehouse. Start with a development board and buy parts as a project calls for them. A small labelled assortment is useful only after you know which values you actually use.

## A practical progression

- **First circuits:** resistors, LEDs, pushbuttons, potentiometers, ceramic and electrolytic capacitors, diodes, and a few NPN BJTs such as BC547.
- **Switching and signal work:** N-channel MOSFETs selected for the gate voltage, comparators, timers and oscillators, and a few logic ICs from the 74HC family.
- **Interfaces:** logic-level shifters, shift registers, ADCs and DACs, EEPROM, OLED displays, USB-UART bridges, and CAN transceivers.
- **Power:** LDOs, buck converters, and boost converters. Read input range, output current, thermal limits, inductor requirements, and layout guidance before connecting a load.
- **Sensors:** an IMU, temperature sensor, light sensor, and one digital sensor with a documented protocol are enough for early projects.

MCP2515 plus a CAN transceiver module and TJA1050 are examples of CAN hardware, not mandatory beginner purchases. Check the voltage domains and the exact transceiver part number.

## Development boards

- [Arduino Uno R4 WiFi](https://docs.arduino.cc/hardware/uno-r4-wifi/): a familiar entry point with official documentation and a convenient ecosystem.
- [Arduino Nano ESP32](https://docs.arduino.cc/hardware/nano-esp32/): a compact ESP32-S3 board with Wi-Fi, Bluetooth, USB-C, Arduino support, and MicroPython documentation.
- [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html): inexpensive, well-documented, and useful for C/C++, MicroPython, GPIO, ADC, PWM, and wireless work.
- **STM32 development boards:** useful when you are ready for vendor reference manuals, timers, DMA, ADCs, interrupts, and hardware debugging. Start with an official or well-documented evaluation board before designing a bare STM32 board.

A board removes reset circuitry, programming connectors, clock choices, and power mistakes from the first experiment. That is a feature, not a shortcut.
