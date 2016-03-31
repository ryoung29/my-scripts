#!/bin/bash

filename=$(basename "$1")
filename=${filename/md/pdf}
pandoc -f markdown "$1" --template=$HOME/Docs/template-letter.tex \
    -V geometry:"left=1.20in, right=0.75in" \
    -V mainfont="Nimbus Sans" \
    -V monofont="Nimbus Mono" \
    -o "$HOME/Docs/Done/$filename" || echo "Failed"
rm "$1"
