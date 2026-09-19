# Domain 09 -- Computer Architecture

From an ALU and register file toward a CPU, a memory system, and a simulated peripheral. Verify with reference models and waveforms, not assumptions.

## Prerequisites

[Domain 08](../08-fpga-and-rtl/README.md) for the RTL habits, plus enough C to read and write a simple driver. The datapath you build here is a bigger version of the FSMs you already tested.

## Core concepts

- RISC-V RV32I in a single cycle: fetch, decode, execute, memory, writeback
- The register file, ALU, and the control path, one decision at a time
- Memory-mapped I/O and the line where the CPU ends and the peripheral begins
- A C driver talking to RTL registers
- Host-based simulation without target hardware (Ripes, Verilator, and friends)

AICTE's *Computer Architecture* (EC18) covers this domain's territory and then keeps going: instruction sets and formats, ALU design and IEEE 754 floating point, hardwired versus microprogrammed control, cache and virtual memory, DMA and interrupts, pipelining, and parallel processing. This roadmap stays deliberately single-cycle — pipelining, the memory hierarchy, and floating point are the natural extensions when you revisit the core in [Domain 13](../13-advanced-hardware/README.md). The C driver here is the same wear pattern you will put on real silicon in Domain 10.

## Levels

| Level | Name | Lessons | What it covers |
|---|---|---|---|
| 01 | [RISC-V core](levels/01-riscv-core/README.md) | 26–27 | RV32I datapath, memory-mapped GPIO and a C driver |

The [Zephyr level in Domain 05](../05-embedded-systems/levels/05-zephyr/README.md) is where the simulated-peripheral story continues on the software side: lesson 28 exercises the host-based simulation idea against a real embedded OS.

## One cycle, end to end

```mermaid
flowchart LR
    A[Fetch] --> B[Decode]
    B --> C[Execute]
    C --> D[Memory]
    D --> E[Writeback]
    E --> F[Update PC]
    F --> A
```

## Common mistakes

- Two units trying to write the register file in the same cycle
- Control signals that conflict because they were designed one instruction at a time
- Writing a driver against register offsets and skipping the hardware header
- Trusting a simulated peripheral to have the timing of the real silicon

## Resources

- [Nand2Tetris](https://www.nand2tetris.org/) and [MIT Computation Structures (6.004)](https://computationstructures.org) for the full systems view.
- [Opportunities](../../opportunities/README.md) for CPU, architecture, and systems roles.
- [Ripes](https://github.com/mortbopet/Ripes) to watch a RISC-V datapath, pipeline, and cache run visually.

## Where to go from here

- [Domain 10](../10-asic-design/README.md) synthesizes and lays out the same RTL.
- Back to [Domain 08](../08-fpga-and-rtl/README.md) for the module-level habits this core stacks on top of.
- **Related in [Opportunities](../../opportunities/README.md):** FOSSi Foundation (CVA6/Ariane, OpenPiton) and RISC-V International mentor the exact open cores this domain builds; the ACM SIGDA SRC at DAC/ICCAD takes architecture research posters.