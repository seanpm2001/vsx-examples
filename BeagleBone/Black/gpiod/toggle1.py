#!/usr/bin/env python3
# //////////////////////////////////////
# 	toggle1.py
#  Toggles the P9_14 pin as fast as it can. P9_14 is line 18 on chip 1.
# 	Wiring:	Attach an oscilloscope to P9_14 to see the squarewave or 
#          uncomment the uleep and attach an LED.
# 	Setup:	sudo apt update; pip install gpiod
# 	See:	https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/tree/bindings/python/examples
# //////////////////////////////////////

import gpiod
import time

LED_CHIP = 'gpiochip1'
LED_LINE_OFFSET = [18]  # P9_14, run: gpioinfo | grep -i -e chip -e P9_14

chip = gpiod.Chip(LED_CHIP)

lines = chip.get_lines(LED_LINE_OFFSET)
lines.request(consumer='blink', type=gpiod.LINE_REQ_DIR_OUT)

while True:
    lines.set_values([0])
    time.sleep(0.1)
    lines.set_values([1])
    time.sleep(0.1)
    