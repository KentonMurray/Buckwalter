##################################################
# Buckwalter Transliteration for python          #
# Follows the general transliteration scheme     #
# except that it allows for multiple decisions   #
# around whether or not to include all types     #
# of characters and diacritics                   #
#                                                #
# Note that this is not XML safe, and may clash  #
# with some punctuation marks (')                #
#                                                #
# Code is provided "as is", without any          #
# warranties or guarantees of any kind, either   #
# expressed or implied.                          #
#                                                #
# Authored by Kenton Murray                      #
# Qatar Computing Research Institute             #
# Doha, Qatar, 2014                              #
##################################################

import argparse
import codecs
import sys

parser = argparse.ArgumentParser(description='Converts characters in Arabic free text to integers')
parser.add_argument('-corpus', type=str, help='Path to the Arabic Corpus', required=True)
parser.add_argument('-hamza', help='Include Hamzas as a letter', default = '', nargs = '?')
parser.add_argument('-madda', help='Include Alefs with Madda on top as a separate letter (otherwise just Alef)', default = '', nargs = '?')
parser.add_argument('-t', help='Include Tar Marbuta as a letter', default = '', nargs='?')
parser.add_argument('-harakat', help='Include diacritics as separate letters (otherwise stripped)', default = '', nargs = '?')
parser.add_argument('-tatweel', help='Include tatweel as an underscore', default = '', nargs = '?')
parser.add_argument('-toUTF', help='Take ASCII to Abjad', default = '', nargs = '?')

args = parser.parse_args()

abjad = {u"\u0627":'A',
u"\u0628":'b', u"\u062A":'t', u"\u062B":'v', u"\u062C":'j',
u"\u062D":'H', u"\u062E":'x', u"\u062F":'d', u"\u0630":'*', u"\u0631":'r',
u"\u0632":'z', u"\u0633":'s', u"\u0634":'$', u"\u0635":'S', u"\u0636":'D',
u"\u0637":'T', u"\u0638":'Z', u"\u0639":'E', u"\u063A":'g', u"\u0641":'f',
u"\u0642":'q', u"\u0643":'k', u"\u0644":'l', u"\u0645":'m', u"\u0646":'n',
u"\u0647":'h', u"\u0648":'w', u"\u0649":'y', u"\u064A":'y'}

# Create the reverse
alphabet = {}
if args.toUTF != '':
  for key in abjad:
    alphabet[abjad[key]] = key

# Tar Mabutta
if args.t != '':
  abjad[u"\u0629"] = 'p'
else:
  abjad[u"\u0629"] = 't' # Some map to Ha ... decide

# Hamza
if args.hamza != '':
  abjad[u"\u0621"] = '\''
  abjad[u"\u0623"] = '>'
  abjad[u"\u0625"] = '<'
  abjad[u"\u0624"] = '&'
  abjad[u"\u0626"] = '}'
  abjad[u"\u0654"] = '\'' # Hamza above
  abjad[u"\u0655"] = '\'' # Hamza below
else:
  abjad[u"\u0621"] = ''
  abjad[u"\u0623"] = 'A'
  abjad[u"\u0625"] = 'A'
  abjad[u"\u0624"] = '' # I don't think that the wa is pronounced otherwise ...
  abjad[u"\u0626"] = '' # Decide ...
  abjad[u"\u0654"] = ''
  abjad[u"\u0655"] = ''

# Alef with Madda on Top
if args.madda != '':
  abjad[u"\u0622"] = '|'
else:
  abjad[u"\u0622"] = 'A'

# Vowels/Diacritics
if args.harakat != '':
  abjad[u"\u064E"] = 'a'
  abjad[u"\u064F"] = 'u'
  abjad[u"\u0650"] = 'i'
  abjad[u"\u0651"] = '~'
  abjad[u"\u0652"] = 'o'
  abjad[u"\u064B"] = 'F'
  abjad[u"\u064C"] = 'N'
  abjad[u"\u064D"] = 'K'
else:
  abjad[u"\u064E"] = ''
  abjad[u"\u064F"] = ''
  abjad[u"\u0650"] = ''
  abjad[u"\u0651"] = ''
  abjad[u"\u0652"] = ''
  abjad[u"\u064B"] = ''
  abjad[u"\u064C"] = ''
  abjad[u"\u064D"] = ''

# Tatweel
if args.tatweel != '':
  abjad[u"\u0640"] = '_'
else:
  abjad[u"\u0640"] = '' 

## Make sure mapping is right
#for key in abjad:
#  print key,
#  print " ",
#  print abjad[key]

if args.toUTF == '':
  with codecs.open(args.corpus, 'r', encoding='utf-8') as f:
    for line in f:
      for char in line:
        if char in abjad:
          sys.stdout.write(abjad[char])
        else:
          # Leaving this in. Run iconv to see if all characters were caught
          sys.stdout.write(char)



# Take Buckwalter Transliterated Text and put it in vernacular
if args.toUTF != '':
  alphabet['|'] = u"\u0622"
  alphabet['a'] = u"\u064E"
  alphabet['u'] = u"\u064F"
  alphabet['i'] = u"\u0650"
  alphabet['~'] = u"\u0651"
  alphabet['o'] = u"\u0652"
  alphabet['F'] = u"\u064B"
  alphabet['N'] = u"\u064C"
  alphabet['K'] = u"\u064D"
  alphabet['\''] = u"\u0621"
  alphabet['>'] = u"\u0623"
  alphabet['<'] = u"\u0625"
  alphabet['&'] = u"\u0624"
  alphabet['}'] = u"\u0626"
  alphabet['p'] = u"\u0629"

  with codecs.open(args.corpus, 'r', encoding='utf-8') as f:
    for line in f:
      for char in line:
        if char in alphabet:
          sys.stdout.write(alphabet[char])
        else:
          sys.stdout.write(char)
