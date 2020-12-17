#(1)
#while True:
#    print('Enter your age:')
#    age = input()
#    try:
#        age = int(age)
#    except:
#        print('Please use numeric digits.')
#        continue
#    if age < 1:
#        print('Please enter a positive number.')
#        continue
#    break
#
#print(f'Your age is {age}.')

#(2)
#import pyinputplus as pyip
#response = pyip.inputNum()

#(3)
#response = input('Enter a number: ')
#import pyinputplus as pyip
#response = pyip.inputInt(prompt='Enter an Integer: ')

#(4)
#we can get help for : inputStr(),inputNum(),inputChoice(),inputMenu(),inputDatetime(),inputYesNo(),inputBool(),inputEmail(),inputFilepath(),inputPassword()
#as following:
#import pyinputplus as pyip
#help(pyip.inputChoice)

#(5)
#The min, max, greaterThan, and lessThan Keyword Arguments
#import pyinputplus as pyip
#response = pyip.inputNum('Enter num min(4): ', min=4)
#response = pyip.inputNum('Enter num greaterThan(4): ', greaterThan=4)
#response = pyip.inputNum('Enter num min=4, lessThan=6: ', min=4, lessThan=6)

#(6)
#By default, blank input isn’t allowed unless the blank keyword argument is set to True:
#import pyinputplus as pyip
#response = pyip.inputNum('Enter num: ')
#response = pyip.inputNum('Enter num blank is allowed: ',blank=True)

#(7)
#The limit, timeout, and default Keyword Arguments
#import pyinputplus as pyip
#response = pyip.inputNum('Enter num : ',limit=2)
#response = pyip.inputNum('Enter num : ',timeout=10)
##Instead of raising RetryLimitException, the inputNum() function simply returns the string 'N/A'
#response = pyip.inputNum('Enter num : ',limit=2, default='N/A')

#(8)
#The allowRegexes and blockRegexes Keyword Arguments
#import pyinputplus as pyip
#response = pyip.inputNum('Enter num : ',allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
#response = pyip.inputNum('Enter num : ',allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])

#(9)
#import pyinputplus as pyip
#response = pyip.inputNum(blockRegexes=[r'[02468]$'])
#print(response)

#(10)
#import pyinputplus as pyip
#response = pyip.inputStr('Enter word: ',allowRegexes=[r'caterpillar', 'category'],blockRegexes=[r'cat'])

#(11)
#Passing a Custom Validation Function to inputCustom()
#import pyinputplus as pyip
#def addsUpToTen(numbers):
#    numbersList = list(numbers)
#    for i, digit in enumerate(numbersList):
#     numbersList[i] = int(digit)
#    if sum(numbersList) != 10:
#     raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
#    return int(numbers) # Return an int form of numbers.
#response = pyip.inputCustom(addsUpToTen)
#addsUpToTen('12345')

#(12)
#Project: How to Keep an Idiot Busy for Hours
#import pyinputplus as pyip
#while True:
#      prompt = 'Want to know how to keep an idiot busy for hours?\n'
#      response = pyip.inputYesNo(prompt)
#      if response == 'no':
#         break
#print('Thank you. Have a nice day.')

#(13)
#Project: Multiplication Quiz
#import pyinputplus as pyip
#import random, time
#numberOfQuestions = 10
#correctAnswers = 0
#for questionNumber in range(numberOfQuestions):
#    # Pick two random numbers:
#    num1 = random.randint(0, 9)
#    num2 = random.randint(0, 9)
#    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
#    try:
#        # Right answers are handled by allowRegexes.
#        # Wrong answers are handled by blockRegexes, with a custom message.
#        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],\
#                              blockRegexes=[('.*', 'Incorrect!')],\
#                              timeout=8, limit=3)
#    except pyip.TimeoutException:
#        print('Out of time!')
#    except pyip.RetryLimitException:
#        print('Out of tries!')
#    else:
#        # This block runs if no exceptions were raised in the try block.
#        print('Correct!')
#        correctAnswers += 1
#    time.sleep(1) # Brief pause to let user see the result.
#    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))