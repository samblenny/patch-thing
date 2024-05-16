# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Copyright 2024 Sam Blenny
#
from board import D4, D5, D6, D9, D10, D11, TX, RX, MISO, MOSI
from digitalio import DigitalInOut, DriveMode, Pull
import gc, time, usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange


# === Config Section ===

INS = (D5, D6, D9, D10, D11)     # Feather "input jack" pins
OUTS = (D4, TX, RX, MISO, MOSI)  # Feather "output jack" pins
CC_LIST = (16, 17, 18, 19, 20)   # MIDI CC numbers for OUTS

MIDI_CH = 0         # MIDI channel: 0 is ch1, 15 is ch16
DEBUG = True        # enable for debug prints to console
DELAY_LOOP = 0.005  # delay (s) between scanning jacks
DELAY_MIDI = 0.002  # delay (s) between MIDI sends (avoid bursts)
SEND_ALL_T = 5.0    # interval (s) between automatic send-all
DELAY_RC = 0.002    # settle time (s) after changing pin drive

# ======================

# MIDI setup
m = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=MIDI_CH)
gc.collect()

# Input and Output pins: start with everything pulled low
in_pins  = [DigitalInOut(p) for p in INS]
out_pins = [DigitalInOut(p) for p in OUTS]
for p in in_pins:
  p.switch_to_input(pull=Pull.DOWN)
for p in out_pins:
  p.switch_to_output(value=False, drive_mode=DriveMode.OPEN_DRAIN)
gc.collect()

# Arrays to hold graph of output to input connections
graph   = [0] * len(out_pins)
changes = [0] * len(out_pins)
gc.collect()

def set_pins_low():
  """Pull all pins LOW to reduce leakage and drain stray charges."""
  for p in in_pins:
    p.pull = Pull.DOWN
  for p in out_pins:
    p.value = False

def set_pins_highz():
  """Set IO pins HIGH-Z to avoid creating weird resistor networks."""
  for p in in_pins:
    p.pull = None
  for p in out_pins:
    p.value = True

def map_graph():
  """Map the connection graph of output pins to input pins.

  With 10k resistors on all the IO pins, and driving HIGH levels only
  with internal pullups, this acts a little odd. I guess it's kind of
  an RC network? It seems marginally better behaved if I leave
  un-involved pins HIGH-Z during measurements and drain stray charge
  before and after.
  Pros: resistors are cheap protection from shorts and also provide
        some (very limited) ESD protection
  Cons: seems to need management of stray charge to get good inputs
  """
  for (i, op) in enumerate(out_pins):
    reg = 0
    # shift input connections into register
    for ip in in_pins:
      set_pins_highz()             # set everything HIGH-Z
      op.value = False             # drive only current output LOW
      ip.pull = Pull.UP            # pull only current input pin HIGH
      time.sleep(DELAY_RC)         # wait for voltage to settle
      reg <<= 1
      reg |= 0 if ip.value else 1  # read input
      set_pins_low()               # set pins LOW (drain stray charge)
      time.sleep(DELAY_RC)
    changes[i] = graph[i] ^ reg    # find changed edges with XOR
    graph[i] = reg                 # store current edges

# Reset: scan pins and prepare to send all CC values
map_graph()
send_all = True;
t_prev = time.monotonic()

# Main Loop: sleep, scan pins, send CC messages when needed
while True:
  gc.collect()
  time.sleep(DELAY_LOOP)
  map_graph()
  # Send all the CC values at regular intervals (but not too often)
  t = time.monotonic()
  if t - t_prev > SEND_ALL_T:
    t_prev = t
    send_all = True
    if DEBUG:
      print()
  # Also send CC values when the graph changes
  for (i, (diff, cc, val)) in enumerate(zip(changes, CC_LIST, graph)):
    if diff or send_all:
      m.send(ControlChange(cc, val))
      time.sleep(DELAY_MIDI)
      if DEBUG:
        print(f"{cc}: {val:05b}")
  send_all = False
