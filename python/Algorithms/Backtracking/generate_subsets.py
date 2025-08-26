def printSubsets(arr,ans,i):
    
    if i == len(arr):
        print(ans)
        return 
    
    # include
    ans.append(arr[i])
    printSubsets(arr,ans,i+1)

    ans.pop()                   # backtrack
    printSubsets(arr,ans,i+1)   # exclude 



if __name__ == '__main__':

    arr = [1,2,3]
    ans = []

    printSubsets(arr,ans,0)