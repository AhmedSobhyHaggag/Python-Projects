#(1)
#Path Separator:Backslash on Windows and Forward Slash on macOS and Linux
#from pathlib import Path
#print(Path('spam', 'bacon', 'eggs'))
#print(str(Path('spam', 'bacon', 'eggs')))

#(2)
#from pathlib import Path
#myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
#for filename in myFiles:
#    print(Path(r'C:\Users\Al', filename))

#(3)
#Using the / Operator to Join Paths
#from pathlib import Path
#path1=Path('spam') / 'bacon' / 'eggs' #if used in the shell output will be WindowsPath('spam/bacon/eggs')
#print(path1)
#path2=Path('spam') / Path('bacon/eggs') #if used in the shell output will be WindowsPath('spam/bacon/eggs')
#print(path2)
#path3=Path('spam') / Path('bacon', 'eggs') #if used in the shell output will be WindowsPath('spam/bacon/eggs')
#print(path3)

#(4)
#from pathlib import Path
#homeFolder = r'C:\Users\Al'
#subFolder = 'spam'
#print(homeFolder + '\\' + subFolder) #if used in the shell output will be'C:\\Users\\Al\\spam
#print('\\'.join([homeFolder, subFolder])) #if used in the shell output will be'C:\\Users\\Al\\spam

#(5)
#from pathlib import Path
#homeFolder = Path('C:/Users/Al')
#subFolder = Path('spam')
#print(homeFolder / subFolder)  #if used in the shell output will be WindowsPath('C:/Users/Al/spam')

#(6)
#The Current Working Directory
#from pathlib import Path
#import os
#print(Path.cwd())
#os.chdir('C:\\Windows\\System32')
#print(Path.cwd())

#(7)
#The Home Directory
#from pathlib import Path
#print(Path.home())

#(8)
#Creating New Folders Using the os.makedirs() Function
#import os
#this will create the directory waffles in this directory(CWD) we could also give it the absolute path
#os.makedirs('.\\waffles')
#Another way
#from pathlib import Path
#Path(r'.\spam').mkdir()

#(9)
#Handling Absolute and Relative Paths
#from pathlib import Path
#print(Path.cwd())
#print(Path.cwd().is_absolute())
#print(Path('spam/bacon/eggs').is_absolute())
#print(Path('my/relative/path'))
#print(Path.cwd() / Path('my/relative/path'))
#print(Path.home() / Path('my/relative/path'))

#(10)
#import os
#print(os.path.abspath('.'))
#print(os.path.abspath('.\\Scripts'))
#print(os.path.isabs('.'))
#print(os.path.isabs(os.path.abspath('.')))
#print(os.path.relpath('C:\\Windows', 'C:\\'))
#print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

#(11)
#Getting the Parts of a File Path
#from pathlib import Path
#p=Path('C:/Users/Al/spam.txt')
#print(p.anchor)
#print(p.parent) # This is a Path object, not a string.
#print(p.name)
#print(p.stem)
#print(p.suffix)
#print(p.drive)
#print(Path.cwd())
#print(Path.cwd().parents[0])
#print(Path.cwd().parents[1])
#print(Path.cwd().parents[2])
#print(Path.cwd().parents[3])
#print(Path.cwd().parents[4])
#import os
#calcFilePath = 'C:\\Windows\\System32\\calc.exe'
#print(os.path.basename(calcFilePath))
#print(os.path.dirname(calcFilePath))
#calcFilePath = 'C:\\Windows\\System32\\calc.exe'
#print(os.path.split(calcFilePath))
#print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))
#print(calcFilePath.split(os.sep))

#(12)
#Finding File Sizes and Folder Contents
#import os
#print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
#print(os.listdir('C:\\Windows\\System32'))
#totalSize = 0
#for filename in os.listdir('C:\\Windows\\System32'):
#      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
#print('\n Total Size of files in C:\\Windows\\System32  = '+str(totalSize))

#(13)
#Modifying a List of Files Using Glob Patterns
#from pathlib import Path
#p = Path('C:\\Users\\Ahmed.Sobhy\\Desktop\\doc')
#print(p.glob('*'))
#print(list(p.glob('*'))) # Make a list from the generator.
#print(list(p.glob('*.txt')))
#print(list(p.glob('note?.txt')))
#print(list(p.glob('*.?x?')))
#for textFilePathObj in p.glob('*.txt'):
#     print(textFilePathObj) # Prints the Path object as a string.

