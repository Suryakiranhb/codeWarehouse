#128. Longest Consecutive Sequence

# O(n log n) approach using set
def longestConsecutive(nums):
    if not nums:
        return 0
    #making nums into a sorted set to eliminate duplicates and to make it sorted
    nums = sorted(set(nums))
    print(nums)
    #num_set.sort()
    longest  =1 
    current = 1
    for i in range(1,len(nums)):
        #checking sequence order, if ith is +1 of i-1 or not,
        if nums[i] == nums[i-1] + 1:
            current+=1
            longest = max(longest, current)
        else:
            #if we encounter ith element smaller than i-1th element, we reset the current length counter and start again
            current = 1 
    return longest

"""
Intuition:
Traverse sorted array.
If i is consecutive with i-1, extend sequence.
If equal, skip (since we used set(), this case disappears anyway)
If bigger gap, reset.
"""

# O(n) approach
def longestConsecutiveHashsetApproach(nums):
    nums_hashset = set(nums)
    longest = 0
    for num in nums_hashset:
        # we only go further if num does not have any num-1 in nums
        if num-1 not in nums_hashset:
            length = 1
            while num+length in nums_hashset:
                length+=1
            longest = max(longest,length)
    return longest

'''
Why this is better:
Every sequence gets explored once (from its starting number).
No duplicate numbers → no redundant work.
Each number is checked at most twice → O(n) runtime.
'''

nums = [100,4,200,1,3,2]
ans = longestConsecutiveHashsetApproach(nums)
print(f"The longest consecutive is {ans}")


'''
Steps
1. Traverse from left to right
2. We check if ith element is +1 higher than i-1 element
3. If so, it is the next consecutive element. Increase the counter and the 
'''