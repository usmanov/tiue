def bubbleSort(arr):
    n = len(arr)

    # Пройдите по всем элементам массива / Traverse through all array elements
    for i in range(n):

        # Последние элементы i уже на месте / Last i elements are already in place
        for j in range(0, n - i - 1):

            # Пересечь массив от 0 до n-i-1 / traverse the array from 0 to n-i-1
            # Поменять местами, если найденный элемент больше / Swap if the element found is greater
            # Чем следующий элемент / than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Код драйвера для тестирования выше / Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])