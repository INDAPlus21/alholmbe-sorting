from random import randint
from main import initialize


def selection_sort(lst):
    for i in range(0, len(lst)):
        current_min_index = i
        current_min_value = lst[i]
        for j in range((i + 1), len(lst)):
            if lst[j] < current_min_value:
                current_min_index = j
                current_min_value = lst[j]

        tmp = lst[i]
        lst[i] = lst[current_min_index]
        lst[current_min_index] = tmp

        initialize(lst)
    return lst


if __name__ == "__main__":
    lst = []
    for i in range(50):
        lst.append(randint(0, 1000))

    selection_sort(lst)
