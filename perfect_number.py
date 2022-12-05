number = int(input("Enter a number here: "))
factors = 0
count = 1


while count < number:
    if number % count == 0:
        print(count)
        factors +=  count
    count +=1


if factors == number:
    print(number, "is a perfect number")

elif factors < number:
    print(number, "is a deficient number")

else:
    print(number, "is a abundant number")



