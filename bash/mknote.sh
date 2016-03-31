#!/bin/bash

filename=$(basename "$1")
filename=${filename/md/odt}
pandoc -f markdown "$1" --reference-odt="$HOME/Docs/OP-temp.odt" -V version=1.0 -o "$HOME/Docs/Done/$filename"
rm "$1"
