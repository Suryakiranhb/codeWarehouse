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
from collections import deque
def maxSlidingWindowDeque(nums, k):
    dq = deque()
    res = []
    for i in range(len(nums)):
        # 1. removing the first deque element if its outside window scope k:
        # note that i-k here is what's covering the window aspect of this code. 
        if dq and dq[0] <= i-k:
            dq.popleft()
        
        # 2. removing all smaller elements from the back of the deque
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 3. add the current element's index to the deque
        dq.append(i)

        # 4. If we have a full window now, we just gotta append the max to the result (we are recording the max)
        if i >= k-1:
            res.append(nums[dq[0]])

    return res
        


nums = [1,3,-1,-3,5,3,6,7]
k = 3
ans = maxSlidingWindowDeque(nums,k)
print("the maximum sliding windows are: ",ans)