def mergesort(arr, low, high):
    #NOTE that we are dealing with array indexes here, not the array elements themselves. 
    # so low = 0, high = len(arr)-1 
    if low >= high:
        return
    else:
        mid = (low+high)//2
        # the above is floor division, eliminates decimal places directly instead of converting float to int with-> mid = int((low + high)/2)
        print("Mid position is: ",mid)
        print("passing to mergesort()->1. low, mid are as follows: ",low , mid)
        mergesort(arr,low,mid)
        print("baCK FROM RECURSION mergesort 1, low, mid and high are as follows: ",low , mid , high)
        print("passing to mergesort()->2. low, mid+1 are as follows: ",low , mid+1)
        mergesort(arr,mid+1,high)
        print("baCK FROM RECURSION mergesort 2, low, mid and high are as follows: ",low , mid , high)
        #return
        print("merge gets passed: ",arr,low,mid,high)
        merge(arr,low,mid,high)

#KEY FACTOR: The recursions for both sides dont happen simultaneously. The side A gets sorted fully, then side B gets sorted fully, 
# and THEN the merge happens. This goes all the way down left first gets sorted then right array even when its only 1 1 element in 
# the range taken for left array and right array

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1
    # we have two halves, one is low to mid, the other is mid+1 to high
    while left<=mid and right <=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
        #we are checking if left is lesser value than right (if so, its sorted)
        #and we append left one to the temp array. We then increment the left pointer.
        #else, it means that left array is greater than the right array, so
        #we append the right element to the temp array. We then increment the right pointer
    
    #in case there are left out elements from the left half, we append those to the temp (they are already sorted anyway)
    while left<=mid:
        temp.append(arr[left])
        left+=1
    
    #in case there are left out elements from the right half, we append those to the temp (they are already sorted anyway)
    while right<=high:
        temp.append(arr[right])
        right+=1
    
    #now inserting from temp array into the original array
    for i in range(low,high+1):
        arr[i] = temp[i-low]



arr = [9, 4, 7, 6, 3, 1, 5]
mergesort(arr, 0 , len(arr)-1)
print("The final array after merge sort will be : ",arr)