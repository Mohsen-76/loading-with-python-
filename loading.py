from random import randrange
import time
from colorama import Fore

logo='''      
   ___  
  / _ \ 
 | (_) |
  \___/ 
'''
# print(len(logo))
# while True:
#     char=''
#     x=''
#     for i in range(0,10):
#         char+='O'
#         print(char,end='\r')
#         time.sleep(0.1)

#     for i in range(len(char)):
#         x+=' '
#         print(x,end='\r')
#         time.sleep(0.1)
while True:
    char=''
    char1=''
    for i in range(0,6):
        char+='O'
        if i!=5:
            char1+='O'
        space=((10-i)-len(char))*' '
        load_logo=f'{char}{space}{char1}'
        print(Fore.YELLOW+load_logo,end='\r')
        time.sleep(0.1)


    char=''
    char1=''
    for i in range(0,6):
        char+=' '
        if i!=5:
           char1+=' '
        space=((10-i)-len(char))*'O'
        load_logo=f'{char}{space}{char1}'
        print(Fore.RED+load_logo,end='\r')
        time.sleep(0.1) 
      