#!/usr/bin/python3

import operator
import os
from PIL import Image

imageName = input("Image name: ")
limit = int(input("How many colors would you like?: "))
ignoreDarkLimit = int(input("Ignore colors darker than(0-75): ")) #0-75
ignoreLightLimit = int(input("Ignore colors lighter than(750-765): "))#765

img = None
try:
    img = Image.open(imageName)
except:
    print("No file with that name")

width, height = img.size
pixels = img.load()
#put pixels in counting dictionary
colDict = {}
for x in range(height):
    for y in range(width):
        pix = pixels[y,x]
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
        grey = (sum(sortedTop[c][0])/3)
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
        
