#Prints the words "hello world"
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



