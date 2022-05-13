"""
Kanji or Word symbols class
"""

from extensions_python import assert_, beautiful_repr, unreachable
from extensions_pipe import flatten
from extensions_for_japanese import is_translitable, translit_to_latin



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
                    self.latin_spelling = [translit_to_latin(ks) for ks in kss] | flatten
            return

        ls = self._ls
        ks = self._ks
        del self._ls
        del self._ks

        if is_translitable(self.word):
            ks = self.word
        else:
            raise Exception("word is NOT translitable")

        self.kana_spelling = ks

        if (ks is not None) and (ls is None):
            match ks:
                case str(ks):
                    ls = translit_to_latin(ks)
                case list(kss):
                    ls = [translit_to_latin(ks) for ks in kss]
                case _:
                    unreachable()

        assert_(ls is not None, "No spelling provided and can't figure it out automatically.")
        assert(ls is not None)
        self.latin_spelling = ls

