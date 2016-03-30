#!/bin/bash

VAR        = "files.txt"
VIDEOCODEC = "XVID"
AUDIOCODEC = "MP3"

ls *.mkv | sort > $VAR # Collect the files in the current directory

cat $VAR | while read line; do  # Loop read the filenames from the file
    INPUT   = $(echo ${line}) # Grab the nxt new filename
    OUTPUT  = ${INPUT%.*v} # Remove shortest match of characters between the '. ' and the '4' at end of string
    OUTPUT  += ".mp4" # Append new extension
    avidemux --video-codec $VIDEOCODEC --audio-codec $AUDIOCODEC --force-alt-h264 --load "$INPUT" --output-format MP4  --save "$OUTPUT" --quit 
done

rm $VAR # Remove the text file with the file names
