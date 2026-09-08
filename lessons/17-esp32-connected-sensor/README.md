# Lesson 17: ESP32 Connected Sensor

## What you are building

An ESP32 sensor node that samples locally and publishes a small status page or serial report over Wi-Fi.

## What you will learn

Network configuration, retries, timeouts, separation of application and transport code, and why connected devices need failure paths.

## Prerequisites

[UART and I2C Device](../14-uart-i2c-device/README.md).

## Components, tools, and software

- Arduino Nano ESP32 or another documented ESP32 board
- I2C sensor, USB cable, breadboard, wires
- Arduino ESP32 core or ESP-IDF, serial monitor, local Wi-Fi network

## Build

Start with local sensor sampling. Add Wi-Fi connection with a timeout, then expose a small read-only status endpoint or periodic serial message. Never put network credentials in a committed source file.

## Test

Test no Wi-Fi, Wi-Fi loss, sensor disconnect, and repeated reconnects. Measure sample interval and response time. Confirm that the device continues local work when the network is unavailable.

## Resources

- [Arduino Nano ESP32 documentation](https://docs.arduino.cc/hardware/nano-esp32/)
- [Arduino ESP32 core documentation](https://docs.espressif.com/projects/arduino-esp32/en/latest/)

## What to build next

[Lesson 18: RTOS Sensor Logger](../18-rtos-sensor-logger/README.md).
