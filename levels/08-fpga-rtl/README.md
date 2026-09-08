# Level 8: FPGA and RTL

Here hardware behaviour is described as synchronous logic and verified before it is placed on a device.

## Project sequence

1. **RTL counter and testbench:** write a clocked counter and prove reset and rollover behaviour.
2. **UART receiver:** sample a serial stream and test framing errors in simulation.
3. **Memory-mapped peripheral:** expose registers to a simple bus and connect it to a soft processor or host.
4. **FPGA data path:** stream samples through a filter or checksum block and measure timing.
5. **Small soft CPU extension:** add or modify one instruction or peripheral interface.

## Verify

Use simulation, assertions, synthesis reports, timing constraints, and on-board probes. Do not treat a successful synthesis as proof that the design works.

**Next:** [Level 9: Computer Architecture](../09-computer-architecture/README.md).
