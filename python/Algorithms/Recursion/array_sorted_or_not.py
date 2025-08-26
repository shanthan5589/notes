# Check if given array is sorted on not
# 2 -> Simplified version --> same logic 

def sorted1(arr,n):
    if n == 1:
        return True
    elif arr[n-1] < arr[n-2]:
        return False
    else:
        return sorted(arr,n-1)
    
def sorted2(arr,n):
    if n == 1:
        return True
    return arr[n-1] >= arr[n-2] and sorted(arr,n-1)


a = [int(x) for x in input().split()]
print(sorted(a,len(a)))