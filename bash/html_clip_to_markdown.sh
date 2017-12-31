#!/bin/sh

# This is good for turning html to markdown from the clipboard.
# It's my replacement to getmd since the server is down. 
# getmd was my replacement to the markdown chrome extension since
# I changed to Firefox

xclip -o selection clipboard -t text/html | pandoc -r html --wrap=none -w markdown_github || echo "command failed."
