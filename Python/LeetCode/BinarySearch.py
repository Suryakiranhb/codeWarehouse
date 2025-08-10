# 704. Binary Search
# https://leetcode.com/problems/binary-search/

def binary_search(nums, target ):
    nums.sort()
    print(nums)
    #sorting done, now to set pointers
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return -1



nums = [-1, 0, 3, 5, 9, 12]
target = 9
ans = binary_search(nums, target)
print("Got the ans as: ",ans)

#explainer:
""" 
Two pointers — cover the search space (low and high).

While space is valid (low <= high):

    Midpoint check — found → return.

    If target bigger → throw away left half (low = mid + 1).

    If target smaller → throw away right half (high = mid - 1).

Not found → -1.
"""