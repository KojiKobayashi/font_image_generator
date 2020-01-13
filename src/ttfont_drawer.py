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

    def has_glyph(self, glyph):
        #font = TTFont(font_path)
        for table in self._font['cmap'].tables:
            if ord(glyph) in table.cmap.keys():
                return True
        return False
