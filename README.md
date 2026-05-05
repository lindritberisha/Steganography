# Image Steganography with Python

This project implements a simple image steganography system using the Least Significant Bit (LSB) technique.
A secret text message is hidden inside a BMP image and later extracted successfully.

---

##  Project Structure

```
image-steganography-project/
├── embed.py
├── extract.py
├── highlight.py
├── secret.txt
├── README.md
└── img/
    ├── dice.bmp
    ├── flowers.bmp
    └── tiger.bmp
```

---

##  Configuration

The same configuration must be used in all scripts:

```python
key = 2026
colourPlane = 1       # 0 = red, 1 = green, 2 = blue
significantBit = 7    # 7 = least significant bit (LSB)
```

---

##  How to Run

### 1. Embed the secret message

```bash
python embed.py
```

This will create:

```
stego-image.bmp
```

---

### 2. Extract the hidden message

```bash
python extract.py
```

The program will print the recovered secret message in the terminal.

---

### 3. Highlight modified pixels

```bash
python highlight.py
```

This will create:

```
highlighted-image.bmp
```

🔴 The red pixels show where the algorithm would embed the message bits.

---

##  How It Works

* The secret message is converted into **7-bit ASCII binary**
* A **14-bit header** stores the message length
* Each bit is embedded into a pixel using the **Least Significant Bit (LSB)**
* Pixels are selected in a **pseudo-random order** using a shared key

---

##  Key Concepts

* **LSB (Least Significant Bit)**
  Small changes that are visually hard to detect

* **Random pixel selection (key-based)**
  Adds security — extraction fails if the wrong key is used

* **Colour plane selection**
  Message can be stored in Red, Green, or Blue channel

---

##  Capacity

Capacity depends on the number of pixels:

```
pixels = width × height
capacity_bits = pixels
capacity_bytes = capacity_bits / 8
```

---

##  Experiments

* Tested with different colour planes (R, G, B)
* Tested different bit positions (7 → 0)
* Observed visual distortion at lower bit positions
* Verified extraction fails with wrong key

---

##  Notes

* Only **ASCII characters** are supported in this implementation
* BMP format is used because it is **uncompressed**
* Larger images provide higher capacity

---

##  Author

Student project for Data Security / Internet Security laboratory.

---
