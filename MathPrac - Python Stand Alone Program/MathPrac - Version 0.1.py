import random

version = 0.01


print("WELCOME\n")
print("This Application was made using Python 3.3 & Microsoft Visual Studio 10\n")
print("This Application is called MathPract. It helps people of all ages practice mathematics")
print("MathPrac was designed and coded by Liam Angus (LiamWA11)")
print("It is version " + str(version))

firstName = input("What is your first name? \n")
#lastName = input("What is you last name? \n")
evenQuestions = True
numberOfQuestions = 0
valuesOkay = False


while (valuesOkay == False):
    firstValue = float(input("Please input the minimum number for the sums. (PS: It can be a decimal and/or negative number)\n"))
    secondValue = float(input("Please input the maximum number for the sums (PS: PLEASE make is larger than '" + str(firstValue) + "' (the first number), Also, it can be a negative and/or decimal too)\n"))
    if (firstValue <= secondValue):
        #print(valuesOkay)
        valuesOkay = True
        #print(valuesOkay)
    elif(firstValue > secondValue):
        #print(valuesOkay)
        valuesOkay = False
        #print(valuesOkay)
        print(str(firstValue) + " is not '<' (Less Than) " + str(secondValue) + ". Please choose these two values again.")

print("A random number will be chosen in between " + str(firstValue) + " and " + str(secondValue) + " for the sums.")
print("The min & max numbers do not work for division (/)")

while evenQuestions == True:
    numberOfQuestions = input(firstName + ", How many questions do you want? Please input an even number. \n")
    evenQuestions = False
score = 0
totalQuestions = 0

while float(numberOfQuestions) >= float(1):
     operation = None
     randOperation = random.randint(0, 3)
     #randOperation = 3
    #print('OPERATION: ' + str(randOperation))

     if int(randOperation) == 0:
         operation = '+'
         print(str(operation))
         
         for questions in range(0, int(numberOfQuestions)):
          randInt1 = random.randint(firstValue, secondValue)
          randInt2 = random.randint(firstValue, secondValue)
          answer = input(str(randInt1) + '+' + str(randInt2) + '\n')
          #print("DEBUG")
          if float(answer) == float(float(randInt1) + float(randInt2)):
            print("Your answer was correct")
            score = score + 1
            totalQuestions = totalQuestions + 1
          else:
            print("You answered " + str(answer) + ". The correct answer was " + str(float(randInt1) + float(randInt2)))
            totalQuestions = totalQuestions + 1
          numberOfQuestions = int(numberOfQuestions) - 1

     elif int(randOperation) == 1:
         operation = '-'
         print(str(operation))

         for questions in range(0, int(numberOfQuestions)):
          randInt1 = random.randint(firstValue, secondValue)
          randInt2 = random.randint(firstValue, secondValue)
          answer = input(str(randInt1) + '-' + str(randInt2) + '\n')
          #print("DEBUG")
          if float(answer) == float(float(randInt1) - float(randInt2)):
            print("Your answer was correct")
            score = score + 1
            totalQuestions = totalQuestions + 1
          else:
            print("You answered " + str(answer) + ". The correct answer was " + str(float(randInt1) - float(randInt2)))
            totalQuestions = totalQuestions + 1
         numberOfQuestions = int(numberOfQuestions) - 1

     elif int(randOperation) == 2:
         operation = '*'
         print(str(operation))

         for questions in range(0, int(numberOfQuestions)):
          randInt1 = random.randint(firstValue, secondValue)
          randInt2 = random.randint(firstValue, secondValue)
          answer = input(str(randInt1) + '*' + str(randInt2) + '\n')
          #print("DEBUG")
          if float(answer) == float(float(randInt1) * float(randInt2)):
            print("Your answer was correct")
            score = score + 1
            totalQuestions = totalQuestions + 1
          else:
            print("You answered " + str(answer) + ". The correct answer was " + str(float(randInt1) * float(randInt2)))
            totalQuestions = totalQuestions + 1
         numberOfQuestions = int(numberOfQuestions) - 1

     elif int(randOperation) == 3:
         operation = '/'
         print(str(operation))

         randInt1Zero = True
         randInt2Zero = True
         
         for questions in range(0, int(numberOfQuestions)):
          while (randInt1Zero == True):
            randInt1 = random.randint(firstValue, secondValue)
            #print(randInt1)
            if randInt1 == 0:
                randInt1Zero = True
            elif randInt1 != 0:
                randInt1Zero = False
          while (randInt2Zero == True):
            randInt2 = random.randint(firstValue, secondValue)
            if randInt2 == 0:
                randInt2Zero = True
            elif randInt2 != 0:
                randInt2Zero = False
          #print(randInt1)
          answer = input(str(randInt1) + '/' + str(randInt2) + '\n')
          #print("DEBUG")
          if float(answer) == float(float(randInt1) / float(randInt2)):
            print("Your answer was correct")
            score = score + 1
            totalQuestions = totalQuestions + 1
          else:
            print("You answered " + str(answer) + ". The correct answer was " + str(float(randInt1) / float(randInt2)))
            totalQuestions = totalQuestions + 1    
         numberOfQuestions = int(numberOfQuestions) - 1
              
print("Your Score Is " + str(score) + " Out Of " + str(totalQuestions))
