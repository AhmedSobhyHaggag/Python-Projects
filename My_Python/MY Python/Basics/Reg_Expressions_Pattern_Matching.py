#(1)
#Finding Patterns of Text Without Regular Expressions
#a function named isPhoneNumber() to check whether a string matches this pattern, returning either True or False
#def isPhoneNumber(text):
#    if len(text) != 12:
#         return False
#    for i in range(0, 3):
#       if not text[i].isdecimal():
#             return False
#    if text[3] != '-':
#         return False
#    for i in range(4, 7):
#       if not text[i].isdecimal():
#             return False
#    if text[7] != '-':
#         return False
#    for i in range(8, 12):
#       if not text[i].isdecimal():
#             return False
#    return True
#print('Is 415-555-4242 a phone number?')
#print(isPhoneNumber('415-555-4242'))
#print('Is Moshi moshi a phone number?')
#print(isPhoneNumber('Moshi moshi'))
#message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
#for i in range(len(message)):
#    chunk = message[i:i+12]
#    if isPhoneNumber(chunk):
#       print('Phone number found: ' + chunk)
#print('Done')

#(2)
#Finding Patterns of Text with Regular Expressions
#Creating Regex Objects
#Matching Regex Objects
#import re
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: ' + mo.group())
#More Pattern Matching with Regular Expressions
#Grouping with Parentheses
#import re
#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My number is 415-555-4242.')
#print(mo.group(1))
#print(mo.group(2))
#print(mo.group(0))
#print(mo.group())
#print(mo.groups())
#areaCode, mainNumber = mo.groups()
#print(areaCode)
#print(mainNumber)
#if you need to match a parenthesis in your text
#import re
#phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
#print(mo.group(1))
#print(mo.group(2))
#Matching Multiple Groups with the Pipe
#import re
#heroRegex = re.compile (r'Batman|Tina Fey')
#mo1 = heroRegex.search('Batman and Tina Fey')
#print(mo1.group())
#mo2 = heroRegex.search('Tina Fey and Batman')
#print(mo2.group())
#import re
#batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#mo = batRegex.search('Batmobile lost a wheel')
#print(mo.group())
#print(mo.group(1))
#print(mo.groups())
#Optional Matching with the Question Mark
#import re
#batRegex = re.compile(r'Bat(wo)?man')
#mo1 = batRegex.search('The Adventures of Batman')
#print(mo1.group())
#mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())
#import re
#phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
#mo1 = phoneRegex.search('My number is 415-555-4242')
#print(mo1.group())
#mo2 = phoneRegex.search('My number is 555-4242')
#print(mo2.group())
#Matching Zero or More with the Star
#import re
#batRegex = re.compile(r'Bat(wo)*man')
#mo1 = batRegex.search('The Adventures of Batman')
#print(mo1.group())
#mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())
#mo3 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo3.group())
#Matching One or More with the Plus
#import re
#batRegex = re.compile(r'Bat(wo)+man')
#mo1 = batRegex.search('The Adventures of Batwoman')
#print(mo1.group())
#mo2 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo2.group())
#mo3 = batRegex.search('The Adventures of Batman')
#print(mo3 == None)
#print(mo3.group())
#Matching Specific Repetitions with Braces
#import re
#haRegex = re.compile(r'(Ha){3}')
#mo1 = haRegex.search('HaHaHa')
#print(mo1.group())
#mo2 = haRegex.search('Ha')
#print(mo2 == None)
#Greedy and Non-greedy Matching
#import re
#greedyHaRegex = re.compile(r'(Ha){3,5}')
#mo1 = greedyHaRegex.search('HaHaHaHaHa')
#print(mo1.group())
#nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
#mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
#print(mo2.group())
#The findall() Method
#import re
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
#print(mo.group())
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
#print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
#print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#Character Classes
#import re
#xmasRegex = re.compile(r'\d+\s\w+')
#collection=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
#swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
#print(collection)

