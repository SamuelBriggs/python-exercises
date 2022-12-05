today_day = int(input("Enter today's day: "))

future_days = int(input("Enter the number of days elapsed since today: "))

actual_future_days= today_day + future_days

if today_day == 1:
    print("Today is Monday", end= " ")

elif today_day == 2:
    print("Today is Tuesday", end= " ")

elif today_day == 3:
    print("Today is Wednesday", end= " ")

elif today_day == 4:
    print("Today is Thursday", end= " ")

elif today_day == 5:
    print("Today is Friday", end= " ")

elif today_day == 6:
    print("Today is Saturday", end= " ")

elif today_day == 0:
    print(today_day, "Sunday", end= " ")


if actual_future_days == 1:
    print("and the future day is Monday")

elif actual_future_days == 2:
    print("and the future day is Tuesday")

elif actual_future_days == 3:
    print("and the future day is Wednesday")

elif actual_future_days == 4:
    print("and the future day is Thursday")

elif actual_future_days == 5:
    print("and the future day is Friday")

elif actual_future_days == 6:
    print("and the future day is Saturday")

elif actual_future_days ==7:
    print("and the future day is Sunday")

elif actual_future_days > 7:
    print("Invalid future day number")



