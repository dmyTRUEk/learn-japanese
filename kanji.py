"""
Kanji and Words
"""

from kanji_class import JapaneseWord



JAPANESE_WORDS: list[JapaneseWord] = [
    JapaneseWord("一", ["1", "one"], ls="ichi"),
    JapaneseWord("二", ["2", "two"], ls="ni"),
    JapaneseWord("三", ["3", "three"], ls="san"),
    JapaneseWord("四", ["4", "four"], ls=["yon", "shi"]),
    JapaneseWord("五", ["5", "five"], ls="go"),
    JapaneseWord("六", ["6", "six"], ls="roku"),
    JapaneseWord("七", ["7", "seven"], ls=["shichi", "nana"]),
    JapaneseWord("八", ["8", "eight"], ls="hachi"),
    JapaneseWord("九", ["9", "nine"], ls=["ku", "kyu"]),
    JapaneseWord("十", ["10", "ten"], ls="jyu"),
    JapaneseWord("百", ["100", "hundred"], ls="hyaku"),
    JapaneseWord("千", ["1000", "thousand", "1_000"], ls="sen"),
    JapaneseWord("万", ["10000", "ten thousand", "10_000", "ten thousands"], ls="man"),

    JapaneseWord("私", "i", ls="watashi"),

    #JapaneseWord("", "", ks=""),
]