#Making Your Own Character Classes
#For example, the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase
#import re
#vowelRegex = re.compile(r'[aeiouAEIOU]')
#print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
#By placing a caret character (^) just after the character class’s opening bracket,
#you can make a negative character class.
#A negative character class will match all the characters that are not in the character class
#import re
#consonantRegex = re.compile(r'[^aeiouAEIOU]')
#print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#The Caret(^) and Dollar Sign Characters($)
#import re
#beginsWithHello = re.compile(r'^Hello')
#print(beginsWithHello.search('Hello, world!'))
#print(beginsWithHello.search('He said hello.'))
#endsWithNumber = re.compile(r'\d$')
#print(endsWithNumber.search('Your number is 42'))
#print(endsWithNumber.search('Your number is forty two.'))
#wholeStringIsNum = re.compile(r'^\d+$')
#print(wholeStringIsNum.search('1234567890'))
#print(wholeStringIsNum.search('12345xyz67890'))
#print(wholeStringIsNum.search('12  34567890'))

#The Wildcard Character(Dot . )
#import re
#atRegex = re.compile(r'.at')
#print(atRegex.findall('The cat in the hat sat on the flat mat.'))

#Matching Everything with Dot-Star
#import re
#nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#mo = nameRegex.search('First Name: Al Last Name: Sweigart')
#print(mo.group(1))
#print(mo.group(2))
#nongreedyRegex = re.compile(r'<.*?>')
#mo = nongreedyRegex.search('<To serve man> for dinner.>')
#print(mo.group())
#greedyRegex = re.compile(r'<.*>')
#mo = greedyRegex.search('<To serve man> for dinner.>')
#print(mo.group())

#Matching Newlines with the Dot Character
#import re
#noNewlineRegex = re.compile('.*')
#print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
#print(noNewlineRegex.search('Serve the public trust.\\nProtect the innocent.\\nUphold the law.').group())
#newlineRegex = re.compile('.*', re.DOTALL)
#print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

#Case-Insensitive Matching
#import re
#robocop = re.compile(r'robocop', re.I)
#print(robocop.search('RoboCop is part man, part machine, all cop.').group())
#print(robocop.search('ROBOCOP protects the innocent.').group())
#print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

#Substituting Strings with the sub() Method
#import re
#namesRegex = re.compile(r'Agent \w+')
#print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
#agentNamesRegex = re.compile(r'Agent (\w)\w*')
#print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
#Eve knew Agent Bob was a double agent.'))

#Managing Complex Regexes
#someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

#(3)
#Project: Phone Number and Email Address Extractor
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
#import pyperclip, re
#phoneRegex = re.compile(r'''(
#    (\d{3}|\(\d{3}\))?                # area code
#    (\s|-|\.)?                        # separator
#    (\d{3})                           # first 3 digits
#    (\s|-|\.)                         # separator
#    (\d{4})                           # last 4 digits
#    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
#    )''', re.VERBOSE)
## Create email regex.
#emailRegex = re.compile(r'''(
#    [a-zA-Z0-9._%+-]+      # username
#    @                      # @ symbol
#    [a-zA-Z0-9.-]+         # domain name
#    (\.[a-zA-Z]{2,4})       # dot-something
#    )''', re.VERBOSE)
##Find matches in clipboard text.
#text = str(pyperclip.paste())
#matches = []
#for groups in phoneRegex.findall(text):
#       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
#       if groups[8] != '':
#           phoneNum += ' x' + groups[8]
#       matches.append(phoneNum)
#for groups in emailRegex.findall(text):
#       matches.append(groups[0])
#for groups in emailRegex.findall(text):
#    matches.append(groups[0])
## Copy results to the clipboard.
#if len(matches) > 0:
#    pyperclip.copy('\n'.join(matches))
#    print('Copied to clipboard:')
#    print('\n'.join(matches))
#else:
#    print('No phone numbers or email addresses found.')