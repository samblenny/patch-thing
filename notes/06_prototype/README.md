<!-- SPDX-License-Identifier: CC-BY-SA-4.0 OR MIT -->
<!-- SPDX-FileCopyrightText: Copyright 2024 Sam Blenny -->
# 06 Prototype

Before I start soldering and drilling holes, I suppose it would be sensible to
write CircuitPython code for a breadboard and flying wire prototype that talks
MIDI CC to a software synth patch.

My goal is a MIDI control surface for tactile control of software synth signal
routing with similar aesthetics to analog modular synths, but at a much lower
cost. My working plan is to scan a grid of 3.5mm patch points, translate the
resulting graph of patch cable connections into MIDI CC messages, then write
synth patches that can use MIDI CC to do adaptive signal routing.

The main risk I see for this scheme is that making a software synth patch that
can adapt its signal routing in response to MIDI CC messages may be much harder
than I expect. I think it will be a bit of a challenge, but it might actually
turn out to be really hard.

If I can't effectively make use of MIDI CC messages in a software synth patch,
then maybe I should adjust my plan for the controller build to focus more on
switches and knobs.


## Breadboard Circuit

![Breadboard with Feather M4 Express, 10k resistors, and wires](breadboard-feather-M4-10k.jpeg)


## CircuitPython Code

**TODO**


## Software Synth Patch

**TODO**
