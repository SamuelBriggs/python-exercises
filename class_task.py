number = int(input("Enter a number here: "))

largest = number
smallest = number


while number != 0:

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    number = int(input("Input another number: "))

print(smallest)
print(largest)