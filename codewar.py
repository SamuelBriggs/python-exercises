def return_outlier(lst):
    outlier = 0
    new_list = []
    for x in lst:
        if x % 2!= 0:
            new_list.append(x)
        else:
            outlier = x
    if len(new_list) == 1:
        print(lst)
        print("This is List comprising of even numbers, the outlier here is: ", end="")
        return new_list[0]
    else:
        print(lst)
        print("This is a list comprising of Odd Numbers, the outlier is: ", end="")
        return outlier

fg = [4,7,6,8,10,12]
th = [3,5,4,1,7]
ch = [1,3,5,7,9,11,8]

print(return_outlier(fg))