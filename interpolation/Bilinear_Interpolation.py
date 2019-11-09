from tool.imageTool import *


def bilinearInterpolation(image, newShape=(1024, 1024)):
    oldHeight, oldWidth, (newHeight, newWidth) = image.shape[0], image.shape[1], newShape
    newImage = np.zeros((newHeight, newWidth, 3), dtype=np.uint8)
    hScale, wScale = oldHeight / newHeight, oldWidth / newWidth

    for i in range(newHeight):
        x = (i + 1) * hScale
        xUp, xDown = int(x)-1, int(x + 1)-1
        for j in range(newWidth):
            y = (j + 1) * wScale
            yLeft, yRight = int(y)-1, int(y + 1)-1

            # X,Y=np.asarray([1-x,x]),np.asarray([[1-y],[y]])
            # for k in range(3):
            #     adjacentLattice = np.asarray([[image[xUp,yLeft,[k]],image[xUp,yRight,[k]]],[image[xDown,yLeft,[k]],image[xDown,yRight,[k]]]])
            #     newImage[i,j,[k]]=np.dot(np.dot(X,adjacentLattice),Y)
            print(x,y,xUp, xDown,yLeft, yRight)
            break
        break
    return newImage

if __name__ == "__main__":
    image = imageLoad()
    newImage = bilinearInterpolation(image, newShape=(1024, 1024))
    imageSave(newImage)
