# Hardware Atlas
>A practical path from your first circuit to custom silicon.

Hardware Atlas is an ascending, project-first roadmap for learning hardware by building, measuring, and debugging real things. You can also find some sorta shopping links and other things relevant to your needs in [resources/india.md](https://github.com/kirbx01/Hardware-Atlas/blob/main/resources/india.md) (You can follow up india.yml after reading `india.md`)

There is a given roadmap for GATE 2027 PREPARATION in [resources/gate.md](https://github.com/kirbx01/Hardware-Atlas/blob/main/resources/gate.md). This has curated list of resources and links you'd need for gate prep.

Start where you are. Pick a project, check its prerequisites, buy only what that project needs, measure the result, and follow its next step.

## Level navigation

- [Level 0: Getting Started](levels/00-getting-started/README.md)
- [Level 1: Basic Circuits](levels/01-basic-circuits/README.md)
- [Level 2: Analog Electronics](levels/02-analog/README.md)
- [Level 3: Digital Electronics](levels/03-digital/README.md)
- [Level 4: Microcontrollers](levels/04-microcontrollers/README.md)
- [Level 5: Embedded Systems](levels/05-embedded/README.md)
- [Level 6: PCB Design](levels/06-pcb-design/README.md)
- [Level 7: Hardware Interfaces](levels/07-interfaces/README.md)
- [Level 8: FPGA and RTL](levels/08-fpga-rtl/README.md)
- [Level 9: Computer Architecture](levels/09-computer-architecture/README.md)
- [Level 10: ASIC Design](levels/10-asic-design/README.md)
- [Level 11: Semiconductor Devices](levels/11-semiconductor-devices/README.md)
- [Level 12: Semiconductor Fabrication](levels/12-semiconductor-fabrication/README.md)
- [Level 13: Advanced Hardware](levels/13-advanced-research/README.md)

## Repository navigation

- [Roadmap](#roadmap)
- [Complete project chain](#complete-project-chain-levels-0-to-5)
- [Practical guides](#practical-guides)
- [Find something quickly](#find-something-quickly)
- [Contributing](#contributing)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [License](LICENSE)

## How to use this repository

1. Find your current level in the roadmap below.
2. Open the level page and choose the first project whose prerequisites you can satisfy.
3. Read the project page before buying anything. It lists the parts, tools, software, tests, and likely mistakes.
4. Build the smallest version, measure it, and record what you observed.
5. Follow the project's **What to build next** link. Do not skip the measurement step just because the circuit appears to work.

The `lessons/` directory contains the detailed build pages. The `levels/` directory explains why those projects are ordered that way. The `resources/` directory covers sourcing, tools, safety, simulation, help, and GATE. The `projects/` directory documents the format for future standalone projects.

## Roadmap

| Level | Focus | Start here |
|---|---|---|
| 0 | Getting Started | [Breadboard, multimeter, and measurements](levels/00-getting-started/README.md) |
| 1 | Basic Circuits | [Resistors, switches, transistors, and RC circuits](levels/01-basic-circuits/README.md) |
| 2 | Analog Electronics | [Sensors, amplifiers, op amps, and filters](levels/02-analog/README.md) |
| 3 | Digital Electronics | [Logic, state, timers, and counters](levels/03-digital/README.md) |
| 4 | Microcontrollers | [GPIO, ADC, PWM, and serial devices](levels/04-microcontrollers/README.md) |
| 5 | Embedded Systems | [Sensors, protocols, RTOS, and custom peripherals](levels/05-embedded/README.md) |
| 6 | PCB Design | [Schematic to prototype](levels/06-pcb-design/README.md) |
| 7 | Hardware Interfaces | [Reliable buses and links](levels/07-interfaces/README.md) |
| 8 | FPGA and RTL | [Synchronous logic and verification](levels/08-fpga-rtl/README.md) |
| 9 | Computer Architecture | [Datapaths, memory, and CPUs](levels/09-computer-architecture/README.md) |
| 10 | ASIC Design | [RTL to silicon flow](levels/10-asic-design/README.md) |
| 11 | Semiconductor Devices | [Device physics and models](levels/11-semiconductor-devices/README.md) |
| 12 | Semiconductor Fabrication | [Process flow and yield](levels/12-semiconductor-fabrication/README.md) |
| 13 | Advanced Hardware | [Reproduction and open research](levels/13-advanced-research/README.md) |

## Complete project chain: Levels 0 to 5

This is the practical route through the currently active part of the roadmap. Items marked **lesson** have a detailed page. Items marked **planned** are the next projects to add, so the handoff is visible without pretending that an unwritten lesson already exists.

### Level 0: Getting Started

1. **Breadboard map** - identify connected rows, power rails, the centre gap, and broken power rails. **Lesson:** [Level 0 guide](levels/00-getting-started/README.md).
2. **Multimeter practice** - measure a battery, check continuity with power removed, measure resistance out of circuit, and measure voltage across a powered circuit. **Lesson:** [Level 0 guide](levels/00-getting-started/README.md).
3. **LED circuit** - build and measure the first safe circuit. Continue to [Lesson 1](lessons/01-led-circuit/README.md).
4. **Basic voltage and current measurements** - extend the LED circuit and voltage divider while learning correct meter placement. **Lesson:** [Level 0 guide](levels/00-getting-started/README.md).

**Next:** [Level 1: Basic Circuits](levels/01-basic-circuits/README.md)

### Level 1: Basic Circuits

5. [LED circuit](lessons/01-led-circuit/README.md) - Ohm's law, polarity, and current limiting.
6. [Voltage divider](lessons/02-voltage-divider/README.md) - measured node voltage and loading.
7. [Button and LED](lessons/03-button-and-led/README.md) - switches and defined logic states.
8. [Transistor switch](lessons/04-transistor-switch/README.md) - low-side switching.
9. [RC circuit](lessons/05-rc-circuit/README.md) - charge, discharge, and time constants.

**Next:** [Level 2: Analog Electronics](levels/02-analog/README.md)

### Level 2: Analog Electronics

10. [Light sensor](lessons/06-light-sensor/README.md) - turn light into a measurable voltage.
11. [Transistor amplifier](lessons/07-transistor-amplifier/README.md) - bias, gain, and clipping.
12. [Op-amp signal conditioner](lessons/08-op-amp-conditioner/README.md) - feedback and supply limits.
13. [Active filter](lessons/09-active-filter/README.md) - cutoff frequency and measured response.

**Next:** [Level 3: Digital Electronics](levels/03-digital/README.md)

### Level 3: Digital Electronics

14. [Logic gates](lessons/10-logic-gates/README.md) - 74HC logic, truth tables, and pull resistors.
15. [Flip-flop and counter](lessons/11-flip-flop-counter/README.md) - state, clocks, reset, and bounce.
16. **555 timer oscillator** - generate a clock, measure its frequency and duty cycle, and compare real values with the calculation. **Planned.**
17. **Simple digital clock** - combine a clock, counters, decoding, and a display without hiding the logic inside a microcontroller. **Planned.**

**Next:** [Level 4: Microcontrollers](levels/04-microcontrollers/README.md)

### Level 4: Microcontrollers

18. [GPIO device](lessons/12-gpio-device/README.md) - firmware inputs, outputs, and debouncing.
19. [Temperature logger](lessons/13-temperature-logger/README.md) - sampling and recorded measurements.
20. [UART and I2C device](lessons/14-uart-i2c-device/README.md) - serial protocols and error handling.
21. [PWM motor controller](lessons/15-pwm-motor-controller/README.md) - drivers, current, and motor noise.

**Next:** [Level 5: Embedded Systems](levels/05-embedded/README.md)

### Level 5: Embedded Systems

22. [STM32 peripheral project](lessons/16-stm32-peripheral/README.md) - timers, ADC, UART, and debugging.
23. [ESP32 connected sensor](lessons/17-esp32-connected-sensor/README.md) - networking and failure paths.
24. [RTOS sensor logger](lessons/18-rtos-sensor-logger/README.md) - tasks, queues, timing, and recovery.
25. **Custom peripheral** - design a small register-based device over I2C, SPI, or UART and write both ends of the protocol. **Planned.**
26. **Bootloader exercise** - validate an image, handle versions, and provide a recoverable update path on a board you can reflash. **Planned.**

**Next:** [Level 6: PCB Design](levels/06-pcb-design/README.md)

## All levels at a glance

Each level has its own page. Use the links below when you want the complete route rather than only the beginner lesson chain.

### Level 0: Getting Started

[Open the Level 0 guide](levels/00-getting-started/README.md)

Learn how breadboards are connected, use a multimeter safely, build the first LED circuit, and measure voltage and current. You are ready to continue when you can draw a simple circuit, identify its return path, and explain a measurement.

**Next:** [Level 1: Basic Circuits](levels/01-basic-circuits/README.md)

### Level 1: Basic Circuits

[Open the Level 1 guide](levels/01-basic-circuits/README.md)

Build the LED circuit, voltage divider, button input, transistor switch, and RC circuit. The focus is prediction and measurement: Ohm's law, polarity, switching, charge, discharge, and time constants.

**Next:** [Level 2: Analog Electronics](levels/02-analog/README.md)

### Level 2: Analog Electronics

[Open the Level 2 guide](levels/02-analog/README.md)

Build a light sensor, transistor amplifier, op-amp signal conditioner, and active filter. Learn bias, gain, loading, clipping, noise, bandwidth, and the limits of ideal models. Verify the work with measured voltages and frequency response.

**Next:** [Level 3: Digital Electronics](levels/03-digital/README.md)

### Level 3: Digital Electronics

[Open the Level 3 guide](levels/03-digital/README.md)

Build logic gates with 74HC ICs, then a flip-flop and counter. Planned extensions add a 555 oscillator and a small digital clock. Verify truth tables, reset behaviour, timing, defined logic levels, and switch bounce before moving to firmware.

**Next:** [Level 4: Microcontrollers](levels/04-microcontrollers/README.md)

### Level 4: Microcontrollers

[Open the Level 4 guide](levels/04-microcontrollers/README.md)

Use a development board for GPIO, temperature logging, UART, I2C, and PWM motor control. Arduino, ESP32, Pico, and STM32 boards are introduced as practical platforms before bare-MCU design. Verify firmware with serial logs, sensor comparisons, bus captures, and current measurements.

**Next:** [Level 5: Embedded Systems](levels/05-embedded/README.md)

### Level 5: Embedded Systems

[Open the Level 5 guide](levels/05-embedded/README.md)

Move from working demos to dependable firmware with STM32, ESP32, RTOS tasks, custom peripherals, and bootloader work. Measure timing, reset causes, resource use, communication failures, and recovery behaviour.

**Next:** [Level 6: PCB Design](levels/06-pcb-design/README.md)

### Level 6: PCB Design

[Open the Level 6 guide](levels/06-pcb-design/README.md)

Convert a tested breadboard circuit into a schematic and a small two-layer PCB. Learn footprints, design rules, decoupling, return paths, connectors, Gerbers, assembly notes, and revision control. Verify the manufactured board against the breadboard measurements.

**Next:** [Level 7: Hardware Interfaces](levels/07-interfaces/README.md)

### Level 7: Hardware Interfaces

[Open the Level 7 guide](levels/07-interfaces/README.md)

Build reliable UART, I2C, SPI, CAN, USB, and Ethernet projects. Focus on framing, addressing, timing, termination, pull-ups, error handling, and recovery. Verify with a logic analyser, protocol documentation, latency measurements, and unplugged-device tests.

**Next:** [Level 8: FPGA and RTL](levels/08-fpga-rtl/README.md)

### Level 8: FPGA and RTL

[Open the Level 8 guide](levels/08-fpga-rtl/README.md)

Write synchronous RTL for counters, UART receivers, memory-mapped peripherals, data paths, and small CPU extensions. Verify with simulation, assertions, synthesis reports, timing constraints, and on-board probes.

**Next:** [Level 9: Computer Architecture](levels/09-computer-architecture/README.md)

### Level 9: Computer Architecture

[Open the Level 9 guide](levels/09-computer-architecture/README.md)

Build from an ALU and register file toward a CPU, memory system, bus, pipeline, cache, or DMA experiment. Verify instruction behaviour with reference models, waveforms, directed tests, and performance measurements.

**Next:** [Level 10: ASIC Design](levels/10-asic-design/README.md)

### Level 10: ASIC Design

[Open the Level 10 guide](levels/10-asic-design/README.md)

Take synthesizable RTL through gates, standard-cell layout, verification, timing, area, power estimates, and an open shuttle design. Verification, design rules, and documented limitations come before fabrication.

**Next:** [Level 11: Semiconductor Devices](levels/11-semiconductor-devices/README.md)

### Level 11: Semiconductor Devices

[Open the Level 11 guide](levels/11-semiconductor-devices/README.md)

Study diode, BJT, and MOSFET behaviour through controlled measurements, small-signal models, SPICE, temperature variation, and process corners. Stay within device ratings and record uncertainty for every experiment.

**Next:** [Level 12: Semiconductor Fabrication](levels/12-semiconductor-fabrication/README.md)

### Level 12: Semiconductor Fabrication

[Open the Level 12 guide](levels/12-semiconductor-fabrication/README.md)

Study wafer preparation, oxidation, deposition, lithography, etch, implantation, metallisation, packaging, and yield through process models, simulations, and safe teaching facilities. This level is not a home chemistry project.

**Next:** [Level 13: Advanced Hardware](levels/13-advanced-research/README.md)

### Level 13: Advanced Hardware

[Open the Level 13 guide](levels/13-advanced-research/README.md)

Choose a research question, reproduce a paper result, investigate open hardware, build a prototype, quantify uncertainty, and publish enough source, data, limitations, and instructions for independent review.

**Next:** choose a deeper branch, revisit a failed project, or contribute a verified lesson to Hardware Atlas.

## Practical guides

- [Components](resources/components.md): buy parts as projects require them.
- [Tools](resources/tools.md): a deliberately ascending workbench.
- [Power and batteries](resources/power-and-batteries.md): wiring and cell safety before experimentation.
- [Simulation](resources/simulation.md): test a complicated idea before ordering hardware.
- [Getting hardware in India](resources/india.md): distributors, Delhi NCR sourcing, inspection, and returns.
- [Where to get help](resources/help.md): choose a community by problem type.
- [GATE alongside the roadmap](resources/gate.md): use exam study to strengthen project work without turning this repo into a coaching site.

## Find something quickly

| I want to... | Open |
|---|---|
| Start from zero | [Level 0](levels/00-getting-started/README.md) |
| Learn basic circuits | [Level 1](levels/01-basic-circuits/README.md) |
| Learn analog electronics | [Level 2](levels/02-analog/README.md) |
| Learn digital logic | [Level 3](levels/03-digital/README.md) |
| Choose a development board | [Components](resources/components.md) and [Level 4](levels/04-microcontrollers/README.md) |
| Buy parts in India | [Getting hardware in India](resources/india.md) |
| Choose tools | [Tools](resources/tools.md) |
| Check a circuit before building | [Simulation](resources/simulation.md) |
| Ask for help | [Where to get help](resources/help.md) |
| Study GATE alongside projects | [GATE guide](resources/gate.md) |
| Add a new project | [Projects](projects/README.md) and [Contributing](CONTRIBUTING.md) |

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding a project or resource. Please also follow the [Code of Conduct](CODE_OF_CONDUCT.md). Hardware Atlas is available under the [MIT License](LICENSE).
