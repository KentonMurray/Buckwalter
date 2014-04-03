Buckwalter
==========

A small python script that transliterates Arabic text using the Buckwalter Transliteration Scheme. It allows for multiple decisions to be made around whether or not to include all types of diacritics and characters or ignore them. Useful for NLP experiments where you may want to normalize text.

usage: buckwalter.py [-h] -corpus CORPUS [-hamza [HAMZA]] [-madda [MADDA]]
                     [-t [T]] [-harakat [HARAKAT]] [-tatweel [TATWEEL]]
                     [-toUTF [TOUTF]]

Converts characters in Arabic free text to integers

optional arguments:
  -h, --help          show this help message and exit
  -corpus CORPUS      Path to the Arabic Corpus
  -hamza [HAMZA]      Include Hamzas as a letter
  -madda [MADDA]      Include Alefs with Madda on top as a separate letter
                      (otherwise just Alef)
  -t [T]              Include Tar Marbuta as a letter
  -harakat [HARAKAT]  Include diacritics as separate letters (otherwise
                      stripped)
  -tatweel [TATWEEL]  Include tatweel as an underscore
  -toUTF [TOUTF]      Take ASCII to Abjad

Note that converting to ASCII to UTF-8 will break if your system settings don't support printing UTF-8 to terminal
