"""
    test_htmlx
    ~~~~~~~~~~~~
    - unit tests for htmlx
    # TODO - tests for all bs5 pages
"""

import unittest

from htmlx.xml.mathml import *

# import requests
# from mock import patch

# from htmlx import htmlx

# from htmlx.decorators import silence


class TestCase(unittest.TestCase):

    def test_mathml(self):
        somemath = math_(
            maction('x'),
            menclose('x'),
            merror('x'),
            mfenced('x'),
            mfrac('x'),
            mi('x'),
            mmultiscripts('x'),
            mn('x'),
            mo('x'),
            mover('x'),
            mpadded('x'),
            mphantom('x'),
            mroot('x'),
            mrow('x'),
            ms('x'),
            mspace('x'),
            msqrt('x'),
            mstyle('x'),
            msub('x'),
            msubsup('x'),
            msup('x'),
            mtable('x'),
            mtd('x'),
            mtext('x'),
            mtr('x'),
            munder('x'),
            munderover('x'),
            semantics('x'),
            maligngroup('x'),
            malignmark('x'),
            msline('x'),
            msgroup('x'),
            mlongdiv('x'),
            mstyle('x'),
            mprescripts('x'),
            mscarries('x'),
            mscarry('x'),
            munder('x'),
            munderover('x'),
            none('x'),
        )

        print(somemath)


if __name__ == '__main__':
    unittest.main()
