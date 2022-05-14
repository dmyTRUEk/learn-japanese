"""
Kanji and Words
"""

from kanji_class import JapaneseWord



JAPANESE_WORDS: list[JapaneseWord] = [
    JapaneseWord("一", ["1", "one"], ks="いち"),
    JapaneseWord("二", ["2", "two"], ks="に"),
    JapaneseWord("三", ["3", "three"], ks="さん"),
    JapaneseWord("四", ["4", "four"], ks=["よん", "し"]),
    JapaneseWord("五", ["5", "five"], ks="ご"),
    JapaneseWord("六", ["6", "six"], ks="ろく"),
    JapaneseWord("七", ["7", "seven"], ks=["しち", "なな"]),
    JapaneseWord("八", ["8", "eight"], ks="はち"),
    JapaneseWord("九", ["9", "nine"], ls=["ku", "kyu"]),
    JapaneseWord("十", ["10", "ten"], ls="jyu"),
    JapaneseWord("百", ["100", "hundred"], ls="hyaku"),
    JapaneseWord("千", ["1000", "thousand", "1_000"], ks="せん"),
    JapaneseWord("万", ["10000", "ten thousand", "10_000", "ten thousands"], ks="まん"),

    JapaneseWord("私", "i", ks="わたし"),
    JapaneseWord("人", ["human", "person", "people"], ks="ひと"),
    JapaneseWord("女", ["woman", "female", "women"],  ks="おんな"),
    JapaneseWord("男", ["man", "male", "men"], ks="おとこ"),
    JapaneseWord("光", ["light", "shine"], ks="ひかり"),

    JapaneseWord("あなた", "you"),
    JapaneseWord("ごぜん", ["AM", "am"], desc="before 12:00"),
    JapaneseWord("ごご",   ["PM", "pm"], desc="after 12:00"),
    JapaneseWord("から", "from", desc="from time"),
    JapaneseWord("まで", "till", desc="till time"),
    JapaneseWord("いま", "now"),
    JapaneseWord("すみません", ["sorry", "excuse me"]),
    JapaneseWord("です", ["is", "are"]),
    JapaneseWord("でした", ["was", "were"]),
    JapaneseWord("たんじょび", "birthday"),

    JapaneseWord("今日", "today",     ks="きょう"),
    JapaneseWord("明日", "tomorrow",  ks="あした"),
    JapaneseWord("昨日", "yesterday", ks="きのう"),

    JapaneseWord("日曜日", "sunday",    ks="にちようび"),
    JapaneseWord("月曜日", "monday",    ks="げつようび"),
    JapaneseWord("火曜日", "tuesday",   ks="かようび"),
    JapaneseWord("水曜日", "wednesday", ks="すいようび"),
    JapaneseWord("木曜日", "thursday",  ks="もくようび"),
    JapaneseWord("金曜日", "friday",    ks="きんようび"),
    JapaneseWord("土曜日", "saturday",  ks="どようび"),

    JapaneseWord("日", "day", ks="ひ"),
    JapaneseWord("曜", ["day of the week", "day of week"], ks="よ"),

    JapaneseWord("おはよございます。", "good morning"),
    JapaneseWord("こんにちは。", ["good day", "good afternoon"]),
    JapaneseWord("こんばんは。", "good evening"),

    JapaneseWord("名", "name", ks="なまえ"),
    JapaneseWord("お名は？", ["what is your name?", "what's your name?", "whats your name?"]),
    JapaneseWord("はじめまして。", "nice to meet you"),

    JapaneseWord("幸せ", ["happy", "happiness"], ks="しあわせ"),
    JapaneseWord("涙", ["tears", "tear"], ks="なみだ"),

    JapaneseWord("太陽", "sun", ks="たいよ"),
    JapaneseWord("雲", "cloud", ks="くも"),
    JapaneseWord("雨", "rain", ks="あめ"),
    JapaneseWord("雷", "thunder", ks="かみなり"),
    JapaneseWord("霧", "fog", ks="きり"),

    JapaneseWord("救い", ["rescue", "salvation"], ks="すくい"),
    JapaneseWord("憎む", "hate", ks="にくむ"),
    JapaneseWord("夜明け", "dawn", ks="よあけ", desc="aka morning"),

    JapaneseWord("駆け引き", "tactics", ks="かけひき"),
    JapaneseWord("森", ["forest", "woods"], ks="もり"),
    JapaneseWord("狂気", ["madness", "insanity"], ks="きょうき"),
    JapaneseWord("やがて", "eventually"),
    JapaneseWord("襲う", "attack", ks="おそう"), # check "o" or "O" in ks
    JapaneseWord("スマホ", "smartphone"),
    JapaneseWord("月", "moon", ks="つき"),
    JapaneseWord("朝", "morning", ks="あさ"),
    JapaneseWord("朝ご飯", "breakfast", ks="あさごはん"),
    JapaneseWord("朝霧", "morning fog"), # asagiri

    JapaneseWord("犠牲", ["victim", "sacrifice"], ks="ぎせい"),
    JapaneseWord("会話", "conversation", ks="かいわ"),

    #JapaneseWord("", "", ks=""),
]

for japanese_word in JAPANESE_WORDS:
    japanese_word.init_spelling()

