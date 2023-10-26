#!/bin/bash

# export DISPLAY to connect to GUI
export DISPLAY=:0.0

# kill all instances of eog
pkill eog

# force display standby
xset dpms force standby
