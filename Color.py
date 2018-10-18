#!/usr/bin/python3

class Color:
    def __init__(self, red, green, blue, alpha = None):
        self.R = float(red)
        self.G = float(green)
        self.B = float(blue)
        self.A = float(alpha)
        self.RGB = (red, green, blue)
        self.RGBA = (red, green, blue, alpha)

    def getHex(self):
        """
        return hexidecimal value of color
        """
        hex = "#{:02x}{:02x}{:02x}".format(self.R,self.G,self.B)
        return hex

    def getGray(self,mode=None):
        """
        return greyscale value of color
        calculated by
        average,
        lightness,
        luminosity
        """
        grey = -1.0
        #average
        if mode == None or mode[0].lower != 'l':
            grey = sum(self.RGB)/3
        #lightness
        elif len(mode) >= 5 and mode[0:4].lower == 'light':
            grey = (max(self.RGB) + min(self.RGB)) / 2
        #luminosity
        elif len(mode) >= 3 and mode[0:2].lower == 'lum':
            alt[0] = self.R * 0.21
            alt[1] = self.G * 0.72
            alt[2] = self.B * 0.07
            grey = sum(alt)
        return grey

    def getGrey(self, mode=None):
        """
        calls getGray.
        This exists to avoid spelling confusion
        """
        return self.getGray(mode)

    def setHex(self, hexi):
        """
        set color based on hexidecimal value
        """
        rgb = tuple(map(ord,hexi[1:].decode('hex')))
        self.R = rgb[0]
        self.G = rgb[1]
        self.B = rgb[2]
        self.RGB = rgb
        self.RGBA = (self.R, self.G, self.B, self.A)
        
        
