from tool.imageTool import *


def bilinearInterpolation(image, newShape=(1024, 1024)):
    oldHeight, oldWidth, (newHeight, newWidth) = image.shape[0], image.shape[1], newShape
    newImage = np.zeros((newHeight, newWidth, 3), dtype=np.uint8)
    hScale, wScale = oldHeight / newHeight, oldWidth / newWidth

    for i in range(newHeight):
        x = (i + 0.5) * hScale - 0.5
        xUp, xDown = int(x), int(x + 1) if int(x + 1) < oldHeight else int(x)
        x = x % 1
        for j in range(newWidth):
            y = (j + 0.5) * wScale - 0.5
            yLeft, yRight = int(y), int(y + 1) if int(y + 1) < oldHeight else int(y)
            y = y % 1

            X, Y = np.asarray([1 - x, x]), np.asarray([[1 - y, 0, 0],
                                                       [y, 0, 0],
                                                       [0, 1 - y, 0],
                                                       [0, y, 0],
                                                       [0, 0, 1 - y],
                                                       [0, 0, y]])
            adjacentLattice = np.asarray([
                [image[xUp, yLeft, 0], image[xUp, yRight, 0], image[xUp, yLeft, 1], image[xUp, yRight, 1], image[xUp, yLeft, 2], image[xUp, yRight, 2]],
                [image[xDown, yLeft, 0], image[xDown, yRight, 0], image[xDown, yLeft, 1], image[xDown, yRight, 1], image[xDown, yLeft, 2], image[xDown, yRight, 2]]
            ])
            newImage[i, j] = np.dot(np.dot(X, adjacentLattice), Y)

    return newImage


if __name__ == "__main__":
    image = imageLoad()
    newImage = bilinearInterpolation(image, newShape=(1024, 1024))
    imageSave(newImage, "flower_bilinear.jpg")
