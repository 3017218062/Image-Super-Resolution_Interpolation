- Attention please: 

- If you want to reprint my article, please mark the original address and author(刘书裴).

- If you are puzzled about a certain part, you can contact me: 3017218062@tju.edu.cn/1005968086@qq.com

- Thanks watching!

# 1. Nearest Interpolation

## {1} Algorithm

### [1] Coordinate mapping

#### (1) For example:

Here is the pixel distribution of the two pictures(src:3x3 and dst:5x5):

![](../resource/interpolation/Nearest_Interpolation/image1.png)

Then overlap two pictures:

![](../resource/interpolation/Nearest_Interpolation/image2.png)

Choose the white pixel and  calculate it:

```
1. Take the boundary pixel of the upper left corner as the origin (0,0).
    For the destination matrix, the pixel I choose is (2,1).
        realPixel1 = (2, 1)
    Calculate the ratio between src and dst:
        heightRatio = srcHeight / dstHeight = 0.6
        widthRatio = srcWidth / dstWidth = 0.6
2. Take the boundary point of the upper left corner as the origin (0,0).
    For the white pixel, its coordinate in destination matrix is (2.5,1.5):
        realPixel2 = (2.5, 1.5) => _realPixel2 = realPixel1 + (0.5, 0.5)
3. Converts coordinates from the dst coordinate system to the src coordinate system:
        virtualPixel2 = realPixel2 * (heightRatio, widthRatio) = (1.5, 0.9)
        virtualPixel1 = (1.0, 0.4) => virtualPixel1 = virtualPixel2 - (0.5, 0.5)
4. In summary:
    virtualPixel = (realPixel + 0.5) * (heightRatio, WidthRatio) - 0.5
```

### [2] Fill the nearest

For nearest, we only need to take the rounding value of the corresponding coordinates.

```python
nearestPixel = int(virtualPixel + 0.5)
```

## {2} Attention

### [1] Why we create two coordinate systems?

If we choose single coordinate system like pixel coordinate, the virtualPixel(realPixel*ratio) may be out of bounds when the radtio is greater than or equal to 0.5. For point coordinate, it can't represents the pixel between two points.

As an example, for the realPixel (src:3x3,dst:6x6), int((5,5)*0.5)=int((2.5,2.5))=(3,3) is out of range(0,3).

### [2] Why we add 0.5 to virtualPixel?

For many programming languages, they can remove data after decimal point when they change the type of float to int.

And Adding 0.5 can a number greater than or equal to 0.5 to add 1 to its integer.

# 2. Bilinear Interpolation

## {1} Algorithm

