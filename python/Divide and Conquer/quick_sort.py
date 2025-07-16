# Lomuto’s Partition Scheme

def lomuto_partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low,high):

        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i + 1],arr[high] = arr[high],arr[i + 1]
    return i + 1

# Hoare’s Partition Scheme (Two-Pointer)

def hoare_partition(arr, low, high):
    
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:

        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j

        arr[i],arr[j] = arr[j],arr[i]


def quick_sort_lomuto(arr, low, high):

    if low < high:
        pi = lomuto_partition(arr, low, high)
        quick_sort_lomuto(arr,low,pi - 1)
        quick_sort_lomuto(arr,pi + 1,high)

def quick_sort_hoare(arr, low, high):

    if low < high:
        pi = hoare_partition(arr, low, high)
        quick_sort_hoare(arr,low,pi)
        quick_sort_hoare(arr,pi + 1,high)

if __name__ == "__main__":
    
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quick_sort_lomuto(arr, 0, n - 1)
    
    for val in arr:
        print(val, end=" ")