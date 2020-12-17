#(1)
#printing list contents
#def printspamlist(list):
#    for i in range (0,4,1):
#        print(list[i])
#spam = ['cat', 'bat', 'rat', 'elephant']
#printspamlist(spam)
#print(spam[0:2])
#print(spam[0:-1])
#print(spam[:2])
#print(spam[1:])
#print(spam[:])
#print(len(spam))
#spam[1] = 'aardvark'
#print(spam[1])
#spam[2] = spam[1]
#printspamlist(spam)
#spam[-1] = 12345
#printspamlist(spam)

#(2)
#list of lists
#spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
#print(spam[0])
#print(spam[-1])
#print(spam[-2])
#print(spam[1])
#print(spam[0][1])
#print(spam[1][1])

#(3)
#list concatenation and replication
#print([1, 2, 3] + ['A', 'B', 'C'])
#print(['X', 'Y', 'Z'] * 3)
#spam = [1, 2, 3]
#spam = spam + ['A', 'B', 'C']
#print(spam)
#spam = ['cat', 'bat', 'rat', 'elephant']
#del spam[2] #del can also be used to delete variables
#print(spam)

#(4)
#a single list and can store any number of cats that the user types in
#catNames = []
#while True:
#    print('Enter the name of cat ' + str(len(catNames) + 1) +
#      ' (Or enter nothing to stop.):')
#    name = input()
#    if name == '':
#        break
#    catNames = catNames + [name]  # list concatenation
#print('The cat names are:')
#for name in catNames:
#    print('  ' + name)

#(5)
#printing sequence in alist
#for i in [1,2,3,4]:
#    print(i)

#(6)
#supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
#for i in range(len(supplies)):
#    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#(7)
#You can determine whether a value is or isn’t in a list with the in and not in operators
#print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
#spam = ['hello', 'hi', 'howdy', 'heyas']
#print('howdy' not in spam)

#(8)
#myPets = ['Zophie', 'Pooka', 'Fat-tail']
#print('Enter a pet name:')
#name = input()
#if name not in myPets:
#    print('I do not have a pet named ' + name)
#else:
#    print(name + ' is my pet.')

#(9)
#The Multiple Assignment Trick
#The number of variables and the length of the list must be exactly equal,
#or Python will give you a ValueError
#cat = ['fat', 'gray', 'loud']
#size, color, disposition = cat
#print(size)
#print(color)
#print(disposition)

#(10)
#Using the enumerate() Function with Lists
#supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
#for index, item in enumerate(supplies):
#    print('Index ' + str(index) + ' in supplies is: ' + item)

#(11)
#Using the random.choice() and random.shuffle() Functions with Lists
#import random
#pets = ['Dog', 'Cat', 'Moose']
##print(random.choice(pets))
##The random.shuffle() function will reorder the items in a list.
#people=['Alice', 'Bob', 'Carol', 'David']
#random.shuffle(people)
#print(people)

#(12)
#spam = 'Hello,'
#spam += ' world!'
#print(spam)
#bacon = ['Zophie']
#bacon *= 3
#print(bacon)

#(13)
#Methods
#Finding a Value in a List with the index() Method
#spam = ['hello', 'hi', 'howdy', 'heyas']
#print(spam.index('hello'))
#When there are duplicates of the value in the list, the index of its first appearance is returned
#spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
#print(spam.index('Pooka'))
#Adding Values to Lists with the append() and insert() Methods
#spam = ['cat', 'dog', 'bat']
#append() method call adds the argument to the end of the list
#spam.append('moose')
#print(spam)
#The insert() method can insert a value at any index in the list.
#The first argument to insert() is the index for the new value,
#and the second argument is the new value to be inserted
#spam.insert(1, 'chicken')
#print(spam)
#Removing Values from Lists with the remove() Method
#If the value appears multiple times in the list,
#only the first instance of the value will be removed
#spam = ['cat', 'bat', 'rat', 'elephant']
#spam.remove('bat') #=del spam[1]
#print(spam)
#Sorting the Values in a List with the sort() Method
#spam = [2, 5, 3.14, 1, -7]
#spam.sort()
#print(spam)
#spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
#spam.sort()
#print(spam)
#You can also pass True for the reverse keyword argument
#to have sort() sort the values in reverse order
#spam.sort(reverse=True)
#print(spam)
#sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings.
#This means uppercase letters come before lowercase letters
#spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
#spam.sort()
#print(spam)
#If you need to sort the values in regular alphabetical order,
#pass str.lower for the key keyword argument in the sort() method call
#spam.sort(key=str.lower)
#print(spam)
#Reversing the Values in a List with the reverse() Method
#spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
#spam.reverse()
#print(spam)

