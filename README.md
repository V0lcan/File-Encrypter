# File Encrypter

A simple Python application for encrypting and decrypting files and folders, including images and text files.  
Supports both a modern PyQt5 GUI and a classic Tkinter interface.

---

## Features

- **Encrypt/Decrypt any file or folder**: Works with images, text, and most file types.
- **Easy-to-use GUI**: Choose between PyQt5 or Tkinter interfaces.
- **Secure encryption**: Uses [Fernet](https://cryptography.io/en/latest/fernet/) symmetric encryption from the `cryptography` library.
- **Key management**: Automatically generates and stores a key file for encryption/decryption.
- **Batch operations**: Encrypt or decrypt entire directories at once.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Install dependencies:
  ```sh
  pip install cryptography pyqt5 filetype tqdm
  ```