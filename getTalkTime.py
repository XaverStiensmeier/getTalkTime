#!/usr/bin/env python3
"""
Very simple program in order to get the non empty time from a .mp3 file.
Should support:
    WAV (.wav)
    MP3 (.mp3)
    OGG (.ogg)
    FLAC (.flac)
    AAC (.aac)
    M4A (.m4a)
    AIFF (.aiff)
    WMA (.wma)
"""
import argparse
import csv
import glob
from pydub import AudioSegment

FILE_ENDINGS = ('wav', 'mp3', 'ogg', 'flac', 'aac', 'm4a', 'aiff', 'wma')
PATTERN = '*.{' + ','.join(FILE_ENDINGS) + '}'

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Calculate the non-empty time of an MP3 file.")
parser.add_argument("-f", "--files", type=str, nargs="+", help="Path to the MP3 file")
parser.add_argument("-t", "--threshold", type=int, default=-40, help="Silence threshold in decibels")
parser.add_argument("-o", "--output", type=str, default=None, help="File to write to (csv)")
args = parser.parse_args()

results = {}
if not args.files:
    args.files = [file for file in glob.glob("*.*") if file.endswith(FILE_ENDINGS)]
    args.files.sort()
    print(args.files)

for file in args.files:
    # Load the MP3 file
    audio = AudioSegment.from_file(file)

    # Find the duration of the audio file
    duration = len(audio)

    # Calculate the non-empty time
    non_empty_time = 0

    for i in range(0, len(audio), 1000):  # Check every second
        segment = audio[i:i+1000]  # Split into 1-second segments (adjust as needed)
        if segment.dBFS > args.threshold:
            non_empty_time += len(segment)
        results[file] = {}
        results[file]["talk_time"] = int(non_empty_time / 1000)
        results[file]["all_time"] = int(len(audio) / 1000)
        results[file]["talk_percentage"] = round(non_empty_time / len(audio), 2)
    # Display the non-empty time
    print(f"{file}: {non_empty_time / 1000} seconds")
if args.output:
    with open(args.output, 'w') as csv_file:  
        writer = csv.writer(csv_file)
        writer.writerow(["name", "talk_time", "all_time", "talk_percentage"])
        for key, value in results.items():
            writer.writerow([key, int(value["talk_time"]), value["all_time"], value["talk_percentage"]])