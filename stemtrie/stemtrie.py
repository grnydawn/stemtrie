# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""Trie library for stemcode applications."""

from pygtrie import StringTrie, _Node

class StemTrie(StringTrie):

    def get_children(self, node=None):
        node = node if node and isinstance(node, _Node) else self._root
        for k in node.children:
            t = self.__class__()
            t._root = self._root.children[k]
            t._sorted = self._sorted
            yield k, t

    def get_child(self, name, node=None):
        node = node if node and isinstance(node, _Node) else self._root
        for k in node.children:
            if k == name:
                t = self.__class__()
                t._root = self._root.children[k]
                t._sorted = self._sorted
                return t
        raise Exception("%s is not a child"%name)
