# Recursive Insertion Sort

arr = [int(x) for x in input().split()]

n = len(arr)

def insertion(key,key_index,search_index,arr,n):

    if key_index == n:
        return arr
    elif search_index == -1:
        arr[search_index + 1] = key
        if key_index + 1 != n:
            key_index += 1
            key = arr[key_index]
            search_index = key_index - 1
            return insertion(key,key_index,search_index,arr,n)
        else:
            return arr
    elif key <= arr[search_index]:
        arr[search_index + 1] = arr[search_index]
        return insertion(key,key_index,search_index-1,arr,n)
    elif key > arr[search_index]:
        arr[search_index + 1] = key
        if key_index + 1 != n:
            key_index += 1
            key = arr[key_index]
            search_index = key_index - 1
            return insertion(key,key_index,search_index,arr,n)
        else:
            return arr

print(insertion(arr[1],1,0,arr,n))