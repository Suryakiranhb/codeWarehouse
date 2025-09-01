#229 Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

#Naive aproach
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

# Optimal approach using Boyer-Moore Voting Algorithm
def majorityElementOptimal(nums):
    # since they want me to find n/2 here, the element can only appear once and be the maximum apprearing number
    number1, number2 = 0, 0
    count1, count2 = 0, 0
    
    for num in nums:
        if num == number1:
            count1 += 1
        elif num == number2:
            count2 += 1
        elif count1 == 0:
            number1, count1 = num, 1
        elif count2 == 0:
            number2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # verify counts to checking if the number truly is apearing more than n/2 times:
    answer = []
    n = len(nums)
    cnt1 = sum(1 for x in nums if x == number1)
    cnt2 = sum(1 for x in nums if x == number2)

    if cnt1 > n//3:
        answer.append(number1)
    if cnt2 > n//3 and number2!=number1: #this handles edge cases where both numbers are the same. In case of input like [0,0,0]
        answer.append(number2)

    return answer


nums = [3,2,3]
ans = majorityElementOptimal(nums)
print(ans, " is the answer")



'''
INSIGHT:
# Majority Element II (n/3) - Voting Algorithm

**Problem:** Find all elements in an array that appear more than ⌊n/3⌋ times.
Insights:
- At most **2 elements** can appear more than n/3 times.
- Use a modified **Boyer-Moore Voting Algorithm**:
  1. Maintain **two candidate numbers** (`num1`, `num2`) and their **counts** (`count1`, `count2`).
  2. Traverse the array:
     - If current number matches a candidate → increment its count.
     - Else if count of a candidate is 0 → assign current number as candidate and set count = 1.
     - Else → decrement both counts by 1.
  3. After traversal, candidates are **potential** majority elements.
  4. Verify each candidate by counting its occurrences in the array.

---

## Edge Case:

- Ensure `num1` and `num2` are **distinct** in the final answer.
- Example: `[0,0,0]` → only `0` should be in the result.

---

## Complexity:

- **Time:** O(n) → single pass + verification pass.
- **Space:** O(1) → constant space for 2 candidates and counts.

'''