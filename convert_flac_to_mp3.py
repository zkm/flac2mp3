#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

# Function to convert FLAC to MP3
def convert_flac_to_mp3(input_file, output_file):
    # Create directory structure if not already exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Convert FLAC to MP3 using ffmpeg
    subprocess.run(['ffmpeg', '-y', '-i', input_file, '-c:a', 'libmp3lame', '-q:a', '2', output_file], check=True)
    print(f"Converted {input_file}")

# Directory paths
input_directory = os.path.expanduser("~/Music")
output_directory = os.path.join(os.path.expanduser("~"), "mp3_collection")

# Iterate over FLAC files and convert them
for root, _, files in os.walk(input_directory):
    for file in files:
        if file.endswith(".flac"):
            input_file = os.path.join(root, file)
            relative_path = os.path.relpath(input_file, input_directory)
            output_file = os.path.join(output_directory, os.path.splitext(relative_path)[0] + ".mp3")

            input_mtime = os.path.getmtime(input_file)
            if os.path.exists(output_file):
                output_mtime = os.path.getmtime(output_file)
                if input_mtime > output_mtime:
                    convert_flac_to_mp3(input_file, output_file)
                else:
                    print(f"Skipping {input_file}, already up to date.")
            else:
                convert_flac_to_mp3(input_file, output_file)
