import random



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
            while j >= gap and arr[j - gap] > temp:
                compares+=1
                arr[j] = arr[j - gap]
                j -= gap
                swaps += 1
            arr[j] = temp
        gap //= 3
    print(f" Total Compares {compares}")
    print(f" Total Swaps {swaps}")

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
    print(f" Total Compares: {compares} \n")
    print(f" Total Swaps: {swaps}\n")

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
        print(f" Total Compares {compares}\n")
        print(f" Total Swaps {swaps}\n")


shell_sort(generate_sorted_array(10))
bubble_sort(generate_sorted_array(10))
modified_bubble_sort(generate_sorted_array(10))

shell_sort(generate_sorted_array(100))
bubble_sort(generate_sorted_array(100))
modified_bubble_sort(generate_sorted_array(100))

shell_sort(generate_sorted_array(1000))
bubble_sort(generate_sorted_array(1000))
modified_bubble_sort(generate_sorted_array(1000))

shell_sort(generate_sorted_array(5000))
bubble_sort(generate_sorted_array(5000))
modified_bubble_sort(generate_sorted_array(5000))

shell_sort(generate_sorted_array(10000))
bubble_sort(generate_sorted_array(10000))
modified_bubble_sort(generate_sorted_array(10000))

shell_sort(generate_sorted_array(20000))
bubble_sort(generate_sorted_array(20000))
modified_bubble_sort(generate_sorted_array(20000))

shell_sort(generate_sorted_array(50000))
bubble_sort(generate_sorted_array(50000))
modified_bubble_sort(generate_sorted_array(50000))