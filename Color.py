#!/usr/bin/python3

class Color:
    def __init__(self, red, green, blue, alpha = None):
        self.R = red
        self.G = green
        self.B = blue
        self.A = alpha
        self.RGB = (red, green, blue)
        self.RGBA = (red, green, blue, alpha)

    def getHex(self):
        hex = "#{:02x}{:02x}{:02x}".format(self.R,self.G,self.B)
        return hex

    def setHex(self, hexi):
        rgb = tuple(map(ord,hexi[1:].decode('hex')))
        self.R = rgb[0]
        self.G = rgb[1]
        self.B = rgb[2]
        self.RGB = rgb
        self.RGBA = (self.R, self.G, self.B, self.A)

        
        
