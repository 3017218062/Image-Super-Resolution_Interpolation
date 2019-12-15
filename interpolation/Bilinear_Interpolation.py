from tool.imageTool import *


def bilinearInterpolation(image, newShape=(1024, 1024)):
    oldHeight, oldWidth, (newHeight, newWidth) = image.shape[0], image.shape[1], newShape
    hScale, wScale = oldHeight / newHeight, oldWidth / newWidth

    X, Y = np.asarray([list(range(newHeight))] * newWidth).T, np.asarray([list(range(newWidth))] * newHeight)
    X, Y = (X + 0.5) * hScale - 0.5, (Y + 0.5) * wScale - 0.5

    ups = X.astype("int")
    lefts = Y.astype("int")
    _X, _Y = X.copy(), Y.copy()
    _X[_X + 1 < oldHeight] += 1
    _Y[_Y + 1 < oldWidth] += 1
    downs = _X.astype("int")
    rights = _Y.astype("int")

    Os = []
    for i in range(3):
        A, B = image[ups, lefts][:, :, i], image[ups, rights][:, :, i]
        C, D = image[downs, lefts][:, :, i], image[downs, rights][:, :, i]
        AB = (rights - Y) * A + (Y - lefts) * B
        CD = (rights - Y) * C + (Y - lefts) * D
        O = (downs - X) * AB + (X - ups) * CD
        Os.append(O.reshape(-1))
    Os = np.asarray(Os, dtype=np.uint8).T
    newImage = Os.reshape((newHeight, newWidth, 3))
    return newImage


if __name__ == "__main__":
    image = imageLoad()
    newImage = bilinearInterpolation(image, newShape=(1024, 1024))
    imageSave(newImage, "flower_bilinear.jpg")
