# KeyLogger Analyzer

A Python-based educational project demonstrating keyboard event logging and log reconstruction for cybersecurity, digital forensics, and input analysis.

## Overview

This repository contains two components:

- **Key Logger** – Records keyboard events and stores them in a structured log file.
- **Log Reader** – Parses the raw log data and reconstructs it into a human-readable format by interpreting special keys such as Backspace, Enter, Tab, Shift, and more.

The project was created to better understand keyboard event handling, log processing, and text reconstruction techniques.

> **Disclaimer**
> This project is intended solely for educational purposes, cybersecurity research, digital forensics, and authorized testing. Do not use this software on systems without the explicit permission of the owner.

## Features

- Records keyboard events
- Stores raw keystroke logs
- Reconstructs readable text from recorded logs
- Handles common special keys
- Simple and lightweight implementation
- Easy to extend with additional key mappings

## Project Structure

```
.
├── keylogger.py          # Records keyboard events
├── keylog_reader.py           # Converts raw logs into readable text
├── keylogs.txt
└── README.md
```

## Requirements

- Python 3.10+
- pynput (or the keyboard library, depending on your implementation)

Install dependencies:

```bash
pip install pynput
```

## Usage

### Start Logging

```bash
python keylogger.py
```

### Analyze the Log

```bash
python analyzer.py
```

The analyzer will generate a reconstructed version of the recorded input.

## How It Works

1. Keyboard events are captured.
2. Events are written to a raw log.
3. The analyzer reads the log sequentially.
4. Special keys are interpreted.
5. The final output resembles the original typed text.

## Learning Objectives

- Keyboard event handling
- File I/O
- Event parsing
- State management
- Text reconstruction
- Python scripting

## Disclaimer

This software is provided for educational and research purposes only.

The author is not responsible for any misuse or unauthorized deployment of this project. Always obtain proper authorization before monitoring or recording keyboard input.

## License

MIT License
