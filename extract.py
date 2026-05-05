from PIL import Image
import random

key = 2026
colourPlane = 1
significantBit = 7

stegoImage = 'stego-image.bmp'

image = Image.open(stegoImage).convert('RGB')
width, height = image.size
pixels = image.load()

capacity = width * height

shuffledIndices = list(range(capacity))
random.seed(key)
random.shuffle(shuffledIndices)

extractedBits = []

for index in shuffledIndices:
    x = index % width
    y = index // width

    pixel = pixels[x, y]
    channelValue = pixel[colourPlane]
    binaryValue = format(channelValue, '08b')

    extractedBits.append(binaryValue[significantBit])

lengthBits = extractedBits[:14]
messageLength = int(''.join(lengthBits), 2)

messageBits = extractedBits[14:14 + messageLength * 7]

message = ""

for i in range(0, len(messageBits), 7):
    charBits = messageBits[i:i + 7]
    character = chr(int(''.join(charBits), 2))
    message += character

print("Recovered secret message:")
print(message)