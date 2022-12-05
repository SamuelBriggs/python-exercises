number = int(input("Enter a number: "))
check = False
if number > 1:
    for x in range(2, number):
        if number % x == 0:
            check = True

if check:
    print(number, "is not a prime number")

else:
    print(number, "is a prime number")