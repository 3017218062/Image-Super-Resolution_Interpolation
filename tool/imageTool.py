import numpy as np
from PIL import Image


def imageLoad():
    image = Image.open(r"../image/flower.jpg")
    image = np.asarray(image)
    return image

def imageSave(image):
    Image.fromarray(image).save(r"../result/flower.jpg")


# if __name__ == "__main__":
#     print(imageLoad().shape)
