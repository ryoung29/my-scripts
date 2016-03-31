#!/bin/bash

# Gets data from speedtest.net and adds data to a csv file. Best used in a
# cron job so that you can continuously monitor connection speeds.
# Requires speedtest-cli

timestamp=$(date +%H:%M)
datestamp=$(date +%F)
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)

mkdir -p $HOME/Speedtest/$year/$month/
touch "$HOME/Speedtest/$year/$month/$datestamp.csv"

filesize=$(stat -c '%s' $HOME/Speedtest/$year/$month/$datestamp.csv)
if [ $filesize == "0" ] ; then echo "Time,Download,Upload,,Graphic" > /home/pi/Speedtest/$year/$month/$datestamp.csv ; fi
speed_test_output=$(/usr/bin/speedtest-cli --share --simple --server 948)
download=$(echo "$speed_test_output" | grep ^Download | awk '{print $2}')
upload=$(echo "$speed_test_output" | grep ^Upload | awk '{print $2}')
graphic=$(echo "$speed_test_output" | grep ^Share | awk '{print $3}')
if [ "$download" == "" ] ; then download="0" ; fi
if [ "$upload" == "" ] ; then upload="0" ; fi
echo "$timestamp,$download,$upload,,$graphic" >> "$HOME/Speedtest/$year/$month/$datestamp.csv"
