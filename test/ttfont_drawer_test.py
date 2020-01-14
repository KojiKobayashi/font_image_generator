import unittest
from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / "src"))

from src.ttfont_drawer import TtfDrawer  # noqa


class TestTtfontDrawer(unittest.TestCase):

    def setUp(self):
        self._font_dir = 'C:/Windows/Fonts'
        self._ttf_japanese = TtfDrawer(self._get_font_path('HGRSMP.TTF'))

    def test_has_glyph(self):
        ttf = TtfDrawer(self._get_font_path('HGRSMP.TTF'))
        self.assertTrue(ttf.has_glyph('あ'))

        ttf = TtfDrawer(self._get_font_path('consola.ttf'))
        self.assertFalse(ttf.has_glyph('あ'))

    def test_draw(self):
        ret = self._ttf_japanese.draw('あ', 32)
        self.assertEqual((32, 32), ret.size)

    def _get_font_path(self, ttf_filename):
        return os.path.join(self._font_dir, ttf_filename)


if __name__ == '__main__':
    unittest.main()

print(ttf.has_glyph(None, None))
