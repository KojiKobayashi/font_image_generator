# import random
# import os
# import string
# import json
from PIL import Image, ImageDraw, ImageFont
# import numpy as np
# from scipy.ndimage.morphology import grey_dilation, grey_erosion
# from PIL import ImageFilter
# from skimage.util import random_noise, img_as_float
from fontTools.ttLib import TTFont
# from fontTools.unicode import Unicode


class TtfDrawer:
    def __init__(self, font_path):
        self._font = TTFont(font_path)
        self._font_path = font_path

    @property
    def font_path(self):
        return self._font_path

    def has_glyph(self, glyph):
        for table in self._font['cmap'].tables:
            if ord(glyph) in table.cmap.keys():
                return True
        return False

    def draw(self, glyph, char_size):
        if not self.has_glyph(glyph):
            return None

        font = ImageFont.truetype(self._font_path, char_size)

        im = Image.new(mode='L', size=(char_size, char_size), color='white')
        drawer = ImageDraw.Draw(im)
        drawer.text(xy=(0, 0), text=glyph, font=font, fill='black')

        return im
