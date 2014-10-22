# coding:utf-8

import cv2
import numpy as np

im = cv2.imread(r'lena.jpg', cv2.IMREAD_COLOR)
cv2.imshow('lena', im)
cv2.waitKey(0)
