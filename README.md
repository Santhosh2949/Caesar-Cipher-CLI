# Caesar Cipher CLI Tool

A lightweight command-line tool written in Python to encrypt and decrypt text using the Caesar cipher algorithm.

This project demonstrates building, packaging, and distributing a Python CLI tool using modern Python standards.

---

## Features

- Encrypt and decrypt text using the Caesar cipher technique
- Command-line interface with clear flags and help output
- Supports custom shift values
- Handles both encryption and decryption modes
- Packaged as a pip-installable CLI tool
- Clean project structure with proper metadata

---
## As a Library
```python
from caesar_cipher import caesar
print(caesar("hello", 3)) # Encryption...
print(caesar("khoor", 3,encrypt=False))  # Decryption...
```
## Installation

#For User to use in terminal
```bash
pip install caesar-cipher-cli
```
#For Developers to contribute 
```bash
git clone https://github.com/Santhosh2949/caesar-cipher-cli
cd caesar-cipher-cli
pip install .

Usage

After installation, use the caesar command directly from the terminal.

Encrypt text
caesar --text "hello" --shift 3


Output:

khoor

Decrypt text
caesar --text "khoor" --shift 3 --decrypt


Output:

hello
```

## Command Options
caesar --help


## Available options:

--text : Text to encrypt or decrypt

--shift : Shift value for the cipher

--decrypt : Enable decryption mode

## Project Structure
caesar-cipher-cli/
├── caesar_cipher/
│   ├── __init__.py
│   └── cli.py
├── pyproject.toml
├── README.md
└── LICENSE

## Technologies Used

Python 3

argparse (standard library)

Git & GitHub

Python packaging (pyproject.toml)