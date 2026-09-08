# Level 3: Digital Electronics

Build digital behaviour from logic ICs before hiding it inside firmware.

## Project sequence

1. [Logic gates](../../lessons/10-logic-gates/README.md): wire 74HC00, 74HC02, or 74HC08 gates with defined input states and decoupling capacitors.
2. [Flip-flop and counter](../../lessons/11-flip-flop-counter/README.md): make a clocked state element, observe switch bounce, and count in binary.
3. **Counter extension**: decode outputs to LEDs and compare the measured sequence with the truth table.
4. **555 timer**: make a clock, measure its frequency, and compare the calculated and measured duty cycle.
5. **Simple digital clock**: combine a stable clock, counters, and a display driver. Keep the first version modest.

Learn Boolean algebra, truth tables, propagation delay, fan-out, pull-ups, debouncing, and why unused CMOS inputs must not float.

**Next:** [Level 4: Microcontrollers](../04-microcontrollers/README.md).
