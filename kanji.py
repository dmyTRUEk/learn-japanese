# This is file with Kanji

from japanese_symbols_classes import JapaneseKanji

ALL_KANJI: list[JapaneseKanji] = [
    #JapaneseKanji("", "", ""),

    JapaneseKanji("一", "ichi", ["1", "one"]),
    JapaneseKanji("二", "ni", ["2", "two"]),
    JapaneseKanji("三", "san", ["3", "three"]),
    JapaneseKanji("四", ["yon", "shi"], ["4", "four"]),
    JapaneseKanji("五", "go", ["5", "five"]),
    JapaneseKanji("六", "roku", ["6", "six"]),
    JapaneseKanji("七", ["shichi", "nana"], ["7", "seven"]),
    JapaneseKanji("八", "hachi", ["8", "eight"]),
    JapaneseKanji("九", "kyu", ["9", "nine"]),
    JapaneseKanji("十", "ju", ["10", "ten"]),
    JapaneseKanji("百", "hyaku", ["100", "hundred"]),
    JapaneseKanji("千", "sen", ["1000", "thousand", "1_000"]),
    JapaneseKanji("万", "man", ["10000", "ten thousand", "10_000"]),

    JapaneseKanji("私", "watashi", "i"),
]

