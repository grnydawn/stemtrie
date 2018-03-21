# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""Trie library for stemcode applications."""

from pygtrie import StringTrie, _Node

class StemTrie(StringTrie):

    @property
    def subtrie(self, node=None):
        node = node if node and isinstance(node, _Node) else self._root
        for k in node.children:
            t = self.__class__()
            t._root = self._root.children[k]
            t._sorted = self._sorted
            yield k, t
