#!/bin/bash

VAR        = "files.txt"
VIDEOCODEC = "XVID"
AUDIOCODEC = "AAC"

ls *.avi | sort > $VAR # Collect the files in the current directory

cat $VAR | while read line; do  # Loop read the filenames from the file
    INPUT   = $(echo ${line}) # Grab the nxt new filename
    OUTPUT  = ${INPUT%.*i} # Remove shortest match of characters between the '. ' and the '4' at end of string
    OUTPUT  += ".mp4" # Append new extension
    avidemux --video-codec $VIDEOCODEC --audio-codec $AUDIOCODEC --force-unpack --load "$INPUT" --output-format MP4 --audio-map --save "$OUTPUT" --quit 
done

rm $VAR # Remove the text file with the file names
