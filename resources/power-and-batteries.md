# Power and Batteries

Keep early projects at extra-low voltage from a known USB supply, battery holder, or current-limited bench supply. Never use mains voltage on a breadboard.

- **Jumper wire:** flexible pre-cut wire for temporary board connections.
- **Solid-core wire:** stiff wire that fits breadboard contacts and is useful for short prototypes.
- **Hookup wire:** flexible insulated wire for soldered connections and harnesses.
- **CR2032:** a small primary coin cell for low-current loads. Do not recharge it or use it for motors.
- **18650 Li-ion and LiPo:** rechargeable cells with significant stored energy. They need a charger designed for the exact chemistry and cell arrangement, protection against overcharge, over-discharge, over-current, and short circuit, and a physically sound enclosure.
- **BMS:** a battery-management system can monitor and protect a pack, but it is not a substitute for the correct charger, cell matching, insulation, or a fuse.

Do not charge an unknown, swollen, punctured, hot, or damaged cell. Do not charge loose cells unattended or mix cells with different age, capacity, or state of charge. A LiPo pack needs a charger and balance/protection arrangement appropriate to its cell count. Read the cell and charger documentation first.

Check polarity, current limits, connector ratings, and the voltage at the load before power-up. Add a fuse when a battery can deliver more fault current than the wiring or circuit can safely tolerate.
