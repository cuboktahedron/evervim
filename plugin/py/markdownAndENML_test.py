# encoding: utf-8
# vim: sts=4 sw=4 fdm=marker
# Author: kakkyz <kakkyz81@gmail.com>
# License: MIT
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
import markdownAndENML
import unittest
from xml.dom import minidom


class TestMarkdownAndENML(unittest.TestCase):
    """ doc """

    def setUp(self):  # {{{
        pass
    #}}}

    """ there is no test """

if __name__ == '__main__':
    from time import localtime, strftime
    print '\n**' + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + '**\n'
# profileを取るとき
#   import test.pystone
#   import cProfile
#   import pstats
#   prof = cProfile.run("unittest.main()", 'cprof.prof')
#   p = pstats.Stats('cprof.prof')
#   p.strip_dirs()
#   p.sort_stats('cumulative')
#   p.print_stats()
#
# 全て流す時
    unittest.main()
#
# 個別でテストするとき
#   suite = unittest.TestSuite()
#   suite.addTest(TestMarkdownAndENML('testParseENML'))
#   unittest.TextTestRunner().run(suite)
