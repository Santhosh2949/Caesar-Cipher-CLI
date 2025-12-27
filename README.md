<<<<<<< HEAD
# Caesar-Cipher-CLI
=======
# Caesar Cipher CLI Tool

    A simple command-line tool to encrypt and decrypt text using the **Caesar Cipher** algorithm.  
    Built with Python using clean argument parsing and case-preserving encryption.

---

## Features
    - Encrypt and decrypt text using a shift value
    - Preserves uppercase and lowercase letters
    - Supports spaces in text
    - Command-line interface using `argparse`
    - Handles invalid input gracefully

---

## Requirements
    - Python 3.7 or higher

---

## Usage
```bash
  Encrypt Text
    python caesar.py -t "Hello World" -s 3
  Output:
        Khoor Zruog
  Decrypt Text
    python caesar.py -t "Khoor Zruog" -s 3 -d
  Output:
        Hello World
```
## Command-Line Arguments
Argument	    Description
-t, --text	    Text to encrypt or decrypt (letters and spaces only)
-s, --shift	    Shift value (integer)
-d, --decrypt   Decrypt mode (optional flag)

## Input Rules

    Only alphabetic characters and spaces are allowed

    Numbers and special characters are rejected

    Shift values are automatically normalized (e.g., 29 → 3)

## How It Works

The Caesar Cipher shifts each letter by a fixed number of positions in the alphabet.

    Encryption shifts letters forward

    Decryption shifts letters backward

    Case is preserved

    Spaces remain unchanged

## Example

    Input:
        Attack At Dawn
    
    Shift:
        5
    
    Output:
        Fyyfhp Fy Ifbs

## Author

    Santhosh Kumar
>>>>>>> 705b500 (Caesar-Cipher-cli)
