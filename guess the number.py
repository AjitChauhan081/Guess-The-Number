#guess the number
import random

print("Hello, What is your name?")
name = str(input())
print('well, ' + name + ' I am thinking of a number between 1 and 20')

oldnum=random.randint(1,20)

for gues in range(1,5):
      print('Take a guess')
      num = int(input())
      if num < oldnum:
          print("Your guess is to low")
      elif num > oldnum:
          print("Your guess is to high")
      else:
          break

if num == oldnum:
    print("Goodjob, "+ name +"! You have guessed my number in gues")
else:
    print("Nope. The number I was thinking of was " + str(oldnum))

    
          
        
          
          
      
      
