#(1)
#The shutil Module
#Copying Files and Folders
#import shutil, os
#from pathlib import Path
#p = Path.cwd()
#print(p)
#Removing entire folders and their contents
#shutil.rmtree('.\\some_folder')
#shutil.rmtree('.\\some_folder_backup')
#Copying Files
#os.makedirs('.\\some_folder')
#p1=shutil.copy(p / 'spam.txt', p / 'some_folder')
#print(p1)
#p2=shutil.copy(p / 'spam.txt', p / 'some_folder/spam2.txt')
#print(p2)
##Copying an entire folder and every folder and file contained in it
#p3=shutil.copytree(p / 'some_folder', p / 'some_folder_backup')
#print(p3)
#(2)
#Moving and Renaming Files and Folders
#Moving_File = open(p/'Moving_File.txt', 'w')
#Moving_File.write('This is a file for Moving(cut) and Renaming operations \n')
#Moving_File.close()
#shutil.move(".\\Moving_File.txt", ".\\some_folder")
#shutil.move(p/'some_folder\\Moving_File.txt', p/'some_folder_backup\\new_Moving_File.txt')

#(3)
#Removing files in US_States_Capital_Quizes folder created before in ch9
#Calling os.unlink(path) will delete the file at path.
#import os
#from pathlib import Path
##US_States_Capital_Quizes folder_Path=Path('.\\US_States_Capital_Quizes')
#for filename in Path('.\\US_States_Capital_Quizes') .glob('*.txt'):
#    #print(filename)
#    os.unlink(filename)
###Removing US_States_Capital_Quizes after being embty
##Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
#os.rmdir('.\\US_States_Capital_Quizes')

#(4)
#Safe Deletes with the send2trash Module
#import send2trash
#baconFile = open('bacon1.txt', 'a')   # creates the file
#baconFile.write('Bacon is not a vegetable.')
#baconFile.close()
#send2trash.send2trash('bacon1.txt')

#(5)
#Walking a Directory Tree
#import os
#from pathlib import Path
#for folderName, subfolders, filenames in os.walk(Path.cwd()):
#    print('The current folder is ' + folderName)
#    for subfolder in subfolders:
#        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#    for filename in filenames:
#        print('FILE INSIDE ' + folderName + ': '+ filename)
#    print('')

#(6)
#Creating and Adding to ZIP Files
#import zipfile, os
#from pathlib import Path
#newZip = zipfile.ZipFile('new.zip', 'w')
#newZip.write('Zipped_Folder_Example', compress_type=zipfile.ZIP_DEFLATED)
#newZip.close()
#newZip = zipfile.ZipFile('new.zip', 'a')
#newZip.write('Zipped_File_Example.txt', compress_type=zipfile.ZIP_DEFLATED)
#newZip.close()
##Reading ZIP Files
#exampleZip = zipfile.ZipFile('new.zip')
#print(exampleZip.namelist())
#spamInfo = exampleZip.getinfo('Zipped_File_Example.txt')
#print(spamInfo.file_size)
#print(spamInfo.compress_size)
#print( f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!' )
#exampleZip.close()
##Extracting from ZIP Files
##Extractall contents
#exampleZip = zipfile.ZipFile('new.zip')
#exampleZip.extractall()
#exampleZip.close()
##Extractall contents to a certain folder : Zipped_Folder_Example
#exampleZip = zipfile.ZipFile('new.zip')
#exampleZip.extractall('Zipped_Folder_Example')
#exampleZip.close()
##Extract one file
#exampleZip = zipfile.ZipFile('new.zip')
#exampleZip.extract('Zipped_File_Example.txt')
#exampleZip.close()
##Extract one file to a certain folder : Zipped_Folder_Example
#exampleZip = zipfile.ZipFile('new.zip')
#exampleZip.extract('Zipped_File_Example.txt','.\\Zipped_Folder_Example\\New_zip_Folder')
#exampleZip.close()

#(7)
#PROJECT: RENAMING FILES WITH AMERICAN-STYLE DATES TO EUROPEAN-STYLE DATES
#Step 1: Create a Regex for American-Style Dates
#! python3
   # renameDates.py - Renames filenames with American MM-DD-YYYY date format
   # to European DD-MM-YYYY.
#import shutil, os, re
## Create a regex that matches files with the American date format.
#datePattern = re.compile(r"""^(.*?) # all text before the date
#       ((0|1)?\d)-                     # one or two digits for the month
#       ((0|1|2|3)?\d)-                 # one or two digits for the day
#       ((19|20)\d\d)                   # four digits for the year
#       (.*?)$                          # all text after the date
#       """, re.VERBOSE)
##Step 2: Identify the Date Parts from the Filenames
## Loop over the files in the working directory.
#for amerFilename in os.listdir('.\\Files_Renaming_project_folder'):
#    mo = datePattern.search(amerFilename)
#    # Skip files without a date.
#    if mo == None:
#       continue
#    # Get the different parts of the filename.
#    beforePart = mo.group(1)
#    monthPart  = mo.group(2)
#    dayPart    = mo.group(4)
#    yearPart   = mo.group(6)
#    afterPart  = mo.group(8)
##Step 3: Form the New Filename and Rename the Files
## Form the European-style filename.
#    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
#     # Get the full, absolute file paths.
#    absWorkingDir = os.path.abspath('.\\Files_Renaming_project_folder')
#    amerFilename = os.path.join(absWorkingDir, amerFilename)
#    euroFilename = os.path.join(absWorkingDir, euroFilename)
#     # Rename the files.
#    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
#    shutil.move(amerFilename, euroFilename)   # uncomment after testing

#(8)
#Project: Backing Up a Folder into a ZIP File
#! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.
#Step 1: Figure Out the ZIP File’s Name
#import zipfile, os
#def backupToZip(folder):
#    # Back up the entire contents of "folder" into a ZIP file.
#    folder = os.path.abspath(folder)   # make sure folder is absolute
#    # Figure out the filename this code should use based on
#    # what files already exist.
#    number = 1
#    while True:
#          zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
#          if not os.path.exists(zipFilename):
#             break
#          number = number + 1
##Step 2: Create the New ZIP File
#    # Create the ZIP file.
#          print(f'Creating {zipFilename}...')
#          backupZip = zipfile.ZipFile(zipFilename, 'w')
##Step 3: Walk the Directory Tree and Add to the ZIP File
#    # Walk the entire folder tree and compress the files in each folder.
#          for  foldername, subfolders, filenames in os.walk(folder):
#               print(f'Adding files in {foldername}...')
#         # Add the current folder to the ZIP file.
#               backupZip.write(foldername)
#         # Add all the files in this folder to the ZIP file.
#               for filename in filenames:
#                   newBase = os.path.basename(folder) + '_'
#                   if filename.startswith(newBase) and filename.endswith('.zip'):
#                      continue   # don't back up the backup ZIP files
#                   backupZip.write(os.path.join(foldername, filename))
#               backupZip.close()
#    print('Done.')
#backupToZip('C:\\Delicious')