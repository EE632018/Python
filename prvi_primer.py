import cv2 as cv

img = cv.imread('Downloads/Slika.jpeg')

cv.imshow('Milos', img)

cv.waitKey(0)