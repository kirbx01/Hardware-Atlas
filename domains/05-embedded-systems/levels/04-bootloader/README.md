# Embedded Level 04 -- Bootloader

Image validation, versioning, and a recoverable update path. A device that can only be flashed once at the factory is a demo; this level is what makes it shippable.

> [!WARNING]
> Planned level. No lesson files exist yet; the project format below is the target to aim at.

## What it will build

- A bootloader that checks an image signature or checksum before jumping to it
- Versioning that refuses to downgrade, and reports why
- A recovery path: a bad image boots the other way instead of bricking the device
- The same firmware updated over the same serial bus you drove for the custom peripheral

## Why it belongs here

Fault recovery is the whole point of the Embedded domain. A watchdog hides a missing recovery path; a bootloader is the recovery path made explicit.

## Where to go from here

- [Embedded Level 05 -- Zephyr](../05-zephyr/README.md) for the structured, driver-API way to build the same systems.
- Back to [Domain 05 overview](../../README.md).