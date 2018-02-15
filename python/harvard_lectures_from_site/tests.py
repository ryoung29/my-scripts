"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import unittest

from download_lectures import *


class TestDownloadLectures(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        self.mediainfo = "Video: AVC; Audio: 'Opus'"
        self.url = 'http://people.seas.harvard.edu/~minilek/cs229r/fall15/lec.html'

    def test_acodec(self):
        codec = acodec(self.mediainfo)
        self.assertEqual(codec, 'aac')

    def test_vcodec(self):
        codec = vcodec(self.mediainfo)
        self.assertEqual(codec, 'copy')

    def test_get_links(self):
        pdf_links, video_links = get_links(self.url)
        self.assertEqual(len(pdf_links), 26)
        self.assertEqual(len(video_links), 25)


if __name__ == '__main__':
    unittest.main()
