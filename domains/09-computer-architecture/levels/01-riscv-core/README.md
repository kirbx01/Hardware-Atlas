# Computer Architecture Level 01 -- RISC-V Core

A small single-cycle RV32I core: fetch, decode, execute, memory, writeback — and a memory-mapped GPIO peripheral connected to a real C driver. The bigger version of the FSMs you already tested in Domain 08.

## Lessons

| # | Lesson | What it builds | Status |
|---|---|---|---|
| 26 | [RISC-V single-cycle datapath](../../../../lessons/26-riscv-single-cycle-datapath/README.md) | Implement and trace a small RV32I core | ✅ |
| 27 | [Memory-mapped GPIO peripheral](../../../../lessons/27-memory-mapped-gpio-peripheral/README.md) | Connect RTL registers to a C driver | ✅ |

## Why a single cycle on purpose

Pipelining, caches, and memory hierarchy are the natural extensions of this core, not prerequisites for understanding it. The register-file and control-path discipline here is what synthesis in the ASIC domain will reward.

## Where to go from here

- The Zephyr side of the driver story continues at [Domain 05, Embedded Level 05](../../../05-embedded-systems/levels/05-zephyr/README.md).
- [Domain 10 -- ASIC Design](../../../10-asic-design/README.md) synthesizes and lays out the same RTL.
- Back to [Domain 09 overview](../../README.md).