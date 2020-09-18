print('hello world')
#this is a comment
#this is also a comment
#this is yet another comment
userAge = 0
userAge, username=30, 'Peter'
userAge=30
userName = 'Peter'
x=5
y=10
y=5
x=y
print("x= ", x)
print("y= ", y)
y=5

#userAge=20, mobileNumber = 12398724. in the notes
#userHeight = 1.82, userWeight = 67.2. in the notes


brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR'% (brand, 1299, exchangeRate)
print (message)
#the scripts have to be in the same line, otherwise the program will assume that the continuation
#in the next line is a different script
message1 = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR' .format('apple', 1299, 1.235235245)
print(message1)
message2 = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR' .format('apple', 1299, 1.235235245)
print(message2)


#declaring the list, list elements can be of different data types
myList = [1, 2, 3, 4, 5, 'Hello']
#print the entire list.
print(myList)
#You’ll get [1, 2, 3, 4, 5, “Hello”]

#print the third item (recall: Index starts fromzero).
print(myList[2])
#You’ll get 3

#print the last item.
print(myList[-1])
#You’ll get “Hello”

#assign myList (from index 1 to 4) to myList2 and print myList2
myList2 = myList[1:5]
print (myList2)

#modify the second item in myList and print the updated list
myList[1] = 20
print(myList)
#You’ll get [1, 20, 3, 4, 5, 'Hello']

#append a new item to myList and print the updated list
myList.append('How are you')
print(myList)
#You’ll get [1, 20, 3, 4, 5, 'Hello', 'How are you']

#remove the sixth item from myList and print the updated list
del myList[5]
print(myList)
#You’ll get [1, 20, 3, 4, 5, 'How are you']

#declaring the dictionary, dictionary keys and
#data can be of different data types
myDict = {'One':1.35, 2.5:'Two Point Five', 3:'+',7.9:2}

#print the entire dictionary
print(myDict)
#You’ll get {2.5: 'Two Point Five', 3: '+', 'One':1.35, 7.9: 2}
#Note that items in a dictionary are not stored in
#the same order as the way you declare them.

#print the item with key = “One”.
print(myDict['One'])
#You’ll get 1.35


#print the item with key = 7.9.
print(myDict[7.9])
#You’ll get 2

#modify the item with key = 2.5 and print the
#updated dictionary
myDict[2.5] = 'Two and a Half'
print(myDict)
#You’ll get {2.5: 'Two and a Half', 3: '+', 'One':
#1.35, 7.9: 2}


#add a new item and print the updated dictionary
myDict['New item'] = 'I’m new'
print(myDict)
#You’ll get {'New item': 'I’m new', 2.5: 'Two and
#a Half', 3: '+', 'One': 1.35, 7.9: 2}


#remove the item with key = “One” and print the
#updated dictionary
del myDict['One']
print(myDict)
#You’ll get {'New item': 'I’m new', 2.5: 'Two and
#a Half', 3: '+', 7.9: 2}

myName = input("Please enter your name: ")
myAge = input("What about your age: ")

print ("Hello World, my name is", myName, "and I am", myAge, "years old.")

userInput = input('Enter 1 or 2: ')
if userInput == '1':
    print ('Hello World')
    print ('how are you')
elif userInput == '2':
    print ("Python Rocks!")
    #print (“I love Python”)
else:
    print ("You did not enter a valid number")

pets = ['cats', 'dogs', 'rabbits', 'hamsters']
for myPets in pets:
    print (myPets)

counter = 5
while counter > 0:
    print ('Counter = ', counter)
    counter = counter - 1

j = 0
for i in range(5):
        j = j + 2
        print ('i = ', i, ', j = ', j)
        if j == 6:
             break

j = 0
for i in range(5):
        j = j + 2
        print ('\ni = ', i, ', j = ', j)
        if j == 6:
         continue
        print ('I will be skipped over if j=6')

try:
    userInput1 = int(input('Please enter a number: '))
    userInput2 = int(input('Please enter another number: '))
    answer =userInput1/userInput2
    print ('The answer is ', answer)
    myFile = open('missing.txt', 'r')
except ValueError:
    print ('Error: You did not enter a number')
except ZeroDivisionError:
    print ('Error: Cannot divide by zero')
except Exception as e:
    print ('Unknown error: ', e)

def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
         if (numberToCheck%x == 0):
             return False
    return True

message5 = 'Global Variable'
def myFunction():
    print('\nINSIDE THE FUNCTION')
    #Global variables are accessible inside a
    #function
    print (message5)
    #Declaring a local variable
    message6 = 'Local Variable'
    print (message6)

#Calling the function
myFunction()
print('\nOUTSIDE THE FUNCTION')
#Global variables are accessible outside function
print (message5)

#Local variables are NOT accessible outside function.
print (message6)




