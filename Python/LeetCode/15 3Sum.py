#3sum
def threeSum(nums):
    # 2 pointers, we first sort nums and then use 2 pointers to know if we get 0 after adding 3 numbers. if so, we append those 3 numbers to the list, and return it.
    nums.sort()
    print(nums)
    answers = []
    for i in range(0,len(nums)-2):
        #skipping dupes for i
        if i>0 and nums[i] == nums[i-1]:
            continue
        pointer1 = i+1
        pointer2 = len(nums)-1
        while pointer1<pointer2:
            print(f"pointer1:{pointer1}, pointer2:{pointer2}")
            addition = nums[i]+nums[pointer1]+nums[pointer2]
            if addition == 0:
                answers.append([nums[i],nums[pointer1],nums[pointer2]])
            #skipping dupes for pointers 1 and 2
                # skip dupes for pointer1
                while pointer1 < pointer2 and nums[pointer1] == nums[pointer1+1]:
                    pointer1 += 1
                # skip dupes for pointer2
                while pointer1 < pointer2 and nums[pointer2] == nums[pointer2-1]:
                    pointer2 -= 1          
                pointer1 += 1
                pointer2 -= 1            
            elif addition < 0:
                pointer1 += 1
            else:
                pointer2 -= 1
    return answers
            

nums = [-1,0,1,2,-1,-4]
ans = threeSum(nums)
print(f"All the combinations that result in a 0 is {ans}")


'''
INSIGHTS:
1. Problem Restatement
Find all unique triplets in an array that sum to 0.
Output should not contain duplicate triplets.

2. Key Ideas
Sorting simplifies the problem:
We can use two pointers instead of nested loops.
Sorting helps in skipping duplicates easily.
Two-pointer technique:
Fix one number (nums[i]).
Use two pointers (left, right) to find pairs that sum to -nums[i].
Skipping duplicates is critical:
For the main loop: skip if nums[i] == nums[i-1].
For two pointers: after finding a valid triplet, move both pointers past duplicates.

3. Complexity
Sorting: O(n log n)
Two-pointer sweep: O(n^2)
Total: O(n^2), which is optimal.

4. Edge Cases
Multiple zeros: e.g., [0,0,0,0] → output [0,0,0] only once.
No solution: return [].
Negative & positive mix: [1,-1,-1,0] → [[-1,0,1]].

5. Example Walkthrough
Input: [-1, 0, 1, 2, -1, -4]
Sorted: [-4, -1, -1, 0, 1, 2]
i=0 (-4) → look for 4 with two pointers → none.
i=1 (-1) →
[-1, -1, 2] ✅
[-1, 0, 1] ✅
i=2 (-1) skipped (duplicate).
i=3 (0) → nothing new.
Final: [[-1,-1,2],[-1,0,1]].
'''