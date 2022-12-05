

largest = float("-inf")
smallest = float("inf")

continue_loop = input("Do you want to enter a number?: ")

while continue_loop == "yes":
    num = int(input("Enter a number here: "))

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    continue_loop = input("Do you still want to enter a number? : ")

print(largest)
print(smallest)
