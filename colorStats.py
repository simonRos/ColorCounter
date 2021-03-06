#!/usr/bin/python3

import operator
import os
try:
    from PIL import Image
except Exception as e1:
    try:
        print(str(e1) + " Trying alternative module.")
        import Image
        print("Alt mod successful")
    except Exception as e2:
        print(e2)
try:
    from PIL import ImageSequence
except Exception as e3:
    try:
        print(str(e3) + " Trying alternative module.")
        import ImageSequence
        print("Alt mod successful")
    except Exception as e4:
        print(e4)
try:
    imageName = input("Image name: ")
    img = Image.open(imageName)
except:
    print("No file with that name")
    raise SystemExit

limit = 10
try:
    limit = int(input("How many colors would you like?(10): "))
except:
    pass
ignoreDarkLimit = 50
try:
    ignoreDarkLimit = int(input("Ignore colors darker than(50): "))
except:
    pass
ignoreLightLimit = 200
try:
    ignoreLightLimit = int(input("Ignore colors lighter than(200): "))
except:
    pass

colDict = {}
#.gifs have multiple frames
i = 1
for frame in ImageSequence.Iterator(img):
    frame = frame.convert('RGB')
    #put pixels in counting dictionary
    width, height = frame.size
    pixels = frame.load()
    for y in range(height):
        for x in range(width):
            pix = pixels[x,y]
            if pix in colDict:
                colDict[pix] += 1
            else:
                colDict[pix] = 1
sortedTop = sorted(colDict.items(), key=operator.itemgetter(1), reverse = True)

fName = imageName.split('.')[0]+'.html'
with open(fName, 'w') as f:
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<style>\n")
    f.write("b{color: white; \
text-shadow:-1px -1px 0 #000, \
1px -1px 0 #000, \
-1px 1px 0 #000, \
1px 1px 0 #000;  }")
    f.write("</style>\n")
    f.write("<title>")
    f.write(imageName)
    f.write("</title>\n")
    f.write("<body>\n")
    f.write("<div>\n")
    f.write("<img src='"+os.path.abspath(os.path.realpath(imageName))+"'>")
    f.write("</div>\n")
    f.write("<div>\n")
    f.write("<ol type='1'>\n")
    c = 0
    while c < limit and c < len(sortedTop):
        #simple, average greyscaling
        grey = sortedTop[c][0][0] * 0.21
        grey+= sortedTop[c][0][1] * 0.72
        grey+= sortedTop[c][0][2] * 0.07
        if (grey < ignoreLightLimit
            and grey > ignoreDarkLimit):
            f.write("<li>\n")
            f.write("<p style='background-color:rgb"+str(sortedTop[c][0])+"'>")
            hexi = "#{:02x}{:02x}{:02x}".format(sortedTop[c][0][0],
                                                sortedTop[c][0][1],
                                                sortedTop[c][0][2])
            f.write("<b>")
            f.write(str(hexi)+" "+str(sortedTop[c][0]))
            f.write("</b>")
            f.write("<ul><li>Pixel count: "+str(sortedTop[c][1])+"</li></ul>")
            f.write("<p>\n")
            f.write("</li>\n")
        else:
            limit+=1
        c += 1
    f.write("</ol>\n")
    f.write("</div>\n")
    f.write("</body>\n")
    f.write("</html>\n")

