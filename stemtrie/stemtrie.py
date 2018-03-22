# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""Trie library for stemcode applications."""

from pygtrie import StringTrie, _Node, _SENTINEL

class StemTrie(StringTrie):

    def get_children(self, with_value=False):
        for k, child in self._root.children.items():
            v = None if self._root.value == _SENTINEL else self_root.value
            if child:
                t = self.__class__()
                t._root = child
                t._sorted = self._sorted
            else:
                t = None
            if with_value:
                yield k, v, t
            else:
                yield k, t

    def get_child(self, name, with_value=False):
        for k, child in self._root.children.items():
            v = None if self._root.value == _SENTINEL else self_root.value
            if k == name:
                t = self.__class__()
                t._root = child
                t._sorted = self._sorted
                if with_value:
                    return v, t
                else:
                    return t
        raise Exception("%s is not a child"%name)
