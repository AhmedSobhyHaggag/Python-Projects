'''webbrowser Comes with Python and opens a browser to a specific page.
requests Downloads files and web pages from the internet.
bs4 Parses HTML, the format that web pages are written in.
selenium Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.'''
#(1)
#Project: mapIt.py with the webbrowser Module
#See mapIt.py, also check batch files at C:\Users\Ahmed.Sobhy\AppData\Local\Programs\Python\Python38\Scripts
#import webbrowser
#webbrowser.open('https://inventwithpython.com/')

#(2)
#import requests
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print(type(res))
#res.status_code == requests.codes.ok
#print(len(res.text))
#print(res.text[:251])

#(3)
#Checking for Errors
#import requests
#res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
#try:
#    res.raise_for_status()
#except Exception as exc:
#    print('There was a problem: %s' % (exc))

#(4)
#Saving Downloaded Files to the Hard Drive
#import requests
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print(res.raise_for_status())
#playFile = open('RomeoAndJuliet.txt', 'wb')
##you need to write binary'wb' data instead of text data in order to maintain the Unicode encoding of the text.
#for chunk in res.iter_content(100000):
#    playFile.write(chunk)
#playFile.close()

#(5)
#HTML
#Parsing HTML with the bs4 Module
#see example.html.
#Creating a BeautifulSoup Object from HTML
#from Website
#import requests, bs4
#res = requests.get('https://nostarch.com')
#print(res.raise_for_status())
#noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
#print(type(noStarchSoup))
##from an Html file on our disk
#exampleFile = open('example.html')
#exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
#print(type(exampleSoup))

#(6)
#Finding an Element with the select() Method
#import bs4
#exampleFile = open('example.html')
#exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
#elems = exampleSoup.select('#author')
#print(type(elems))  #elems is a list of Tag objects.
#print(len(elems))
#print(type(elems[0]))
#print(str(elems[0])) #The Tag object as a string.
#print(elems[0].getText())
#print(elems[0].attrs)
#pElems = exampleSoup.select('p')
#print(str(pElems[0]))
#print(pElems[0].getText())
#print(str(pElems[1]))
#print(pElems[1].getText())
#print(str(pElems[2]))
#print(pElems[2].getText())

#(7)
#Getting Data from an Element’s Attributes
#import bs4
#soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
#spanElem = soup.select('span')[0]
#print(str(spanElem))
#print(spanElem.get('id'))
#print(spanElem.get('some_nonexistent_addr') == None )
#print(spanElem.attrs )

#(8)
#Project: Opening All Search Results
#See searchpypi.py

#(9)
#Project: Downloading All XKCD Comics
#You can Open a new file editor tab and save it as downloadXkcd.py
#Step 1: Design the Program
#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
#import requests, os, bs4
#url = 'https://xkcd.com'               # starting url
#os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
#while not url.endswith('#'):
##Step 2: Download the Web Page
## Download the page.
#    print('Downloading page %s...' % url)
#    res = requests.get(url)
#    print(res.raise_for_status())
#    soup = bs4.BeautifulSoup(res.text, 'html.parser')
##Step 3: Find and Download the Comic Image
# # Find the URL of the comic image.
#    comicElem = soup.select('#comic img')
#    if comicElem == []:
#        print('Could not find comic image.')
#    else:
#        comicUrl = 'https:' + comicElem[0].get('src')
#        # Download the image.
#        print('Downloading image %s...' % (comicUrl))
#        res = requests.get(comicUrl)
#        print(res.raise_for_status())
##Step 4: Save the Image and Find the Previous Comic
## Save the image to ./xkcd.
#        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
#        for chunk in res.iter_content(100000):
#            imageFile.write(chunk)
#        imageFile.close()
## Get the Prev button's url.
#    prevLink = soup.select('a[rel="prev"]')[0]
#    url = 'https://xkcd.com' + prevLink.get('href')
#print('Done.')

#(10)
#Controlling the Browser with the selenium Module
#Starting a selenium-Controlled Browser
#from selenium import webdriver
#browser = webdriver.Chrome()
#print(type(browser))
#browser.get('https://inventwithpython.com')

#(11)
#Finding Elements on the Page
#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.get('https://inventwithpython.com')
#try:
#    elem = browser.find_element_by_class_name('cover-thumb')
#    print('Found <%s> element with that class name!' % (elem.tag_name))
#except:
#    print('Was not able to find an element with that name.')

#(12)
#Clicking the Page
#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.get('https://inventwithpython.com')
#linkElem = browser.find_element_by_link_text('Read Online for Free')
#print(type(linkElem))
#linkElem.click() # follows the "Read Online for Free" link

#(13)
#Filling Out and Submitting Forms
#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.get('https://login.metafilter.com')
#userElem = browser.find_element_by_id('user_name')
#userElem.send_keys('your_real_username_here')
#passwordElem = browser.find_element_by_id('user_pass')
#passwordElem.send_keys('your_real_password_here')
#passwordElem.submit()

#(14)
#Sending Special Keys
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#browser = webdriver.Chrome()
#browser.get('https://nostarch.com')
#htmlElem = browser.find_element_by_tag_name('html')
#htmlElem.send_keys(Keys.HOME)    # scrolls to top
#htmlElem.send_keys(Keys.END)     # scrolls to bottom

#(15)
'''Clicking Browser Buttons
The selenium module can simulate clicks on various browser buttons as well through the following methods:
browser.back() Clicks the Back button.
browser.forward() Clicks the Forward button.
browser.refresh() Clicks the Refresh/Reload button.
browser.quit() Clicks the Close Window button.'''