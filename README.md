# Hardware Atlas

Hardware Atlas is an ascending, project-first roadmap for learning hardware by building, measuring, and debugging real things. It is not a shopping list and it is not an undirected collection of links.

Start where you are. Pick a project, check its prerequisites, buy only what that project needs, measure the result, and follow its next step.

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
| 7 | Hardware Interfaces and Communication | [Reliable buses and links](levels/07-interfaces/README.md) |
| 8 | FPGA and RTL | [Synchronous logic and verification](levels/08-fpga-rtl/README.md) |
| 9 | Computer Architecture | [Datapaths, memory, and CPUs](levels/09-computer-architecture/README.md) |
| 10 | ASIC Design | [RTL to silicon flow](levels/10-asic-design/README.md) |
| 11 | Semiconductor Devices | [Device physics and models](levels/11-semiconductor-devices/README.md) |
| 12 | Semiconductor Fabrication | [Process flow and yield](levels/12-semiconductor-fabrication/README.md) |
| 13 | Advanced Hardware and Research | [Reproduction and open research](levels/13-advanced-research/README.md) |

## Complete lesson chain

### Levels 0 and 1: foundations

1. [LED circuit](lessons/01-led-circuit/README.md) - Ohm's law, polarity, and current limiting.
2. [Voltage divider](lessons/02-voltage-divider/README.md) - measured node voltage and loading.
3. [Button and LED](lessons/03-button-and-led/README.md) - switches and defined logic states.
4. [Transistor switch](lessons/04-transistor-switch/README.md) - low-side switching.
5. [RC circuit](lessons/05-rc-circuit/README.md) - charge, discharge, and time constants.

Begin with [Level 0](levels/00-getting-started/README.md) if breadboards or multimeters are new to you. Begin with [Level 1](levels/01-basic-circuits/README.md) if you already understand voltage, current, and resistance.

### Level 2: analog electronics

6. [Light sensor](lessons/06-light-sensor/README.md) - turn light into a measurable voltage.
7. [Transistor amplifier](lessons/07-transistor-amplifier/README.md) - bias, gain, and clipping.
8. [Op-amp signal conditioner](lessons/08-op-amp-conditioner/README.md) - feedback and supply limits.
9. [Active filter](lessons/09-active-filter/README.md) - cutoff frequency and measured response.

Open the [Level 2 guide](levels/02-analog/README.md) for the theory route and extension projects.

### Level 3: digital electronics

10. [Logic gates](lessons/10-logic-gates/README.md) - 74HC logic, truth tables, and pull resistors.
11. [Flip-flop and counter](lessons/11-flip-flop-counter/README.md) - state, clocks, reset, and bounce.

The next planned additions are a 555 oscillator and a small digital clock. Follow the [Level 3 guide](levels/03-digital/README.md) for that planned sequence.

### Level 4: microcontrollers

12. [GPIO device](lessons/12-gpio-device/README.md) - firmware inputs, outputs, and debouncing.
13. [Temperature logger](lessons/13-temperature-logger/README.md) - sampling and recorded measurements.
14. [UART and I2C device](lessons/14-uart-i2c-device/README.md) - serial protocols and error handling.
15. [PWM motor controller](lessons/15-pwm-motor-controller/README.md) - drivers, current, and motor noise.

The [Level 4 guide](levels/04-microcontrollers/README.md) explains how to choose between Arduino, ESP32, Pico, and STM32 boards.

### Level 5: embedded systems

16. [STM32 peripheral project](lessons/16-stm32-peripheral/README.md) - timers, ADC, UART, and debugging.
17. [ESP32 connected sensor](lessons/17-esp32-connected-sensor/README.md) - networking and failure paths.
18. [RTOS sensor logger](lessons/18-rtos-sensor-logger/README.md) - tasks, queues, timing, and recovery.

The [Level 5 guide](levels/05-embedded/README.md) describes the next planned projects: a custom peripheral and a bootloader exercise. The later levels each have their own page, starting with [Level 6: PCB Design](levels/06-pcb-design/README.md).

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

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding a project or resource. External links should be checked, and each project should explain what to build, what to learn, what to measure, and what comes next.
