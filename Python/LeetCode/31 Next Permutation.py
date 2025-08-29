#31. Next Permutation

def nextPermutation(nums):
    pivot = -1
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            pivot = i
            break
        #print(nums[i])
    print(f"Pivot value: {pivot}")
    # once we find the pivot value weare sure of 2 things, 
    # 1. whatever elements come after the pivot points are sorted in descending order
    # 2. By swapping the pivot with the smallest (but higher than pivot) element from the descending order list will give us the proper next permutation 
    # (that is, after we make all descending list into ascending list AFTER swapping it out with pivot) 
    if pivot == -1:
        nums.reverse()
        return nums
        # Note that if the pivot remains -1, it means that the traversal in the for loop above has reached the beginning if the list, thereby we know that the whole list is
        # sorted in descending order. If so, that order is the last permutation order. We just reverse it to get the first permutation order since nothing comes after last order, we just have to start from beginning permutation.
    
    # finding the next successor
    # Step 3: Find successor (smallest number > pivot, from right side)
    for j in range(len(nums)-1, pivot, -1):
        if nums[j] > nums[pivot]:
            nums[pivot], nums[j] = nums[j], nums[pivot]
            break

    # reversal of the descending numbers
    left = pivot+1
    right = len(nums)-1
    while(left<right):
        nums[left],nums[right] = nums[right],nums[left]
        left+=1
        right-=1
    return nums


nums = [1,3,2]
ans = nextPermutation(nums)
print(f"The next permutation would be {ans}")


#Flash card summary:
# * Pivot condition: look for nums[i] < nums[i+1] from right.
# * If pivot not found → reverse whole array.
# * Swap pivot with rightmost successor > pivot.
# * Reverse suffix after pivot.