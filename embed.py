from PIL import Image
import random

key = 2026
colourPlane = 1       # 0 = red, 1 = green, 2 = blue
significantBit = 7    # 7 = least significant bit

coverImage = 'img/flowers.bmp'
secretFile = 'secret.txt'
outputImage = 'stego-image.bmp'


def modify_pixel(pixel, plane, bit, modifier):
    change = modifier * (2 ** (7 - bit))

    r = pixel[0] + change if plane == 0 else pixel[0]
    g = pixel[1] + change if plane == 1 else pixel[1]
    b = pixel[2] + change if plane == 2 else pixel[2]

    return (r, g, b)


image = Image.open(coverImage).convert('RGB')
width, height = image.size
pixels = image.load()

with open(secretFile, 'r', encoding='utf-8') as file:
    secret = file.read()

if any(ord(ch) > 127 for ch in secret):
    raise ValueError("Secret message must contain only ASCII characters.")

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

    pixel = pixels[x, y]
    channelValue = pixel[colourPlane]
    binaryValue = format(channelValue, '08b')

    if binaryValue[significantBit] != bits[i]:
        if bits[i] == '1':
            pixels[x, y] = modify_pixel(pixel, colourPlane, significantBit, 1)
        else:
            pixels[x, y] = modify_pixel(pixel, colourPlane, significantBit, -1)

image.save(outputImage)

print("Stego image created successfully.")
print("Output image:", outputImage)
print("Capacity:", capacity, "bits")
print("Used:", len(bits), "bits")