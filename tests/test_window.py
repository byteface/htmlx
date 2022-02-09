"""
    test_window
    ~~~~~~~~~~~~~~~~
"""

import unittest

from htmlx.decorators import *
# from htmlx.dom import *
# from htmlx.javascript import *
# from htmlx.webapi import *
from htmlx.window import *


class TestCase(unittest.TestCase):

    @silence
    def test_window(self):
        window.location = "http://www.google.com"
        # print(window.document.body.innerHTML)
        print(window.document.title)


if __name__ == '__main__':
    unittest.main()
