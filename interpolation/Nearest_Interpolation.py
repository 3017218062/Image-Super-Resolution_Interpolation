from tool.imageTool import *


def nearestInterpolation(image, newShape=(1024, 1024)):
    oldHeight, oldWidth, (newHeight, newWidth) = image.shape[0], image.shape[1], newShape
    hScale, wScale = oldHeight / newHeight, oldWidth / newWidth

    X = np.asarray([list(range(newHeight))] * newWidth).T
    Y = np.asarray([list(range(newWidth))] * newHeight)
    X = np.floor((X + 0.5) * hScale).astype("int")
    Y = np.floor((Y + 0.5) * wScale).astype("int")

    Os = []
    for i in range(3):
        O = image[X, Y][:, :, i]
        Os.append(O.reshape(-1))
    Os = np.asarray(Os).T
    newImage = Os.reshape((newHeight, newWidth, 3)).astype(np.uint8)

    # for i in range(newHeight):
    #     x = int((i + 0.5) * hScale)
    #     for j in range(newWidth):
    #         y = int((j + 0.5) * wScale)
    #         newImage[i, j] = image[x, y]
    return newImage


if __name__ == "__main__":
    image = imageLoad()
    newImage = nearestInterpolation(image, newShape=(1024, 1024))
    imageSave(newImage, "flower_nearest.jpg")
