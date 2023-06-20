# getTalkTime
Python program to get non-silent time of an audio file.

## CLI
- "-f", "--files": Requests one or more filenames. Takes all audio files in current folder if none is given.
- "-t", "--threshold": default=-40. Silence threshold in decibels. Expects an integer.
- "o", "--output": File to write csv to. If none is given, no csv file will be written.

## About Thresholds
If you have too much background noise, I advise you to first use noise reduction (using Audacity or another program) and then come back. Altering the threshold should be the last resort. Of course, if your recording is very quiet, thresholding might be the right way to go.