#(14)
#import random
#messages = ['It is certain',
#    'It is decidedly so',
#    'Yes definitely',
#    'Reply hazy try again',
#    'Ask again later',
#    'Concentrate and ask again',
#    'My reply is no',
#    'Outlook not so good',
#    'Very doubtful']
#print(messages[random.randint(0, len(messages) - 1)])

#(15)
#SEQUENCE DATA TYPES(data types similar to lists)
#name = 'Zophie'
#print('Zo' in name)
#print('z' in name)
#print('p' not in name)
#for i in name:
#     print('* * * ' + i + ' * * *')

#(16)
#The Tuple Data Type(immutable form of the list data type)
#you can indicate this by placing a trailing comma
#after the value inside the parentheses.
#Otherwise, Python will think you’ve just typed a value inside regular parentheses.
#The comma is what lets Python know this is a tuple value
#print(type(('hello',)))
#print(type(('hello')))

#(17)
#Type conversion
#print(tuple(['cat', 'dog', 5]))
#print(list(('cat', 'dog', 5)))
#print(list('hello'))

#(18)
#Referencing
#spam = [0, 1, 2, 3, 4, 5]
#cheese = spam # The reference is being copied, not the list.
#cheese[1] = 'Hello!' # This changes the list value.
#print(spam)
#print(cheese) # The cheese variable refers to the same list.
#Identity and the id() Function
#print(id('Howdy') ) #address stored at
#eggs = ['cat', 'dog']
#print(id(eggs))
#eggs.append('moose')
#print(id(eggs))
#eggs.insert(0,'egg')
#print(id(eggs))

#(19)
#The copy Module’s copy() and deepcopy() Functions
#import copy
#spam = ['A', 'B', 'C', 'D']
#print(id(spam))
#cheese = copy.copy(spam)
#print(id(cheese)) # cheese is a different list with different identity.
#cheese[1] = 42
#print(spam)
#print(cheese)
#If the list you need to copy contains lists,
#then use the copy.deepcopy() function instead of copy.copy().

#(20)
# Conway's Game of Life
#import random, time, copy
#WIDTH = 60
#HEIGHT = 20
#
## Create a list of list for the cells:
#nextCells = []
#for x in range(WIDTH):
#    column = [] # Create a new column.
#    for y in range(HEIGHT):
#        if random.randint(0, 1) == 0:
#            column.append('#') # Add a living cell.
#        else:
#            column.append(' ') # Add a dead cell.
#    nextCells.append(column) # nextCells is a list of column lists.
#
#while True: # Main program loop.
#    print('\n\n\n\n\n') # Separate each step with newlines.
#    currentCells = copy.deepcopy(nextCells)
#
#    # Print currentCells on the screen:
#    for y in range(HEIGHT):
#        for x in range(WIDTH):
#            print(currentCells[x][y], end='') # Print the # or space.
#        print() # Print a newline at the end of the row.
#
#    # Calculate the next step's cells based on current step's cells:
#    for x in range(WIDTH):
#        for y in range(HEIGHT):
#            # Get neighboring coordinates:
#            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
#            leftCoord  = (x - 1) % WIDTH
#            rightCoord = (x + 1) % WIDTH
#            aboveCoord = (y - 1) % HEIGHT
#            belowCoord = (y + 1) % HEIGHT
#
#            # Count number of living neighbors:
#            numNeighbors = 0
#            if currentCells[leftCoord][aboveCoord] == '#':
#                numNeighbors += 1 # Top-left neighbor is alive.
#            if currentCells[x][aboveCoord] == '#':
#                numNeighbors += 1 # Top neighbor is alive.
#            if currentCells[rightCoord][aboveCoord] == '#':
#                numNeighbors += 1 # Top-right neighbor is alive.
#            if currentCells[leftCoord][y] == '#':
#                numNeighbors += 1 # Left neighbor is alive.
#            if currentCells[rightCoord][y] == '#':
#                numNeighbors += 1 # Right neighbor is alive.
#            if currentCells[leftCoord][belowCoord] == '#':
#                numNeighbors += 1 # Bottom-left neighbor is alive.
#            if currentCells[x][belowCoord] == '#':
#                numNeighbors += 1 # Bottom neighbor is alive.
#            if currentCells[rightCoord][belowCoord] == '#':
#                numNeighbors += 1 # Bottom-right neighbor is alive.
#
#            # Set cell based on Conway's Game of Life rules:
#            if currentCells[x][y] == '#' and (numNeighbors == 2 or
#numNeighbors == 3):
#                # Living cells with 2 or 3 neighbors stay alive:
#                nextCells[x][y] = '#'
#            elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                # Dead cells with 3 neighbors become alive:
#                nextCells[x][y] = '#'
#            else:
#                # Everything else dies or stays dead:
#                nextCells[x][y] = ' '
#    time.sleep(1) # Add a 1-second pause to reduce flickering






