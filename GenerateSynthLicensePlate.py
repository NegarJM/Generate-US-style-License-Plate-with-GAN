# coding=utf-8
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import cv2
import numpy as np
import os
from math import *
from random import randint
import argparse

chars_us = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# def GenCh(f, val):
#     img = Image.new("RGB", (45, 70), (255, 255, 255))
#     draw = ImageDraw.Draw(img)
#     draw.text((0, 3), val, (0, 0, 0), font=f)
#     img = img.resize((23, 70))
#     A = np.array(img)
#     return A


def GenCh1(f, val):
    img = Image.new("RGB", (23, 70), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((3, 12), val, (0, 0, 0), font=f)
    A = np.array(img)
    return A


def r(val):
    return int(np.random.random() * val)


class GenPlate:
    def __init__(self, fontUS):
        self.fontUS = ImageFont.truetype(fontUS, 43, 0)
        self.img = np.array(Image.new("RGB", (180, 80), (255, 255, 255)))
        self.bg = cv2.resize(cv2.imread("./images/template.bmp"), (180, 80))
        self.smu = cv2.imread("./images/smu2.jpg")

    def draw(self, val):
        offset = 2
        # offset = (160 - len(val) * 23 - (len(val) - 1) * 6) // 2
        for i, char in enumerate(val):
            self.img[
                0:70, offset + i * 23 + i * 6 : offset + (i + 1) * 23 + i * 6
            ] = GenCh1(self.fontUS, char)
        return self.img

    def generate(self, text):
        fg = self.draw(text)
        fg = cv2.bitwise_not(fg)
        com = cv2.bitwise_or(fg, self.bg)
        return com

    def genPlateString(self, pos, val):
        plateStr = ""
        box = [0] * 6
        if pos != -1:
            box[pos] = 1
        for unit, cpos in zip(box, range(len(box))):
            if unit == 1:
                plateStr += val
            else:
                if cpos < 3:
                    plateStr += chars_us[randint(10, 35)]
                else:
                    plateStr += chars_us[randint(0, 9)]

        return plateStr

    def genBatch(self, batchSize, pos, charRange, outputPath, size):
        if not os.path.exists(outputPath):
            os.mkdir(outputPath)
        for i in range(batchSize):
            plateStr = G.genPlateString(-1, -1)
            img = G.generate(plateStr)
            filename = os.path.join(
                outputPath, str(i).zfill(4) + "-" + plateStr + ".jpg"
            )
            cv2.imwrite(filename, img)


if __name__ == "__main__":
    # image = cv2.imread("./LicensePlateDataset/18854897fd142e.png")
    # print(image.shape)
    G = GenPlate("./license_plate_usa/us_license_plate.ttf")
    G.genBatch(100, 2, range(len(chars_us)), "./GeneratedPlateSamples", (180, 80))
