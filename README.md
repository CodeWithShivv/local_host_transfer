# File Transfer Software

## Overview

This project provides a simple file transfer solution using a graphical user interface (GUI) built with Tkinter. The software allows users to transfer files between macOS and Windows systems over the same network. It includes both client and server components, each bundled as standalone executables for ease of use.

## Components

- **File Transfer GUI**: A Tkinter-based application for selecting and sending files.
- **File Transfer Server**: A server application that listens for incoming file transfers and saves the received files.

## Features

- **Automatic Discovery**: The software automatically discovers available servers on the network.
- **Drag and Drop Support**: Users can drag and drop files to be transferred (in the case of the GUI).
- **Cross-Platform**: Supports both macOS and Windows.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- PyInstaller (for building executables)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
