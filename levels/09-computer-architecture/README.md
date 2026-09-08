# Level 9: Computer Architecture

This level connects logic design to complete machines: datapaths, control, memory, and software-visible behaviour.

## Project sequence

1. **ALU and register file:** implement operations and verify flags with directed tests.
2. [RISC-V single-cycle datapath](../../lessons/26-riscv-single-cycle-datapath/README.md): implement a documented RV32I subset and trace register state.
3. [Memory-mapped GPIO peripheral](../../lessons/27-memory-mapped-gpio-peripheral/README.md): define a CSR interface and write RTL plus a bare-metal C driver.
4. [Zephyr native-sim peripheral](../../lessons/28-zephyr-native-sim-peripheral/README.md): test a driver and simulated hardware on the host.
5. **Memory and bus system:** add address decoding, RAM, and a memory-mapped peripheral.
6. **Pipeline experiment:** measure hazards and compare a simple pipeline with the single-cycle design.
7. **Cache or DMA project:** measure hit rate, bandwidth, and correctness under contention.

## Verify

Use instruction-level tests, waveform inspection, architectural reference models, and performance measurements.

**Next:** [Level 10: ASIC Design](../10-asic-design/README.md).
