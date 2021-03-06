#I have to make this a bit more readable than the previous one.

import os
import cv2
import sys
import numpy as np

#imgPath = 'C:\\Users\\Samir\\Pictures\\surf.jpg'
#bits = 8
def importThings():
    import cv2
    import sys
    import numpy as np
    import os


def resizingFile(imgPath, width, height):

    img = cv2.imread(imgPath)
    resizedPath = ((imgPath[:-4])+ '_' + str(width) + 'x' + str(height) + '.png')
    resizeImg = cv2.resize(img, [width,height], interpolation= cv2.INTER_AREA)
    cv2.imwrite(resizePath, resizeImg)


def countPercentage(count, total):
    percentage = int((float(count)/float(total))*100.0)
    print(str(percentage), end="\r", flush=True)

def dominantColors(imgPath, bits):

    img3 = cv2.imread(imgPath)
    width = len(img3[0])
    height = len(img3)
    divisor1 = 256/bits
    total = height * width
    count = 0
    colorRange = np.zeros((int(bits), int(bits), int(bits)))
    for t in range(0, height):
        for u in range(0, width):
            foo = img3[t][u]
            foo1 = foo[0]/divisor1
            foo2 = foo[1]/divisor1
            foo3 = foo[2]/divisor1
            colorRange[int(foo1)][int(foo2)][int(foo3)] += int(1)
            count += 1
        countPercentage(count, total)
    return colorRange


def colorSorter(testArray):
    arr = testArray
    sumArr = 0
    arrSize = len(arr)*len(arr)*len(arr)
    color2Darr = np.zeros((arrSize, 2))
    color2Darr = color2Darr.tolist()
    for v in range(0, len(arr)):
        for x in range(0, len(arr[v])):
            for y in range(0, len(arr[x])):
                arrValue = arr[v][x][y]
                colorVal = [v, x, y]
                color2Darr[sumArr][0] = arrValue
                color2Darr[sumArr][1] = list(colorVal)
                sumArr += 1
    arr2 = np.zeros((arrSize))
    arr2 = arr2.tolist()
    zeroCount = arrSize-1
    maxSize = arrSize-1
    for v in range(0,len(color2Darr)):
        microCount = 0
        arr2[v] = maxSize
        if color2Darr[v][0] >= 1:  
            for x in range(0,len(color2Darr)):
                if color2Darr[v][0] > color2Darr[x][0]:
                    arr2[v] -= 1
                if color2Darr[v][0] == color2Darr[x][0]:
                    for y in range(0, v):
                        if color2Darr[v][0] == color2Darr[y][0]:
                            microCount += 1
                    arr2[v] -= microCount
        if color2Darr[v][0] == 0:
            arr2[v] = zeroCount
            zeroCount -= 1
    arr3 = np.zeros((arrSize, 4))
    arr3 = arr3.tolist()
    for v in range(0,len(color2Darr)):
        arr3[arr2[v]][0] = arr2[v]
        arr3[arr2[v]][1] = v
        arr3[arr2[v]][2] = color2Darr[v][0]
        arr3[arr2[v]][3] = color2Darr[v][1]
    return arr3

