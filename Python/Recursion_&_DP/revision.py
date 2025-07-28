# Revision

# sliding window revision (fixed size window)

def sliding_window_fixed_size(arr, k):
    max_sum = curr_sum = sum(arr[:k])
    i_value = 0
    k_value = k
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k]
        #here i-k will be the window. as i increases, we subtract the element k-length before i. In this case, its 3 length before i
        #then we find the max. If current sum is greater than the max sum we calculated earlier, we update the max sum and continue till we reach the end
        max_sum = max(curr_sum,max_sum)
        if max_sum == curr_sum:
            i_value = i
            k_value = i-k
    return max_sum, i_value, k_value

arr = [2, 1, 5, 1, 3, 2]
k = 3
biggest_subarray_of_size_k, till_here, from_here = sliding_window_fixed_size(arr,k)
print("Biggest subarray of size k: ",biggest_subarray_of_size_k)
print("The biggest subarray of size ",k," will be from ",from_here," till ",till_here)
