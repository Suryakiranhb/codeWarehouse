#239. Sliding Window Maximum

#simple, non deque solution
def maxSlidingWindow(nums, k):
    windows = []
    pointer1 = 0
    pointer2 = pointer1+k
    while(pointer2<=len(nums)):
        temp_sum = 0
        max_value = max(nums[pointer1:pointer2])
        windows.append(max_value)
        pointer1+=1
        pointer2+=1
    return windows

#solution using deque
#def maxSlidingWindowDeque(nums, k):


nums = [1,3,-1,-3,5,3,6,7]
k = 3
ans = maxSlidingWindow(nums,k)
print("the maximum sliding windows are: ",ans)