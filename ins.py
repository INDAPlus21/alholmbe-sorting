from random import randint
from main import initialize


def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j > 0 and lst[j-1] > lst[j]:
            tmp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = tmp
            j -= 1
        initialize(lst)

    return lst


if __name__ == "__main__":
    lst = []
    for i in range(50):
        lst.append(randint(0, 1000))
    insertion_sort(lst)
