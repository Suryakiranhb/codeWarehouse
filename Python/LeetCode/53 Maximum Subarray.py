#53. Maximum Subarray

def maxSubArray(nums):
    current_sum =max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum,current_sum)
    return max_sum

    """
    max = 0
    tally = nums[0]
    pointer1 = 0
    pointer2 = 1
    while pointer1<len(nums)-1 and pointer2<len(nums)-1:
        max = tally
        tally+=pointer2
        if tally<=0:
            
            pointer1 = pointer2
            pointer2+=1
        else:
            pointer2+=1
    """




nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = maxSubArray(nums)
print(f"The max subarray would sum up to {ans} ")