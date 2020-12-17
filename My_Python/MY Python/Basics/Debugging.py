#(1)
#Raising Exceptions
#raise Exception('This is the error message.')

#(2)
#def boxPrint(symbol, width, height):
#    if len(symbol) != 1:
#       raise Exception('Symbol must be a single character string.')
#    if width <= 2:
#       raise Exception('Width must be greater than 2.')
#    if height <= 2:
#       raise Exception('Height must be greater than 2.')
#    print(symbol * width)
#    for i in range(height - 2):
#        print(symbol + (' ' * (width - 2)) + symbol)
#    print(symbol * width)
#for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#    try:
#        boxPrint(sym, w, h)
#    except Exception as err:
#        print('An exception happened: ' + str(err))

#(3)
#Getting the Traceback as a String
#def spam():
#    bacon()
#def bacon():
#    raise Exception('This is the error message.')
#spam()

#(4)
#import traceback
#try:
#    raise Exception('This is the error message.')
#except:
#        errorFile = open('errorInfo.txt', 'w')
#        Nc=errorFile.write(traceback.format_exc())
#        errorFile.close()
#        print('The traceback info was written to errorInfo.txt.')

#(5)
#Assertions
#ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
#ages.sort()
#print(ages)
#assert ages[0] <= ages[-1] # Assert that the first age is <= the last age
#ages.reverse()
#print(ages)
#assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

#Note:If you run a Python script with python -O myscript.py instead of python myscript.py, Python will skip assert statements.

#(6)
#Using an Assertion in a Traffic Light Simulation
#market_2nd = {'ns': 'green', 'ew': 'red'}
#mission_16th = {'ns': 'red', 'ew': 'green'}
#def switchLights(stoplight):
#    for key in stoplight.keys():
#        if stoplight[key] == 'green':
#            stoplight[key] = 'yellow'
#        elif stoplight[key] == 'yellow':
#            stoplight[key] = 'red'
#        elif stoplight[key] == 'red':
#            stoplight[key] = 'green'
#switchLights(market_2nd)
#print(market_2nd)

#With assertion
#market_2nd = {'ns': 'green', 'ew': 'red'}
#mission_16th = {'ns': 'red', 'ew': 'green'}
#def switchLights(stoplight):
#    for key in stoplight.keys():
#        if stoplight[key] == 'green':
#            stoplight[key] = 'yellow'
#        elif stoplight[key] == 'yellow':
#            stoplight[key] = 'red'
#        elif stoplight[key] == 'red':
#            stoplight[key] = 'green'
#    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
#switchLights(market_2nd)
#print(market_2nd)

#(7)
#Logging
#Using the logging Module
#import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')
#logging.debug('Start of program')
#def factorial(n):
#    logging.debug('Start of factorial(%s%%)'  % (n))
#    total = 1
#    for i in range(n + 1):
#        total *= i
#        logging.debug('i is ' + str(i) + ', total is ' + str(total))
#    logging.debug('End of factorial(%s%%)'  % (n))
#    return total
#print(factorial(5))
#logging.debug('End of program')

#(8)
#Logging Levels
#import logging
#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s -  %(message)s')
#logging.debug('Some debugging details.')
#logging.info('The logging module is working.')
#logging.warning('An error message is about to be logged.')
#logging.error('An error has occurred.')
#logging.critical('The program is unable to recover!')

#(9)
#Disabling Logging
#import logging
#logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s -  %(message)s')
#logging.critical('Critical error! Critical error!')
#logging.disable(logging.CRITICAL)
#logging.critical('Critical error! Critical error!')
#logging.error('Error! Error!')

#(10)
#Logging to a File
#import logging
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
#logging.debug('Start of program')
#def factorial(n):
#    logging.debug('Start of factorial(%s%%)'  % (n))
#    total = 1
#    for i in range(n + 1):
#        total *= i
#        logging.debug('i is ' + str(i) + ', total is ' + str(total))
#    logging.debug('End of factorial(%s%%)'  % (n))
#    return total
#print(factorial(5))
#logging.debug('End of program')

#(11)
#Mu’s Debugger
#Debugging a Number Adding Program
#print('Enter the first number to add:')
#first = input()
#print('Enter the second number to add:')
#second = input()
#print('Enter the third number to add:')
#third = input()
#print('The sum is ' + first + second + third)

#(12)
#
#import random
#heads = 0
#for i in range(1, 1001):
#    if random.randint(0, 1) == 1:
#         heads = heads + 1
#    if i == 500:
#        print('Halfway done!')
#print('Heads came up ' + str(heads) + ' times.')