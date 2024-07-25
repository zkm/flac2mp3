#!/usr/bin/env python3
import os
import subprocess
import logging
import re
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to sanitize filenames
def sanitize_filename(filename):
    # Replace unsafe characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# Function to check if the FLAC file is corrupt
def is_flac_file_valid(file_path):
    try:
        result = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(file_path), '-f', 'null', '-'], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"File is corrupt: {file_path}")
            return False
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking file {file_path}: {e}")
        return False

# Function to convert FLAC to MP3
def convert_flac_to_mp3(input_file, output_file):
    try:
        # Create directory structure if not already exists
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Convert FLAC to MP3 using ffmpeg
        subprocess.run(['ffmpeg', '-y', '-i', str(input_file), '-c:a', 'libmp3lame', '-q:a', '2', str(output_file)], check=True)
        logging.info(f"Converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error converting {input_file} to MP3: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

# Directory paths
input_directory = Path.home() / "Music"
output_directory = Path.home() / "mp3_collection"

# Iterate over FLAC files and convert them
for root, _, files in os.walk(input_directory):
    for file in files:
        if file.endswith(".flac"):
            input_file = Path(root) / file
            if not is_flac_file_valid(input_file):
                continue

            sanitized_filename = sanitize_filename(file)
            relative_path = input_file.relative_to(input_directory)
            sanitized_relative_path = relative_path.with_name(sanitized_filename)
            output_file = output_directory / sanitized_relative_path.with_suffix(".mp3")

            input_mtime = input_file.stat().st_mtime
            if output_file.exists():
                output_mtime = output_file.stat().st_mtime
                if input_mtime > output_mtime:
                    convert_flac_to_mp3(input_file, output_file)
                else:
                    logging.info(f"Skipping {input_file}, already up to date.")
            else:
                convert_flac_to_mp3(input_file, output_file)
