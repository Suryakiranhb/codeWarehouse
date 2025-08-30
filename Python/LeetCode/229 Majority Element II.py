#229 Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def majorityElement(nums):
    times = len(nums)//3
    nums.sort()
    elements = []
    counter = 1  # start from 1 because the element itself counts

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            counter += 1
        else:
            counter = 1
        if counter > times and nums[i] not in elements:
            elements.append(nums[i])

    return elements


    


nums = [3,2,3]
ans = majorityElement(nums)
print(ans, " is the answer")