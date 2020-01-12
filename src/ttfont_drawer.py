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


def has_glyph(font_path, glyph):
    font = TTFont(font_path)
    for table in font['cmap'].tables:
        if ord(glyph) in table.cmap.keys():
            return True
    return False
