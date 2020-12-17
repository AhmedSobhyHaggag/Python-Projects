#DICTIONARIES AND STRUCTURING DATA
#(1)
#myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
#This dictionary’s keys are 'size', 'color', and 'disposition'.
#The values for these keys are 'fat', 'gray', and 'loud', respectively.
#print(myCat['size'])

#(2)
#birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
#while True:
#      print('Enter a name: (blank to quit)')
#      name = input()
#      if name == '':
#         break
#      if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#      else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')
#         print(birthdays)

#(3)
#spam = {'color': 'red', 'age': 42}
#for v in spam.values():
#    print(v)
#for k in spam.keys():
#    print(k)
#for i in spam.items():
#    print(i)
#print(list(spam.values()))
#print(list(spam.keys()))
#print(list(spam.items()))
#spam = {'color': 'red', 'age': 42}
#for k, v in spam.items():
#    print('Key: ' + k + ' Value: ' + str(v))

#(4)
#spam = {'name': 'Zophie', 'age': 7}
#print('name' in spam.keys())
#print('Zophie' in spam.values())
#print('color' in spam.keys())
#print('color' not in spam.keys())
#print('color' in spam)
#print('age' in spam) #we can use spam instead of only spam.keys()
#print('Zophie' in spam)

#(5)
#picnicItems = {'apples': 5, 'cups': 2}
#print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
#print('I am bringing ' + str(picnicItems.get('eggs', 0))) + ' eggs.')
# 0 is the default value returned if eggs doesn't exist in the dictionary

#(6)
#spam = {'name': 'Pooka', 'age': 5}
#print(spam.setdefault('color', 'black'))
#print(spam)
#print(spam.setdefault('color', 'white'))
#print(spam)
#spam['name']='white'
#print(spam)

#(7)
#message = 'It was a bright cold day in April, and the clocks were striking \
#thirteen.'
#count = {}
#for character in message:
#    count.setdefault(character, 0)
#    count[character] = count[character] + 1
#print(count)

#(8)
#import pprint
#message = 'It was a bright cold day in April, and the clocks were striking \
#thirteen.'
#count = {}
#for character in message:
#    count.setdefault(character, 0)
#    count[character] = count[character] + 1
#pprint.pprint(count)
#print(pprint.pformat(count))

#(9)
#theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#def printBoard(board):
#    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#    print('-+-+-')
#    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#    print('-+-+-')
#    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#printBoard(theBoard)

#(10)
#allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#             'Bob': {'ham sandwiches': 3, 'apples': 2},
#             'Carol': {'cups': 3, 'apple pies': 1}}
#def totalBrought(guests, item):
#    numBrought = 0
#    for k, v in guests.items():
#       numBrought = numBrought + v.get(item, 0)
#    return numBrought
#print('Number of things being brought:')
#print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
#print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
#print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
#print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
#print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))






