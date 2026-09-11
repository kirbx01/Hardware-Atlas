# Level 08 -- FPGA and RTL

Synchronous RTL for counters, UART receivers, and memory-mapped peripherals. Verified with simulation, assertions, and synthesis reports, not just "it compiled."

> [!WARNING]
> "It compiled" means your syntax is fine. It says nothing about whether the design is right. The simulation and the synthesis report are where the design gets checked.

## What this level covers

- Combinational versus sequential RTL, and why the distinction shows up in silicon
- Finite state machines in Verilog, including the states nobody planned
- Clock crossing and synchronisation for asynchronous inputs
- Automated verification with cocotb testbenches
- Synthesis reports: the area and timing that the simulator never told you

## Lessons

| # | Lesson | What it builds |
|---|---|---|
| 23 | [Combinational arithmetic RTL](../../lessons/23-combinational-arithmetic-rtl/README.md) | Build and simulate a synthesizable ALU |
| 24 | [UART RX FSM](../../lessons/24-uart-rx-fsm/README.md) | Synchronize and receive asynchronous serial data |
| 25 | [cocotb Python testbench](../../lessons/25-cocotb-python-testbench/README.md) | Automate RTL verification |

## How the pieces connect

```mermaid
flowchart LR
    A[Combinational RTL] --> B[FSM design]
    B --> C[UART RX]
    A --> D[cocotb verification]
    C --> D
```

## Common mistakes

- Writing combinational logic inside a clocked block and getting latches you did not ask for
- No reset, then wondering why the board powers up in an unknown state
- Feeding an asynchronous input at a flip-flop without a synchroniser
- Running the testbench once, seeing green, and calling it verified

## Where to go from here

- [Level 09](../09-computer-architecture/README.md) builds a RISC-V datapath out of the same RTL habits.
- [Level 10](../10-asic-design/README.md) takes that RTL toward silicon.

## Resources

- [HDLBits](https://hdlbits.01xz.net/wiki/Main_Page) for interactive Verilog practice.
- [ChipVerify](https://www.chipverify.com/) for SystemVerilog and UVM reference.