import numpy as np
from PIL import Image


def imageLoad():
    image = Image.open(r"../image/flower.jpg")
    image = np.asarray(image)
    return image


def imageSave(image, imageName="flower.jpg"):
    Image.fromarray(image).save(r"../result/%s" % imageName)

# if __name__ == "__main__":
#     print(imageLoad().shape)
