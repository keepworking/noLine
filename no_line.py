"""
Python captcha no line.

@hikai
"""
from PIL import Image


img = Image.open("captcha2.gif")
img = img.convert("RGBA")
pixdata = img.load()
mask = [1, -1]

for count in range(0, 3):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            edge = 0

            for i in range(len(mask)):
                try:
                    edge += pixdata[x, y + i][0] * mask[i]
                except:
                    continue

            edge = abs(edge)
            knee = 254
            if edge > knee:
                pixdata[x, y] = (255, 255, 255, 255)


img.save("unline.gif", "GIF")
