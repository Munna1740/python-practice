'''
#user input
num1 = input("Enter the first value: ")
num2 = input("Enter the second value: ")
sum = float(num1) + float(num2)
print(sum)
div = float(num1)/ int(num2)
print(div)

#------------------End-------------------------
# see with type number
num1 = 20
num2 = 60
sum = num1+num2
print(f"{num1}+{num2}= {sum}")
#----------------------------------------------

#----------------------------------------------
# multiple print statement in show in single line
print("Name: Md Mostafa Munna ",end=" ")
print("Phone:01824807920")
#----------------------End---------------------


#----------------------LIST--------------------
#list practice:
subject = ["C","C++","Python","C#","Java","JavaScript"]
print(subject)
print(subject[3])
print(subject[3:]) # when we give (:) it works as a loop. Its shows index 3 to rest of the list.
print(subject[-1]) #It shows from the last. when we type -1.

# in operator.it check the word on the list or not.
print("Python" in subject)

# not in operator:
print("Php" not in subject)

# add item in the list: 
subject = subject+["Swift"]
print(subject)

#use different function in list:
print(len(subject))

# append function:
subject.append("Go") # add item in the last.
print(subject)

#insert function:
subject.insert(2,"HTML")
print(subject)

# remove function:
subject.remove("Go")
print(subject)

# sort function:(choto theke boro )
number = [20,6,45,12,92,30]
number.sort()
print(number)

# reverse function:(boro theke choto)
number.reverse()
print(number) 

#pop function:( remove items from last)
number.pop()
print(number)

#copy the list:
number2 = number.copy()
print(number2)

#clear the list:
number2.clear()
print(number2)

# identify the item possition in the list:
possition = number.index(20)
print("12 position in the array is : ", possition)

# count function:
count = number.count(12)
print("12 in the array:", count, "times")
#------------------End-------------------------


#-----------------Range------------------------
num = list(range(10))
print(num)

num2 = list(range(5, 21)) # define range
print(num2)

num3 = list(range(5, 51,2)) # define range with difference
print(num3)
#-------------------------------End----------------------------------


#---------------------While & For loop-------------------------------

number = [60,30,20,10,40,50,80]
index = 0
while index < len(number):
    print(number[index])
    index = index+1
#using for loop
for x in number:
    print(x)

#sum of the listed items
sum = 0
for x in number:
    sum = sum + x
print(sum)
#-----------------------End-------------------------


#---------------------Series------------------------
#1+2+3.....n (sum)
number = int(input("Enter the number: "))
sum = 0
for x in range(1,number+1,1):
    sum= sum+x
print(sum)
#----------------------End---------------------------

#--------------------------Pattern--------------------------

#*
#**
#***
#****

n = 4
for i in range(n+1):
    print(i*"*")

#*
#***
#*****

n = 4
for i in range(n+1):
    print((2*i-1)*"*")
#----------------------------------------------------------

#----------------------Guessing Game-----------------------
from random import randint
for x in range(1,4):
    guessNumber = int(input("Enter the guessing Number: "))
    randomNumber = randint(1,10)
    if guessNumber == randomNumber:
        print("Yeh!! You have won ")
        print("Here random number was", randomNumber)
    else:
        print("Ops!! You have loss" )
        print("Here random number was", randomNumber)
#-----------------------End--------------------------------


#--------------------------List as a user input------------

inputList = input("Enter the list element: ")
list = inputList.split()
print(list)
#--------------------------------End-----------------------

#-------------------------------check how many number,text and word in any sentance-------------------------------

numberOfWords = 0
numberOfLetter = 0
numberOfDigit = 0

text = input("Enter the text of the number: ")

for x in text:
    x = x.lower()
    if (x>='a' and x<='z'):
        numberOfLetter = numberOfLetter+1

    elif(x>='0' and x<='9'):
        numberOfDigit = numberOfDigit+1

    elif x == ' ':
        numberOfWords=numberOfWords+1

print("Number of letter is: ", numberOfLetter)
print("Number of digit is: ", numberOfDigit)
print("Number of words is :",numberOfWords+1)
#----------------------------------------------------End---------------------------------------------------------
'''




