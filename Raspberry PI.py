import datetime
Select_name = input('what would you like to call me?')
whatIsYourName = input('what would like me to call you')
class AI:
      
      def __init__(self, name):
            self.name = name
            
P1 = AI(Select_name)

def list():
      print('define words(type define than the word you want to define) \n tell you my name (make sure you type What is your name) \n What i am (type what are you) \n Tell you the time \n'

whatIsYourName = ('my name' + P1)
WhatCanIDO = 'here is a list of things i can do'
WhatAreYou = 'I am a ANI or Artificial Narrow Intelligence'
now = datetime.datetime.now()
currenttime = now.hour + ':', now.min

            
            
Maininput = input('Hello what can i do for you')


if Maininput == 'what is your name':
      print(whatIsYourName)
            
if Maininput == 'what are you:
            print(WHatCanIDo)
            
if Maininput == 'Hey' + Select_name:
            print('hello' + whatIsYourName+ ',What can i help you with)

if Maininput == 'what time is it':
                  print(now)
                  
            
            

    
