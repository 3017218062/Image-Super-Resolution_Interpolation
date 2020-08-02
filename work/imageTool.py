import numpy as np
from PIL import Image


def imageLoad():
    image = Image.open("../input/flower.jpg")
    image = np.asarray(image)
    return image


def imageSave(image, imageName="flower.jpg"):
    Image.fromarray(image).save("../output/%s" % imageName)
