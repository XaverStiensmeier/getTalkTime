# getTalkTime
Python program to get non-silent time of an audio file.

## CLI
- "-f", "--files": Requests one or more filenames. Takes all audio files in current folder if none is given.
- "-t", "--threshold": default=-40. Silence threshold in decibels. Expects an integer.
- "o", "--output": File to write csv to. If none is given, no csv file will be written.
