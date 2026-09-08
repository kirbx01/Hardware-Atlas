# Level 7: Hardware Interfaces

This level turns individual peripherals into systems that can exchange data reliably.

## Project sequence

1. **UART command device:** define framing, commands, timeouts, and error responses.
2. **I2C sensor network:** use multiple addresses, pull-ups, bus recovery, and a documented register map.
3. **SPI display or flash device:** measure clock polarity, phase, chip select timing, and throughput.
4. [Logic analyzer decode](../../lessons/21-logic-analyzer-decode/README.md): capture a noisy SPI or I2C bus and diagnose timing or packet errors.
5. [CAN bus node](../../lessons/22-can-bus-node/README.md): connect CAN controller and transceiver nodes, termination, arbitration, and error handling.
6. **USB or Ethernet endpoint:** move from local buses to enumerated or packet-based communication.

## Verify

Capture signals with a logic analyser, document the wire protocol, test unplugged devices, and measure latency and error recovery.

**Next:** [Level 8: FPGA and RTL](../08-fpga-rtl/README.md).
