# Level 8: FPGA and RTL

Here hardware behaviour is described as synchronous logic and verified before it is placed on a device.

## Project sequence

1. [Combinational arithmetic RTL](../../lessons/23-combinational-arithmetic-rtl/README.md): write and simulate a synthesizable multi-bit ALU.
2. [UART RX FSM](../../lessons/24-uart-rx-fsm/README.md): synchronize an asynchronous input and handle serial reception errors.
3. [cocotb Python testbench](../../lessons/25-cocotb-python-testbench/README.md): automate RTL verification with Python and Verilator.
4. **RTL counter and testbench:** write a clocked counter and prove reset and rollover behaviour.
5. **Memory-mapped peripheral:** expose registers to a simple bus and connect it to a soft processor or host.
6. **FPGA data path:** stream samples through a filter or checksum block and measure timing.

## Verify

Use simulation, assertions, synthesis reports, timing constraints, and on-board probes. Do not treat a successful synthesis as proof that the design works.

**Next:** [Level 9: Computer Architecture](../09-computer-architecture/README.md).
