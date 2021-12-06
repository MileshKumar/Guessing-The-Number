#please import the random module.
import random

#to create a varible and define randon funtion.
number = random.randint(1,10)

#using for loop to define three time of chance to guess the number currect.
for i in range(0,3):

    #user's input for the guess number
    user = int(input("Guess the number : "))

    #using if statement for guess currect number's,
    #.then true print first statement & false print second statement.
    if user == number:
        print("Yipiii !!")
        print("You Guess The Number is Right\nYou are a good coder.")
        break
    #second statement (false).
    if user!= number:
            print ("Your Guess Is Incurrect Please Try Again Latter")