#(1)
#double qoutes
#print("That is Alice's cat.")
#Escape Characters
#print( 'Say hi to Bob\'s mother.')
#print("Hello there!\nHow are you?\nI\'m doing fine.")
#Raw Strings
#print(r'That is Carol\'s cat.')
#Multiline Strings with Triple Quotes
#print('''Dear Alice,
#
#Eve's cat has been arrested for catnapping, cat burglary, and extortion.
#
#Sincerely,
#Bob''')
#Multiline Comments
#"""This is a test Python program.
#Written by Al Sweigart al@inventwithpython.com
#
#This program was designed for Python 3, not Python 2.
#"""
#def spam():
#    """This is a multiline comment to help
#    explain what the spam() function does."""
#    print('Hello!')
#Indexing and Slicing Strings
#spam='Hello,world!'
#print(spam[0])
#print(spam[4])
#print(spam[-1])
#print(spam[0:5])
#print(spam[:5])
#print(spam[7])
#print(spam[7:])
#The in and not in Operators with Strings
#print('Hello' in 'Hello, World')
#print('Hello' in 'Hello')
#print('HELLO' in 'Hello, World')
#print('' in 'spam')
#print('cats' not in 'cats and dogs')
#Putting Strings Inside Other Strings
#name = 'Al'
#age = 4000
#print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')
#name = 'Al'
#age = 4000
#print('My name is %s. I am %s years old.' % (name, age))
#name = 'Al'
#age = 4000
#print(f'My name is {name}. Next year I will be {age + 1}.')
#Useful String Methods
#The upper(), lower(), isupper(), and islower() Methods
#The upper(), lower(), isupper(), and islower() Methods
#spam = 'Hello, world!'
#spam = spam.upper()
#print(spam)
#spam = spam.lower()
#print(spam)
#spam = 'Hello, world!'
#print(spam.islower())
#print(spam.isupper())
#print('HELLO'.isupper())
#print('abc12345'.islower())
#print('12345'.islower())
#print('12345'.isupper())
#The isX() Methods
#print('hello'.isalpha())
#print('hello123'.isalpha())
#print('hello123'.isalnum())
#print('hello'.isalnum())
#print('123'.isdecimal())
#print('    '.isspace())
#print('This Is Title Case'.istitle())
#print('This Is Title Case 123'.istitle())
#print('This Is not Title Case'.istitle())
#print('This Is NOT Title Case Either'.istitle())
#validateInput.py
#while True:
#    print('Enter your age:')
#    age = input()
#    if age.isdecimal():
#        break
#    print('Please enter a number for your age.')
#
#while True:
#    print('Select a new password (letters and numbers only):')
#    password = input()
#    if password.isalnum():
#        break
#    print('Passwords can only have letters and numbers.')a
#The startswith() and endswith() Methods
#print('Hello, world!'.startswith('Hello'))
#print('Hello, world!'.endswith('world!'))
#print('abc123'.startswith('abcdef'))
#print('abc123'.endswith('12'))
#print('Hello, world!'.startswith('Hello, world!'))
#print('Hello, world!'.endswith('Hello, world!'))
#The join() and split() Methods
#print(', '.join(['cats', 'rats', 'bats']))
#print(' '.join(['My', 'name', 'is', 'Simon']))
#print('ABC'.join(['My', 'name', 'is', 'Simon']))
#print('My name is Simon'.split())
#print('MyABCnameABCisABCSimon'.split('ABC'))
#print('My name is Simon'.split('m'))
#spam = '''Dear Alice,
#How have you been? I am fine.
#There is a container in the fridge
#that is labeled "Milk Experiment."
#
#Please do not drink it.
#Sincerely,
#Bob'''
#print(spam.split('\n'))
#Splitting Strings with the partition() Method
#print('Hello, world!'.partition('w'))
#print('Hello, world!'.partition('world'))
#print('Hello, world!'.partition('o'))
#print('Hello, world!'.partition('XYZ'))
#before, sep, after = 'Hello, world!'.partition(' ')
#print(before)
#print(sep)
#print(after)
#Justifying Text with the rjust(), ljust(), and center() Methods
#print('Hello'.rjust(10))
#print('Hello'.rjust(20))
#print('Hello, World'.rjust(20))
#print('Hello'.ljust(10)+'Ahmed')
#print( 'Hello'.rjust(20, '*'))
#print('Hello'.ljust(20, '-'))
#print('Hello'.center(20))
#print('Hello'.center(20, '='))
#picnicTable.py
#def printPicnic(itemsDict, leftWidth, rightWidth):
#    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#    for k, v in itemsDict.items():
#        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
#printPicnic(picnicItems, 12, 5)
#printPicnic(picnicItems, 20, 6)
#Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
#spam = '    Hello, World    '
#print(spam.strip())
#print(spam.lstrip())
#print(spam.rstrip())
#spam = 'SpamSpamBaconSpamEggsSpamSpam'
#print(spam.strip('ampS'))
#Numeric Values of Characters with the ord() and chr() Functions
#print(ord('A'))
#print(ord('4'))
#print(ord('!'))
#print(chr(65))
#print(ord('B'))
#print(ord('A') < ord('B'))
#print(chr(ord('A')))
#print(chr(ord('A') + 1))

