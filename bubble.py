from random import randint


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == "__main__":
    lst = []
    for i in range(50):
        lst.append(randint(0, 1000))
    print(bubble_sort(lst))
