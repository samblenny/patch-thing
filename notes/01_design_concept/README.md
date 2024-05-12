<!-- SPDX-License-Identifier: CC-BY-SA-4.0 OR MIT -->
<!-- SPDX-FileCopyrightText: Copyright 2024 Sam Blenny -->
# 01 Design Concept

Patch-thing is a MIDI controller providing tactile signal routing control for
software synths using patch cables and a grid of 3.5mm jack patch points.

Changing the cable connections, or pressing the send-all button, sends USB MIDI
CC messages describing the current patch configuration.

How is this different from 3.5mm patch points as used in EuroRack modules or
semi-modular synths?

1. Although Patch-thing has the physical form of a patch point grid, it does
   not route analog signals. Rather, Patch-thing controls signal routing by
   sending MIDI CC messages to a software synth. The signal routing happens in
   software, so you don't need so much analog circuitry.

2. Patch-thing is not interoperable with 3.5mm analog CV/Gate signals. The
   signals between Patch-thing's 3.5mm jacks use digital 3.3V CMOS logic to
   scan in a way vaguely similar to mechanical keyboard keyscan matrix.

3. Patch-thing is meant to be easily customized. By editing its CircuitPython
   code, jacks can be configured as input or output, and you can adjust which
   CC values get sent. Also, the front panel has space for putting label tape
   next to each jack.


## Hardware

1. Enclosure: Steel box with hinged lid

2. Patch points: Grid of 3.5mm audio jacks

3. Patch cables: EuroRack "audio noodle" style 3.5mm cables

4. Send-All button: Button to trigger CC messages without changing the patch

5. USB-C jack: USB connection to host computer for USB MIDI and Mass Storage

6. Brain: CircuitPython board with enough GPIO pins for each 3.5mm jack

7. Protection Circuit: Diode clamps to protect GPIO from overvolt/undervolt


## Software

1. CircuitPython: loop to scan jacks and send MIDI CC messages

2. Synth: Demo synth using Pd, LMMS, Pygame, or something similar


## Usage

1. Connect Patch-thing to host computer with a USB-C cable.

2. (Optional) If you don't like the default assignments of input and output
   jacks, or the associated CC values, edit CircuitPython's code.py to taste.

3. Start software synth on host computer. This will probably need to involve a
   programmable synth patch using Pd, Max/MSP, SuperCollider, or some other
   similar system capable of implementing matrix-switch functionality that can
   be controlled by MIDI CC messages.

4. Use 3.5mm EuroRack-style patch cables to make connections between the patch
   point jacks. (Patch-thing will send MIDI CC messages as you do this)

5. If you need to re-start your synth, you can use Patch-thing's send-all
   button to re-transmit all the MIDI CC messages to define your entire patch.
