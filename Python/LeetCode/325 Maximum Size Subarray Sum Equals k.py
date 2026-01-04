def largest_subarray(arr, target):
    
    temp_sum = 0
    for i in range(0,len(arr)):
        temp_sum += arr[i]
        for j in range(i+1,len(arr)):
            temp_sum+=arr[j]




Input =   [15, -2, 2, -8, 1, 7, 10, 23]
target = 5
