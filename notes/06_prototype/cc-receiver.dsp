// SPDX-License-Identifier: MIT
// SPDX-FileCopyrightText: Copyright 2024 Sam Blenny
//
// This is Faust DSP source code for use with https://faustide.grame.fr/
//
// This MIDI CC decoder listens to 5 MIDI CC controls, where the value of each
// control represents the graph edges from one "output jack" to each of 5
// possible "input jacks". For example, cc16 == 5 (0b00101) means output D4 is
// connected to inputs D11 (0b00001) and D9 (0b00100)

declare options "[midi:on]";
import("stdfaust.lib");
cc16 = nentry("16[midi:ctrl 16]",0,0,127,1);
cc17 = nentry("17[midi:ctrl 17]",0,0,127,1);
cc18 = nentry("18[midi:ctrl 18]",0,0,127,1);
cc19 = nentry("19[midi:ctrl 19]",0,0,127,1);
cc20 = nentry("20[midi:ctrl 20]",0,0,127,1);
graph = (cc16 | cc17 | cc18 | cc19 | cc20);
process = hgroup("cc", no.pink_noise/6*graph) <: _,_;
