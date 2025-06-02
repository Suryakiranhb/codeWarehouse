#mergesort2

def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    res = merge(left,right)
    return res

def merge(left,right):
    results = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            results.append(left[i])
            i+=1
        elif right[j] < left[i]:
            results.append(right[j])
            j+=1
        
    #now, to add the remaining elements
    results.extend(left[i:])
    results.extend(right[j:])
    return results

#sorted_array = mergesort([9, 4, 10, 7, 1])
#print("After mergesort: ",sorted_array)


### COUNT INVERSIONS

def countinversions(arr, inversion = 0):
    if len(arr)<=1:
        return arr, inversion
    
    mid = len(arr)//2
    left, left_inversions = countinversions(arr[:mid])
    right, right_inversions = countinversions(arr[mid:])
    #total_inversions = left_inversions + right_inversions
    merged_arr, merge_inversions = merge(left, right)
    return merged_arr, left_inversions+right_inversions+merge_inversions

def merge(left,right):
    merged_arr = []
    inversions = 0
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i+=1
        elif right[j] < left[i]:
            merged_arr.append(right[j])
            inversions += len(left)-i
            j+=1
        
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])
    return merged_arr , inversions

arr = [2, 4, 1, 3, 5]
sorted_arr , inversions = countinversions(arr)
print("sorted array: ",sorted_arr,"inversions: ",inversions)
