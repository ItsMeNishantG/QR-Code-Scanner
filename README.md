# QR-Code-Scanner
Simple QR Code Scanner Using Python 

A lightweight, purely terminal-based Command Line Interface (CLI) Python utility to decode QR codes and barcodes directly from static image files. 

Unlike most Python QR scanners that require heavy computer vision dependencies, this project completely bypasses **OpenCV**. It relies instead on **Pillow** (Python Imaging Library) and **pyzbar**, ensuring low system resource consumption, absolute speed, and zero external window popups.

## Features

- **No OpenCV Dependency:** Completely lightweight and operates entirely within your terminal environment.
- **Robust Decoding Engine:** Powered by the industry-standard `zbar` library to parse skewed or compressed matrices accurately.
- **Smart Error Handling:** Safely detects missing files, invalid formats, or images that lack decodable matrices without crashing your command line.
- **Multi-Code Parsing:** Automatically loops through and prints all data if an image contains multiple codes simultaneously.

## Prerequisites

Before running the application, your machine needs to have Python installed along with the underlying system-level `zbar` DLL/binary configuration, which maps pixels to decoded strings.

### System Dependencies

#### macOS
Install via Homebrew:
```bash
brew install zbar
```

#### Linux (Debian/Ubuntu)
Install via APT:
```bash
sudo apt-get install libzbar0
```

#### Windows
Windows users typically do not require additional system binary steps, as `pyzbar` includes bundled DLL variants. However, if you run into initialization problems, make sure you have installed the [Visual C++ Redistributable Packages for Visual Studio](https://microsoft.com).

## Installation

1. Clone this repository locally to your machine:
   ```bash
   git clone https://github.com
   cd simple-qr-scanner
   ```

2. Install the necessary Python packages using pip:
   ```bash
   pip install pillow pyzbar
   ```

## Usage

1. Drop the image containing a target QR code (supported formats include `.png`, `.jpg`, `.jpeg`, and `.webp`) directly into the repository root directory.
2. Open `simple_scanner.py` in your code editor and change the `target_image` value at the bottom to match your file name:
   ```python
   if __name__ == "__main__":
       target_image = "your_actual_file.png" 
       scan_qr_file(target_image)
   ```
3. Run the script from your terminal:
   ```bash
   python simple_scanner.py
   ```

### Example Terminal Output

```text
🔍 Analyzing image: 'your_actual_file.png'...

🎉 Success! Found QR Data:
---------------------------------
• Data: https://github.com
• Type: QRCODE
---------------------------------
```

## How It Works

- **File Validation:** The script queries the host operating system using `os.path.exists` to check path definitions before initializing memory buffers.
- **Memory Streaming:** `Pillow` reads raw image data vectors without locking hardware structures or spawning background UI display processing cycles.
- **Byte Stream Decoding:** The `pyzbar.decode` routine processes high-density graphical pixel grids and outputs raw bytes (`b'...'`). The script then maps these bytes back into a human-readable format using universal UTF-8 standard definitions (`.decode('utf-8')`).

## License

This project is open-source and available for personal use 
