import random

guess_taken = 0 

print("Hello! What is your name?")
name = input()

num =random.randint(0,100)

guess=int(input (name +"  I am thinking of a number between 1 and 100,can you guess what is it?  "))

while guess_taken<9:
    guess_taken = guess_taken +1
    if guess < num:
        print("you need to guess higher..Try again!!")
        guess=int(input("(guess a number between 1 and 100) - "))
    else:
        print("you need to guess lower..Try again!")
        guess=int(input("(guess a number between 1 and 100) - "))
    if guess==num:
        break

if guess==num:
    guess_taken = str (guess_taken)
    print("Good job! ",name +" you guessed my number in ",guess_taken + " guesses")
   
if guess!=num:
     num = str (num)
     print("nope, The number I was thinking is",num)

