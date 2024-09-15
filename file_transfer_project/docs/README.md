# File Transfer Project

## Overview

This project allows file transfer between macOS and Windows systems using a GUI application and a TCP-based file transfer protocol.

## Installation

1. **macOS:**
   - Build the macOS application using pyinstaller.
   - Run the application to select files and send them to a server.

2. **Windows:**
   - Build the Windows application using pyinstaller.
   - Run the application to select files and send them to a server.

## Running the Server

On Windows, run the server script to listen for incoming file transfers:

```
python src/server/server.py
```

## Usage

1. Start the server on Windows.
2. Run the file transfer application on macOS or Windows.
3. Enter the server IP address and select a file to send.

## License

This project is licensed under the MIT License.
