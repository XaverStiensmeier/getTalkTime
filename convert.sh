#!/bin/bash
for f in *.mp4; do ffmpeg -i "$f" -c:a libmp3lame "${f%.mp4}.mp3"; done