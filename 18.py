#Write python program using function to sort a series of numbers using either
#insertion sort or bubble sort.

def bubbleSort(arr):
    n = len(arr)
    swap = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap:
            return
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is: ")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")