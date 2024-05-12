<!-- SPDX-License-Identifier: CC-BY-SA-4.0 OR MIT -->
<!-- SPDX-FileCopyrightText: Copyright 2024 Sam Blenny -->
# 02 Diode Clamp Circuits


Goals:

1. Avoid releasing the magic smoke (don't expose CircuitPython board IO pins to
   voltages outside of the MCU's absolute maximum ratings).

2. Avoid IO driver over-current damage due to shorting 3.5mm plug tip to sleeve

3. Avoid damage from electrostatic discharge (ESD) by touching 3.5mm plugs


Motivation:

1. EuroRack modules, semi-modular synths, and other audio synth gear use analog
   control signals in a variety of voltage ranges (-10V..10V, -5V..5V, 0V..5V,
   0V..12V, etc.). In a setup with a mix of synth gear, accidentally connecting
   analog CV signals directly to a CircuitPython IO pin could easily damage the
   board.

2. It's very easy to touch the signal pins when handling 3.5mm audio plugs, so
   ESD into the 3.5mm jack inputs will happen.


Plan:

1. For each 3.5mm jack, use a diode clamp circuit with current limiting
   resistors to protect the CircuitPython board's IO pins against brief
   accidental connection to analog modular gear and mild repeated ESD.


Cautions:

1. The limited ESD protection of this circuit (mostly just current limiting
   resistors in front of the CircuitPython board's built in ESD protection) is
   probably insufficient for dry climates. If you live in a place like Arizona,
   you probably need better ESD protection.


## Clamp Circuit Simulation

I made this schematic in KiCad and simulated it with ngspice to get a rough
idea of how a diode clamp circuit might perform with EuroRack-level input and
the output connected to a 3.3V CMOS GPIO pin. I used 1N5817 Schottky diodes,
1 kΩ current limiting resistors, and a 10 kΩ pull-down resistor.

I got the 1N5817 Spice model from the SMC Diodes website at
[Products &gt; Discrete &gt; Schottky-Rectifiers](https://www.smc-diodes.com/Products/Discrete/Schottky-Rectifiers).

The design goals here are:

1. Clamp the output voltage to levels that won't damage a 3.3V CMOS IO pin
   running in either input or output mode.

2. Limit clamping current to avoid overheating the diodes or subjecting
   connected equipment to a high current load (keeping in mind that 3.5mm jacks
   may short signals to ground, but we can't do anything about that).


### Schematic for diode clamp to protect one IO pin:

![Schematic of diode clamp circuit](dual-1K-schematic.png)


### Simulation screenshots for DC sweep -9V to +9V

According to this simulation, with a DC sweep of -9V to +9V on the input, the
diode clamp circuit should clamp the output voltage to stay within the range of
approximately -0.25V to +3.39V, with clamping currents of less than 9mA.

*CAUTION: This is an approximation. Don't put too much faith in these numbers.*

![Diode clamp DC sweep simulation with min VOUT cursor](dual-1K-min-VOUT.png)

![Diode clamp DC sweep simulation with max VOUT cursor](dual-1K-max-VOUT.png)


## Links:

These are some application notes that I found on designing diode clamp circuits:

- [Onsemi AND8231/D: Circuit Configuration Options for TVS Diodes](https://www.onsemi.com/pub/Collateral/AND8231-D.PDF)

- [TI SBAA227: System-Level Protection for High-Voltage Analog
Multiplexers](https://www.ti.com/lit/an/sbaa227/sbaa227.pdf)
