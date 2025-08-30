#560 Subarray Sum Equals K

#as you know, brute forcing this would just be traversing this array and using every element with every other element to figure out how many 
def subarraySum(nums,k):
    matches = 0
    for i in range(0,len(nums)):
        sum_counter=0
        for j in range(i, len(nums)):
            sum_counter+=nums[j]
            if sum_counter == k:
                matches+=1
    return matches

# Optimized approach - using prefix sum
def subarraySumOptimal(nums, k):
    hashmap_store = {0:1}
    prefix_sum = 0
    count = 0
    for i in range(0,len(nums)):
        prefix_sum+=nums[i]
        if prefix_sum - k in hashmap_store:
            count+= hashmap_store[prefix_sum - k]
        hashmap_store[prefix_sum] = hashmap_store.get(prefix_sum,0)+1
    return count

'''
INSIGHT:
Time = O(n), Space = O(n).
This is the optimal solution.

Subarray sums = difference of two prefix sums.
Store prefix sums in hashmap while traversing.
Check prefix - k instead of recomputing subarrays.
'''
        
nums = [1,2,3]
k = 3
ans = subarraySumOptimal(nums,k)
print("The subarrays equal to sum that can be formed are: ",ans)

