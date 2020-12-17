password=0
it=0
cred = False
while it<3 and cred == False:
      it=it+1
      print('Who are you?')
      name = input()
      if name != 'Joe':
         continue
      print('Hello, Joe. What is the password? (It is a fish.)')
      password = input()
      if password == 'swordfish':
         cred=True
         break
if cred==False:
   print('Access denied.')
else :
   print('Access granted.')