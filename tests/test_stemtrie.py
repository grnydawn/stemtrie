#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stemtrie` package."""

import os
import stat
import sys
import pytest
from stemtrie import StemTrie

ROOT_DIR = '/usr/local'
SUB_DIR = os.path.join(ROOT_DIR, 'lib')
SUB_DIRS = tuple(os.path.join(ROOT_DIR, d)
                 for d in ('lib', 'lib32', 'lib64', 'share'))

@pytest.fixture
def trie():
    """Sample pytest fixture.
    """
    t = StemTrie()
    t['a/b'] = 'ab'
    t['a/c'] = 'ac'
    return t

@pytest.fixture
def dirtrie():
    """Sample pytest fixture.
    """

    t = StemTrie(separator=os.path.sep)

    # Read sizes regular files into a Trie
    for dirpath, unused_dirnames, filenames in os.walk(ROOT_DIR):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            try:
                filestat = os.stat(filename)
            except OSError:
                continue
            if stat.S_IFMT(filestat.st_mode) == stat.S_IFREG:
                t[filename] = filestat.st_size
    return t

def test_trie(trie):
    """Sample pytest test function with the pytest fixture as an argument."""
    assert trie['a/b'] == 'ab'
    assert trie['a/c'] == 'ac'

def test_add(trie):
    """Sample pytest test function with the pytest fixture as an argument."""
    trie['b'] = 'b'
    assert trie['b'] == 'b'
    assert len(trie) == 3

def test_del(trie):
    """Sample pytest test function with the pytest fixture as an argument."""
    del trie['a':]
    assert not trie.keys()
