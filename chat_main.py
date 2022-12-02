import random

print('Hello this is a test ,what is your favourite number?')

computerfavnumber=17

favnumber=input()
print(favnumber + ' ... is a very nice number indeed. So , what is your name?')
name=input()
print('what a lovely name:  ' + name + '... 4now, I will reveal what my favourite number is:')

print (computerfavnumber)

favcolour=input("Now, tell me, what is your favourite colour?")

print(favcolour + " ... Wow! That is my favourite colour too!") 


print("Lets play a game! I am thinking of a number between 1 and 20. Try to guess the number!")

guessesTaken = 0

number = random.randint(1, 20)

while guessesTaken < 3:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = (guessesTaken)
    print('Good job! You guessed my number in ' + str(guessesTaken + ' guesses!'))

if guess != number:
    number = (number)
    print('Nope. The number I was thinking of was ' + str(number))

print("That was a fun game! BTW what is your best skill?")
bestskill=input()
print( bestskill + " ... that's good. My best skill is having tea")
old = int(input("how old are you ? [Number]"))
year = 2022 - old
ms3 = " Oh !, so you were born in "
print(ms3 + str(year))
fav = input("I like english, what about you ?")
ms4 = "Why do you like it "
ms5 = "?"
ms6 = input (ms4 + ms5)
print ("I can sure about that")
ms7 = (input(" What do you think about this tester ?"))
print("Thank for your repl !")
#Just testing it all
