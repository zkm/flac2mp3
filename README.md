## flac2mp3

[![CI](https://github.com/zkm/flac2mp3/actions/workflows/ci.yml/badge.svg)](https://github.com/zkm/flac2mp3/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

![Python 3.10–3.12](https://img.shields.io/badge/Python-3.10%E2%80%933.12-3776AB?logo=python&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?logo=ffmpeg&logoColor=white)
![Standard library only](https://img.shields.io/badge/dependencies-standard%20library%20only-brightgreen)

A simple Python script to recursively convert FLAC files to MP3 format while preserving the original folder structure.

### Features
- Recursively searches for FLAC files in the specified source directory.
- Converts FLAC files to MP3 using `ffmpeg` with high-quality settings.
- Preserves the original directory structure in the target directory.
- Skips files that have already been converted to avoid duplication.
- Uses the user's home directory dynamically for compatibility across different systems.

### Requirements
- Python 3.10 or later
- `ffmpeg` installed on your system

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/zkm/flac2mp3.git
   cd flac2mp3
   ```

2. Ensure `ffmpeg` is installed. You can install it on Arch Linux with:
   ```sh
   sudo pacman -S ffmpeg
   ```

### Usage
1. Edit the script if needed to customize the source and target directories.
2. Run the script:
   ```sh
   python flac2mp3.py
   ```

### Contributing
Feel free to open issues or submit pull requests to improve the script.

### License
This project is licensed under the [MIT LICENSE](LICENSE).
