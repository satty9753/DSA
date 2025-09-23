def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(i, swapped)
        if not swapped:
            break
    return arr


# numbers = [64, 34, 25, 12, 22, 11, 90]
# sorted_numbers = bubble_sort(numbers)
# print("Sorted array is:", sorted_numbers)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            print("Swapping", arr[j], arr[j+1])
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key # Insert the key at its correct position
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = insertion_sort(numbers)
print("Sorted array is:", sorted_numbers)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



