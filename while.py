import random

number_to_be_guessed = random.randint(1,100)

count = 0


while count < 3:

    guess = int(input("Enter a random number here: "))

    if guess == number_to_be_guessed:
        print("You got it right, kudos!")
        break

    elif guess > number_to_be_guessed:
        print("number is higher", guess, number_to_be_guessed)

    elif guess < number_to_be_guessed:
        print ("number is less", guess, number_to_be_guessed)
    count = count + 1


if guess!= number_to_be_guessed:
    print("loser")




