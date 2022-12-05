number = int(input("Enter a number "))
count = 0

for x in range(1, number+1):
    if number % x == 0:
        print (x)
        count += 1

print(number, "has", count, "factors")