#(2)
#Copying and Pasting Strings with the pyperclip Module
#import pyperclip
#pyperclip.copy('Hello, world!')
#print(pyperclip.paste())

#(3)
#Project: Multi-Clipboard Automatic Messages
#Path for the patch file which runs this script: C:\Users\Ahmed.Sobhy\AppData\Local\Programs\Python\Python38\Scripts
#! python3
# mclip.py - A multi-clipboard program.
#TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
#        'busy': """Sorry, can we do this later this week or next week?""",
#        'upsell': """Would you consider making this a monthly donation?"""}
#import sys, pyperclip
#if len(sys.argv) < 2:
#    print('Usage: py mclip.py [keyphrase] - copy phrase text')
#    sys.exit()
#keyphrase = sys.argv[1]    # first command line arg is the keyphrase
#if keyphrase in TEXT:
#    pyperclip.copy(TEXT[keyphrase])
#    print('Text for ' + keyphrase + ' copied to clipboard.')
#else:
#    print('There is no text for ' + keyphrase)

#(4)
#Project: Adding Bullets to Wiki Markup
#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
#import pyperclip
#text = pyperclip.paste()
# Separate lines and add stars.
#lines = text.split('\n')
#for i in range(len(lines)):    # loop through all indexes for "lines" list
#    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
#text = '\n'.join(lines)
#pyperclip.copy(text)

#(5)
#A Short Progam: Pig Latin
# English to Pig Latin
#print('Enter the English message to translate into Pig Latin:')
#message = input()
#VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
#pigLatin = [] # A list of the words in Pig Latin.
#for word in message.split():
#    # Separate the non-letters at the start of this word:
#    prefixNonLetters = ''
#    while len(word) > 0 and not word[0].isalpha():
#        prefixNonLetters += word[0]
#        word = word[1:]
#    if len(word) == 0:
#        pigLatin.append(prefixNonLetters)
#        continue
#    # Separate the non-letters at the end of this word:
#    suffixNonLetters = ''
#    while not word[-1].isalpha():
#        suffixNonLetters += word[-1]
#        word = word[:-1]
#    # Remember if the word was in uppercase or title case.
#    wasUpper = word.isupper()
#    wasTitle = word.istitle()
#    word = word.lower() # Make the word lowercase for translation.
#    # Separate the consonants at the start of this word:
#    prefixConsonants = ''
#    while len(word) > 0 and not word[0] in VOWELS:
#        prefixConsonants += word[0]
#        word = word[1:]
#    # Add the Pig Latin ending to the word:
#    if prefixConsonants != '':
#        word += prefixConsonants + 'ay'
#    else:
#        word += 'yay'
#    # Set the word back to uppercase or title case:
#    if wasUpper:
#        word = word.upper()
#    if wasTitle:
#        word = word.title()
#    # Add the non-letters back to the start or end of the word.
#    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
## Join all the words back together into a single string:
#print(' '.join(pigLatin))