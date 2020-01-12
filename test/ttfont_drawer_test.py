import unittest
from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / "src"))

import src.ttfont_drawer as ttf  # noqa


class TestTtfontDrawer(unittest.TestCase):

    def setUp(self):
        self.font_dir = 'C:/Windows/Fonts'

    def test_has_glyph(self):
        # contains_japanese_ttf = os.path.join(self.font_dir, 'HGRSMP.TTF')
        contains_japanese_ttf = self._get_font_path('HGRSMP.TTF')
        self.assertTrue(ttf.has_glyph(contains_japanese_ttf, 'あ'))

        not_contains_japanese_ttf = self._get_font_path('consola.ttf')
        self.assertFalse(ttf.has_glyph(not_contains_japanese_ttf, 'あ'))

    def _get_font_path(self, ttf_filename):
        return os.path.join(self.font_dir, ttf_filename)


if __name__ == '__main__':
    unittest.main()

print(ttf.has_glyph(None, None))
