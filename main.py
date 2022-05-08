# Note opencv uses BGR not RGB!

import cv2 as cv
import numpy as np


def draw_line_automatically(img):
    """ Using built-in function"""
    cv.line(img, (0,0), (500,500), (255,0,0), 1)


def draw_line_slowly(img):
    """Accessing each value using python = operator"""
    for i in range(0,500):
        img[i,i] = [255,0,0]


def draw_line_itemset(img):
    """Using itemset"""
    for i in range(0,500):
        img.itemset((i,i,0), 255)
        img.itemset((i,i,1), 0)
        img.itemset((i,i,2), 0)

def copy_can(img):
    """Copies can image to top right corner"""
    can = img[0:150, 250:500]
    img[0:150, 0:250] = can


sample_image = cv.imread("sample.jpg")
sample_image = cv.resize(sample_image, (500,500))
copy_can(sample_image)

print(sample_image.shape)
cv.imshow("Sample", sample_image)
k = cv.waitKey(0)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
