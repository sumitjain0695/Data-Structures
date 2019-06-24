def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while arr[high] != arr[low] and key >= arr[low] and key <= arr[high]:
        mid = int(low + ((key - arr[low]) * (high - low) / (arr[high] - arr[low])))

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
arr = [2, 4, 6, 8, 10, 12, 14, 16]
find=int(input())
print(interpolation_search(arr, find))
