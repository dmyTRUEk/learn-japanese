"""
Kanji or Word symbols class
"""

from extensions_python import assert_, beautiful_repr, is_latin, unreachable
from extensions_pipe import all_, flatten_
from extensions_for_japanese import is_kana, is_translitable_to_kana, translit_to_kana, translit_to_latin



@beautiful_repr
class JapaneseWord:
    word: str
    translation: str | list[str] # to english
    description: None | str = None
    latin_spelling: str | list[str]
    kana_spelling: None | str | list[str] = None

    def __init__(
            self,
            word: str,
            translation_to_english: str | list[str],
            /, *,
            ls: None | str | list[str] = None, # latin spelling
            ks: None | str | list[str] = None, # kana spelling
            desc: None | str = None,
            ):
        self.word = word
        self.translation = translation_to_english
        if ks is not None:
            assert(is_kana(ks))
            self.kana_spelling = ks
        else:
            self._ls = ls
            self._ks = ks
        self.description = desc

    def init_spelling(self):
        if self.kana_spelling is not None:
            match self.kana_spelling:
                case str(ks):
                    self.latin_spelling = translit_to_latin(ks)
                case list(kss):
                    self.latin_spelling = [translit_to_latin(ks) for ks in kss] | flatten_
            return

        ls = self._ls
        ks = self._ks
        del self._ls
        del self._ks

        if is_translitable_to_kana(self.word):
            ks = translit_to_kana(self.word)
        else:
            # raise Exception("word is NOT translitable")
            pass

        self.kana_spelling = ks

        if (ks is not None) and (ls is None):
            match ks:
                case str(ks):
                    ls = translit_to_latin(ks)
                case list(kss):
                    ls = [translit_to_latin(ks) for ks in kss] | flatten_
                case _:
                    unreachable()

        assert_(ls is not None, "No spelling provided and can't figure it out automatically.")
        assert(ls is not None)
        self.latin_spelling = ls

        assert(
            (self.kana_spelling is None) or
            (self.kana_spelling | all_(lambda symbol: is_kana(symbol)))
        )
        assert(self.latin_spelling | all_(lambda symbol: is_latin(symbol)))

