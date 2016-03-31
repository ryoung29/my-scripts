#!/bin/bash

filename=$(basename "$1")
filename=${filename/md/pdf}
pandoc -f markdown "$1" --template=$HOME/Docs/mytemplate.tex \
    -V geometry:"left=0.75in, right=0.75in" \
    -V version=1.0 \
    -V mainfont="Nimbus Sans" \
    -V monofont="Nimbus Mono" \
    -o "$HOME/Docs/Done/$filename"
rm "$1"
