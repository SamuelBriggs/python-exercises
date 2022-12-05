x = [12, 3, 3, 4, 16, 4, 2, 6, 1, 1, 243, 353, 4654]
y = [2, 18, 3, 21, 4, 12, 19, 8]


def is_unique(lst):

    for index, number in enumerate(lst):
        if number in lst[index+1:]:
            return "List is not unique"
    return "List is Unique"

print(is_unique(y))
