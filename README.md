<!-- SPDX-License-Identifier: CC-BY-SA-4.0 OR MIT -->
<!-- SPDX-FileCopyrightText: Copyright 2024 Sam Blenny -->
# patch-thing

A tactile patch-panel style MIDI controller project for software synths.

Patch-thing uses a matrix-scan algorithm to map cable connections. When you
patch cables or press the send-all button, Patch-thing's CircuitPython code
sends MIDI CC messages representing the current state of output jack to input
jack wiring.

This project is meant to be a relatively cheap and accessible way to add
colorful and tactile signal routing controls to a software synth.

*CAUTION: Plugging Patch-thing into EuroRack modules or other similar analog
synth gear is not recommended. Patch-thing uses 3.3V CMOS digital signals which
are not compatible with EuroRack CV/Gate signals.*


## Notes

- [03 Bill of Materials](notes/03_bom/README.md)

- [02 Diode Clamp Circuits](notes/02_diode_clamp_circuits/README.md)

- [01 Design Concept](notes/01_design_concept/README.md)


## Licenses

This repository is structured as a lab notebook. As such, there may be files of
different types, from different sources, potentially with different licenses.

For specifics, check my text files for SPDX license identifier comments at the
top. If I include third party code, it should generally be in a distinct
folder with LICENSE and/or README files explaining the origin and licensing.

For plain-text copies of the licenses used in this repo, refer to the
[LICENSES](LICENSES) folder.
