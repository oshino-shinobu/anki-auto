Anki-auto
=========

Scripts, minimizing the time needed to add cards to Anki
--------------------------------------------------------
saveword.py writes the currently selected word to ./Purgatory

genkanji.py takes all kanji that appear in ./Words and generates ./KanjiForImport

How to use it
-------------
Configure it:
* bind shortcut Ctrl+something to call 'python YOURDIR/anki-auto/saveword.py'
* install addons: Rikaisama in Firefox and [kanji_colorizer](https://ankiweb.net/shared/info/1964372878) in Anki
* configure Rikaisama to save words in YOURDIR/anki-auto/Words
* create deck for words that corresponds to the format you use in Rikaisama
  * I use `$d$t$r$t$n$t[sound:$a]` as the format in Rikaisama and
  * Japanese (recognition&recall) from [Japanese Support](https://ankiweb.net/shared/info/3918629684)
* download [RTK1+JLPT+Joyo kanji w/ radical decomposition, word lists](https://ankiweb.net/shared/info/2109757073) deck, so that you have the correct 'Options Group'
* create deck for kanji with the Options Group as in the above deck

Use it:
* open ./Purgatory via Firefox and manually save the words (by pressing S on each word) in ./Words via Rikaisama
* run `python genkanji.py`
* import words from ./Words and kanji from ./KanjiForImport
* generate diagrams for kanji via kanji_colorizer

Pretty easy, right?

I wonder if there is a way to make Rikaisama save all words from Purgatory automatically.

P.S. Don't waste your time with Heisig.
Just learn words (preferably in context, e.g. via Core 6000) and kanji that appear in these words simultaneously.

Note also, that you can take any file that contains kanji, rename it to Words, and generate kanji for import. This might be handy.
