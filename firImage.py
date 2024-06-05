import cv2
import numpy as np
from PIL import Image

def filterImage(path, passType):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    sigma = 2.0
    len_f = int(6 * sigma)
    n = np.arange(-len_f // 2, len_f // 2 + 1)

    h = np.exp(-n**2 / (2 * sigma**2))
    if passType == "low":
        h /= h.sum()
    elif passType == "high":
        h -= h.mean()
    kernel = np.outer(h, h)

    filtered_image = cv2.filter2D(image, -1, kernel)

    return Image.fromarray(filtered_image)