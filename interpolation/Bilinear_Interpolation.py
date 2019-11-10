from tool.imageTool import *


def bilinearInterpolation(image, newShape=(1024, 1024)):
    oldHeight, oldWidth, (newHeight, newWidth) = image.shape[0], image.shape[1], newShape
    newImage = np.zeros((newHeight, newWidth, 3), dtype=np.uint8)
    hScale, wScale = oldHeight / newHeight, oldWidth / newWidth

    for i in range(newHeight):
        x = (i + 0.5) * hScale - 0.5
        xUp, xDown = int(x), int(x + 1)
        if xDown == oldHeight:
            xDown -= 1
        x = x % 1
        for j in range(newWidth):
            y = (j + 0.5) * wScale - 0.5
            yLeft, yRight = int(y), int(y + 1)
            if yRight == oldWidth:
                yRight -= 1
            y = y % 1

            X, Y = np.asarray([1 - x, x]), np.asarray([[1 - y], [y]])
            for k in range(3):
                adjacentLattice = np.asarray([[image[xUp, yLeft, k], image[xUp, yRight, k]],
                                              [image[xDown, yLeft, k], image[xDown, yRight, k]]])
                newImage[i, j, k] = np.dot(np.dot(X, adjacentLattice), Y)

    return newImage.astype(np.uint8)


if __name__ == "__main__":
    image = imageLoad()
    newImage = bilinearInterpolation(image, newShape=(1024, 1024))
    imageSave(newImage, "flower_bilinear.jpg")
