"""
Unit Tests
"""

from unittest_class import unittest

from extensions_for_japanese import is_kana



@unittest
def test_is_kana():
    assert(is_kana("あ"))
    assert(is_kana("いま"))
    assert(is_kana("おはよ！"))
    assert(not is_kana("abc"))
    assert(not is_kana("駆け引き"))

