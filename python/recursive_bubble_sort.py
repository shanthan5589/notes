# Recursive Bubble Sort

arr = [int(x) for x in input().split()]

length = len(arr)

def bubble(i,end,arr):

    if end == 0:
        return arr
    elif i > end:
        return bubble(1,end-1,arr)
    else:
        if arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
        return bubble(i+1,end,arr)

print(bubble(1,length-1,arr))