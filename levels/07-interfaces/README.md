# Level 7: Hardware Interfaces

This level turns individual peripherals into systems that can exchange data reliably.

## Project sequence

1. **UART command device:** define framing, commands, timeouts, and error responses.
2. **I2C sensor network:** use multiple addresses, pull-ups, bus recovery, and a documented register map.
3. **SPI display or flash device:** measure clock polarity, phase, chip select timing, and throughput.
4. **CAN node pair:** send frames between two nodes, add termination, and handle bus errors.
5. **USB or Ethernet endpoint:** move from local buses to enumerated or packet-based communication.

## Verify

Capture signals with a logic analyser, document the wire protocol, test unplugged devices, and measure latency and error recovery.

**Next:** [Level 8: FPGA and RTL](../08-fpga-rtl/README.md).
