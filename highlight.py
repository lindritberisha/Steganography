from PIL import Image
import random

key = 2026
colourPlane = 1
significantBit = 7

coverImage = 'img/flowers.bmp'
secretFile = 'secret.txt'
outputImage = 'highlighted-image.bmp'


image = Image.open(coverImage).convert('RGB')
width, height = image.size
pixels = image.load()

with open(secretFile, 'r', encoding='utf-8') as file:
    secret = file.read()

messageBits = ''.join(format(ord(ch), '07b') for ch in secret)
lengthBits = format(len(secret), '014b')
bits = lengthBits + messageBits

capacity = width * height

if len(bits) > capacity:
    raise ValueError("Message is too large for this image.")

shuffledIndices = list(range(capacity))
random.seed(key)
random.shuffle(shuffledIndices)

for i in range(len(bits)):
    index = shuffledIndices[i]

    x = index % width
    y = index // width

    pixels[x, y] = (255, 0, 0)

image.save(outputImage)

print("Highlighted image created successfully.")
print("Output image:", outputImage)
print("Modified pixels:", len(bits))