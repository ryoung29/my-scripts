#!/bin/bash

brightness=$(xrandr --current --verbose | grep Brightness | awk '{printf "%f", $2}')

if [[ $brightness < 1.1 ]]
then
    brightness=$(echo "$brightness + 0.1" | bc)
    xrandr --output eDP1 --brightness $brightness
fi
