import random
import matplotlib.pyplot as plt
import numpy as np
def generate_random_array(size):
    array = []
    for i in range(size):
        array.append(random.randint(1, 10000000))
    return array
def generate_sorted_array(size):
    return list(range(size))

def generate_reversed_sorted_array(size):
    return list(range(size - 1, -1, -1))
def shell_sort(arr):
    compares = 0
    swaps = 0
    size = len(arr)
    gap = 1
    while gap < size // 3:
        gap = 3 * gap + 1
    while gap >= 1:
        for i in range(gap, size):
            temp = arr[i]
            j = i
            while j >= gap:
                compares += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break
            arr[j] = temp
        gap //= 3
    print(f"Total Compares: {compares}")
    print(f"Total Swaps: {swaps}")
def bubble_sort(arr):
    compares = 0
    swaps = 0
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            compares += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f" Total Compares: {compares}")
    print(f" Total Swaps: {swaps}")

def modified_bubble_sort(arr):
    compares = 0
    swaps = 0
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            compares += 1
            if arr[j] > arr[j + 1]:
                swaps +=1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    print(f" Total Compares {compares}")
    print(f" Total Swaps {swaps}")

size_of_sorted_array = [10, 100, 1000,5000, 10000, 20000, 50000]

for i in range(len(size_of_sorted_array)):
    print(f"Total elements:{size_of_sorted_array[i]}")
    print("shell sort:")
    shell_sort(generate_reversed_sorted_array(size_of_sorted_array[i]))
    print("bubble sort:")
    bubble_sort(generate_reversed_sorted_array(size_of_sorted_array[i]))
    print("modified bubble sort:")
    modified_bubble_sort(generate_reversed_sorted_array(size_of_sorted_array[i]))