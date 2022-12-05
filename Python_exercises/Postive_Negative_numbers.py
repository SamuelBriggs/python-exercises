positive_number_count = 0
negative_number_count = 0
numbers_added_together = 0


integer_number = int(input("Enter an integer, the input ends if is 0: "))

while integer_number != 0:
    if integer_number > 0:
        positive_number_count += 1
        numbers_added_together += integer_number
    elif integer_number < 0:
        negative_number_count += 1

    integer_number = int(input(""))
total = positive_number_count+negative_number_count
if total < 1:
    print("No numbers were entered except 0")
else:
    print("Number of positive numbers is: ", positive_number_count)
    print("Number of negative numbers is: ", negative_number_count)
    actual_average = numbers_added_together / positive_number_count
    print("The total is: ", numbers_added_together)
    print("The actual average is ", actual_average)


