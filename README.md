# LSB Image Steganography Tool

A command-line interface (CLI) tool written in Python that allows you to hide secret text messages inside images using **Least Significant Bit (LSB)** steganography, and extract them later. 

This project was built to demonstrate core cybersecurity and low-level data manipulation concepts, ensuring that the hidden message remains visually undetectable to the human eye.

---

## Features

* **Encode:** Hide text messages of any length (up to the image's pixel capacity) inside `.png` images.
* **Decode:** Extract hidden messages from modified images.
* **CLI Interface:** Easy-to-use terminal commands built with Python's native `argparse`.
* **Lossless:** Modifies only the last bit of the RGB channels, preserving the image's visual integrity.

---

## How It Works (The LSB Technique)

An image is composed of pixels, and each pixel contains 3 color channels: Red, Green, and Blue (RGB). Each channel is represented by an 8-bit binary number (0-255). 

This tool takes a text message, converts it into a binary string, and replaces the **Least Significant Bit (the last bit)** of each RGB value in the image with the bits of the secret message. Because only the last bit is altered, the color value changes by a maximum of 1, making the alteration invisible to the human eye.

---

## Prerequisites and Installation

To run this tool, you need **Python 3** installed on your machine and the `Pillow` library for image processing.

1. Clone this repository:
```bash
git clone https://github.com/marques-jpg/Stego
cd *your path to the repo*
```

2. Install the required dependencies:
```bash
pip install Pillow
```

---

## Usage Instructions

The script operates in two main modes: `encode` and `decode`.

### 1. Hiding a Message (Encode)
To hide a message, you need the original image, the secret message, and the desired name for the output image.
> **Important:** Always save your output image in `.png` format. Compressing algorithms like `.jpg` will destroy the hidden bits!

```bash
python stego.py encode -i original.png -m "My highly classified secret!" -o secret_image.png
```

### 2. Extracting a Message (Decode)
To extract a hidden message from an image, simply provide the path to the modified image.

```bash
python stego.py decode -i secret_image.png
```

**Output:**
```text
Message extracted: My highly classified secret!
```

---

## Disclaimer

This tool was developed for **educational and ethical purposes only** as part of a cybersecurity portfolio. Do not use this tool to hide malicious code or for any illegal activities. The author is not responsible for any misuse of this software.


## License

MIT License © 2026 Guilherme Marques.
