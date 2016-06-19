# encoding: utf-8
# vim: sts=4 sw=4 fdm=marker
# Author: kakkyz <kakkyz81@gmail.com>
# License: MIT
import markdown


def parseMarkdown(mkdtext):  # {{{
    m = markdown.markdown(mkdtext.decode('utf-8'), extensions=['gfm'])
    return m
#}}}

if __name__ == "__main__":
    import doctest
    doctest.testmod()
