"""
Some functions to work with Japanese
"""

from pipe import all, map

from extensions_python import char, find_all, unreachable

from kana import JAPANESE_LETTERS
import kanji



JAPANESE_PUNCTUATION_TO_ENG: dict[char, char] = {
    '。': '.',
    '、': ',',
    '！': '!',
    '？': '?',
}


def is_kana(string: str) -> bool:
    return (string | all(lambda ch:
        (ch in JAPANESE_LETTERS | map(lambda l: l.hiragana)) or
        (ch in JAPANESE_LETTERS | map(lambda l: l.katakana)) or
        (ch in JAPANESE_PUNCTUATION_TO_ENG)
    ))


def is_translitable(string: str) -> bool:
    for symbol in string:
        if symbol in JAPANESE_PUNCTUATION_TO_ENG:
            continue
        elif find_all(kanji.JAPANESE_WORDS, lambda jw: symbol == jw.word) is not None:
            continue
        elif (found:=find_all(JAPANESE_LETTERS, lambda l: symbol in [l.hiragana, l.katakana])) is not None:
            assert(len(found) == 1)
            continue
        else:
            return False
    return True


def translit_to_kana(japanese_word: str) -> str | list[str]:
    kana_spelling: str | list[str] = ""
    for symbol in japanese_word:
        if symbol in JAPANESE_PUNCTUATION_TO_ENG:
            kana_spelling += symbol
        elif is_kana(symbol):
            kana_spelling += symbol
        elif (found:=find_all(kanji.JAPANESE_WORDS, lambda jw: symbol == jw.word)) is not None:
            assert(len(found) == 1)
            word = found[0]
            assert(word.kana_spelling is not None)
            ks: str | list[str] = word.kana_spelling
            match ks:
                case str(_ks):
                    kana_spelling += _ks
                case list(kss):
                    kana_spelling = kss | map(lambda _ks: kana_spelling + _ks)
                case _:
                    unreachable()
        else:
            unreachable()
    return kana_spelling


def translit_to_latin(japanese_word: str) -> str | list[str]:
    latin_spelling: str | list[str] = ""
    for symbol in japanese_word:
        if symbol in JAPANESE_PUNCTUATION_TO_ENG:
            lss = JAPANESE_PUNCTUATION_TO_ENG[symbol]
            latin_spelling += lss
        elif is_kana(symbol):
            lss = find_all(JAPANESE_LETTERS, lambda l: symbol in [l.hiragana, l.katakana])
            assert(lss is not None)
            assert(len(lss) == 1)
            lss = lss[0]
            latin_spelling += lss.latin_spelling
        elif (found:=find_all(kanji.JAPANESE_WORDS, lambda jw: symbol == jw.word)) is not None:
            assert(len(found) == 1)
            ls: str | list[str] = found[0].latin_spelling
            match ls:
                case str(_ls):
                    latin_spelling += _ls
                case list(lss):
                    latin_spelling = lss | map(lambda _ls: latin_spelling + _ls)
                case _:
                    unreachable()
        else:
            unreachable()
    return latin_spelling


def japanese_uppercase(string: str):
    res = ""
    for ch in string:
        match ch:
            case 'ゃ':
                res += 'や'
            case 'ゅ':
                res += 'ゆ'
            case 'ょ':
                res += 'よ'
            case _:
                res += ch
    return res