#(14)
#Checking Path Validity
#from pathlib import Path
#winDir = Path('C:/Windows')
#notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
#calcFile = Path('C:/Windows/System32/calc.exe')
#print(winDir.exists())
#print(winDir.is_dir())
#print(notExistsDir.exists())
#print(calcFile.is_file())
#print(calcFile.is_dir())
#dDrive = Path('D:/')
#print(dDrive.exists())

#(15)
#The File Reading/Writing Process
#from pathlib import Path
#p = Path('spam.txt')
#print(p.write_text('Hello, world!'))
#print(p.read_text())

#(16)
#Opening Files with the open() Function
#from pathlib import Path
#helloFile = open(Path.home() / 'hello.txt')
#print(Path.home())
#helloFile = open('C:\\Users\\Ahmed.Sobhy\\hello.txt')
##Reading the Contents of Files
#helloContent = helloFile.read()
#print(helloContent)
#sonnetFile = open(Path.home() / 'sonnet29.txt')
#print(sonnetFile.readlines())
##Writing to Files
#baconFile = open('bacon.txt', 'w')
#baconFile.write('Hello, world!\n')
#baconFile.close()
#baconFile = open('bacon.txt', 'a')
#baconFile.write('Bacon is not a vegetable.')
#baconFile.close()
#baconFile = open('bacon.txt')
#content = baconFile.read()
#baconFile.close()
#print(content)

#(17)
#Saving Variables with the shelve Module
#import shelve
#shelfFile = shelve.open('mydata')
#cats = ['Zophie', 'Pooka', 'Simon']
#shelfFile['cats'] = cats
#shelfFile.close()
#shelfFile = shelve.open('mydata')
#print(type(shelfFile))
#print(shelfFile['cats'])
#shelfFile.close()
#shelfFile = shelve.open('mydata')
#print(list(shelfFile.keys()))
#print(list(shelfFile.values()))
#shelfFile.close()

#(18)
#Saving Variables with the pprint.pformat() Function
#import pprint
#cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
#pprint.pformat(cats)
#fileObj = open('myCats.py', 'w')
#fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
#fileObj.close()
#import myCats
#print(myCats.cats)
#print(myCats.cats[0])
#print(myCats.cats[0]['name'])

#(19)
#Project: Generating Random Quiz Files
#Step 1: Store the Quiz Data in a Dictionary
#===============================================
#! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
#import random
#   # The quiz data. Keys are states and values are their capitals.
#capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',\
#   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',\
#   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',\
#   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':\
#   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':\
#   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':\
#   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':\
#   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':\
#   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':\
#   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
#   Mexico': 'Santa Fe', 'New York': 'Albany',\
#   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',\
#   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',\
#   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':\
#   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':\
#   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
#   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
##Step 2: Create the Quiz File and Shuffle the Question Order
##==========================================================
## Generate 35 quiz files.
#for quizNum in range(35):
#    # Create the quiz and answer key files.
#    quizFile = open(f'US_States_Capital_Quizes\\capitalsquiz{quizNum + 1}.txt', 'w')
#    answerKeyFile = open(f'US_States_Capital_Quizes\\capitalsquiz_answers{quizNum + 1}.txt', 'w')
#    # Write out the header for the quiz.
#    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
#    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
#    quizFile.write('\n\n')
#    # Shuffle the order of the states.
#    states = list(capitals.keys())
#    random.shuffle(states)
##Step 3: Create the Answer Options
##====================================
#    # Loop through all 50 states, making a question for each.
#    for questionNum in range(50):
#        # Get right and wrong answers.
#        correctAnswer = capitals[states[questionNum]]
#        wrongAnswers = list(capitals.values())
#        del wrongAnswers[wrongAnswers.index(correctAnswer)]
#        wrongAnswers = random.sample(wrongAnswers, 3)
#        answerOptions = wrongAnswers + [correctAnswer]
#        random.shuffle(answerOptions)
##Step 4: Write Content to the Quiz and Answer Key Files
## Loop through all 50 states, making a question for each.
#            # Write the question and the answer options to the quiz file.
#        quizFile.write(f'{questionNum + 1}.What is the capital of {states[questionNum]}?\n')
#        for i in range(4):
#            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
#            quizFile.write('\n')
#            # Write the answer key to a file.
#        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
#    quizFile.close()
#    answerKeyFile.close()

#(20)
#Project: Updatable Multi-Clipboard
#See mcb.pyw and mcb.bat