#(1)func
#def hello():
#    print('Howdy!')
#    print('Howdy!!!')
#    print('Hello there.')
#hello()
#hello()
#hello()

#(2)func with parameter
#def hello(name):
#    print('Hello, ' + name)
#hello('Alice')
#hello('Bob')

#(3)
#def sayHello(name):
#       print('Hello, ' + name)
#sayHello('Al')

#(4)
#import random
#def getAnswer(answerNumber):
#    if answerNumber == 1:
#           return 'It is certain'
#    elif answerNumber == 2:
#           return 'It is decidedly so'
#    elif answerNumber == 3:
#           return 'Yes'
#    elif answerNumber == 4:
#           return 'Reply hazy try again'
#    elif answerNumber == 5:
#           return 'Ask again later'
#    elif answerNumber == 6:
#           return 'Concentrate and ask again'
#    elif answerNumber == 7:
#           return 'My reply is no'
#    elif answerNumber == 8:
#           return 'Outlook not so good'
#    elif answerNumber == 9:
#           return 'Very doubtful'
#r = random.randint(1, 9)
#fortune = getAnswer(r)
#print(fortune)

#(5)
#you can set the end keyword argument to change the newline character to a different string
#print('Hello', end='')
#print('World')

#(6)
#when you pass multiple string values to print(), the function will automatically separate them with a single space
#print('cats', 'dogs', 'mice')

#(7)
#you could replace the default separating string by passing the sep keyword argument a different string.
#print('cats', 'dogs', 'mice', sep=',')

#(8)
#def a():
#       print('a() starts')
#       b()
#       d()
#       print('a() returns')
#
#def b():
#       print('b() starts')
#       c()
#       print('b() returns')
#
#def c():
#       print('c() starts')
#       print('c() returns')
#
#def d():
#       print('d() starts')
#       print('d() returns')
#
#a()

#(9)
#Gvar1=8
#def add6(Par):
#    print(str(6+Par))
#add6(Gvar1)

#(10)
#def spam():
#    global eggs
#    eggs = 'spam'
#eggs = 'global'
#spam()
#print(eggs)

#(11)
#eggs = 1
#def spam():
#    global eggs
#    eggs = 'spam' # this is the global
#def bacon():
#    global eggs
#    eggs = 'bacon' # this is the global
#def ham():
#    print(eggs) # this is the global
#print(eggs)
#eggs = 42 # this is the global
#spam()
#bacon()
#print(eggs)

#(12)
#Division by zero error
#def spam(divideBy):
#    return 42 / divideBy
#print(spam(2))
#print(spam(12))
#print(spam(0))
#print(spam(1))

#(13)
#EXCEPTION HANDLING
#Errors can be handled with try and except statements. The code that could potentially have an error is put in a try clause.
#def spam(divideBy):
#    try:
#        return 42 / divideBy
#    except ZeroDivisionError:
#        print('Error: Invalid argument.')
#print(spam(2))
#print(spam(12))
#print(spam(0))
#print(spam(1))

#(14)
#Note that any errors that occur in function calls in a try block will also be caught
#The reason print(spam(1)) is never executed is because once the execution jumps to the code
#in the except clause, it does not return to the try clause. Instead, it just continues moving down
#the program as normal.
#def spam(divideBy):
#    return 42 / divideBy
#try:
#    print(spam(2))
#    print(spam(12))
#    print(spam(0))
#    print(spam(1))
#except ZeroDivisionError:
#    print('Error: Invalid argument.')

#(15)
#Zigzag Program
#def drawzigag(NumLines):
#    NumLines=NumLines+3
#    for i in range(0,int((NumLines-1)/2)-1,1):
#        for j in range(1,int(((NumLines-1)/2))-i,1):
#            print(' ',end='')
#        for k in range (8):
#            print('*',end='')
#        print(' ')
#    for k in range (8):
#        print('*',end='')
#    print(' ')
#    for i in range(int((NumLines-1)/2)-1,0,-1):
#        for j in range(1,int(((NumLines-1)/2))-i+1,1):
#            print(' ',end='')
#        for k in range (8):
#            print('*',end='')
#        print(' ')
#drawzigag(9)

#(16)
#continues Zigzag Program
#import time, sys
#indent = 0 # How many spaces to indent.
#indentIncreasing = True # Whether the indentation is increasing or not.
#try:
#    while True: # The main program loop.
#        print(' ' * indent, end='')
#        print('********')
#        time.sleep(0.1) # Pause for 1/10 of a second.
#        if indentIncreasing:
#            # Increase the number of spaces:
#            indent = indent + 1
#            if indent == 20:
#                # Change direction:
#                indentIncreasing = False
#        else:
#            # Decrease the number of spaces:
#            indent = indent - 1
#            if indent == 0:
#                # Change direction:
#                indentIncreasing = True
#except KeyboardInterrupt:
#    sys.exit()







