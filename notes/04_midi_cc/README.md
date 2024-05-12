<!-- SPDX-License-Identifier: CC-BY-SA-4.0 OR MIT -->
<!-- SPDX-FileCopyrightText: Copyright 2024 Sam Blenny -->
# 04 MIDI CC

Picking suitable MIDI Control Change (CC) control numbers requires some thought
about potential conflicts with other MIDI controllers. Some CC numbers are very
common, like CC 1 for mod wheels. Many other controls have assigned meanings.

MIDI CC messages have three bytes. The first byte indicates the message
type (CC) and channel (1-16). The second byte is the CC control number (0-127).
The third byte is the CC data value (0-127).

For Patch-thing, **CC control numbers 16 to 31** are probably a reasonable
choice for default CC output channels.


## Summary of CC control number assignments

Midi.org has a table of MIDI 1.0
[Control Change Messages](https://midi.org/midi-1-0-control-change-messages)
that lists standard meanings for different CC control numbers.

1. Controls 0-31 are MSB values (7-bits, range 0-127)

2. Controls 32-63 are LSB values corresponding to controls 0-31 (providing
   14-bit range, 0-16383, but often not implemented)

3. Many control numbers have standard assignments

4. Many control numbers are "Undefined" or "General Purpose", but these
   unassigned controls are scattered between assigned controls. The largest
   contiguous blocks of general purpose or undefined controls are 14-31 (MSB),
   46-63 (LSB), and 102-119.

   List of all Undefined and General Purpose Controller control numbers:

   | Control | Description                  |
   | ------- | ---------------------------- |
   |       9 | undefined                    |
   |   14-15 | undefined                    |
   |      16 | General Purpose Controller 1 |
   |      17 | General Purpose Controller 2 |
   |      18 | General Purpose Controller 3 |
   |      19 | General Purpose Controller 4 |
   |   20-31 | undefined                    |
   |   46-47 | LSB for CC 14-15 (undefined) |
   |   48-51 | LSB for CC 16-19 (G.P. 1-4)  |
   |   51-63 | LSB for CC 20-31 (undefined) |
   |      80 | General Purpose Controller 5 |
   |      81 | General Purpose Controller 6 |
   |      82 | General Purpose Controller 7 |
   |      83 | General Purpose Controller 8 |
   |   85-87 | undefined                    |
   |   89-90 | undefined                    |
   | 102-119 | undefined                    |
