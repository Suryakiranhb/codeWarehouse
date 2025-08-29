#leader value

def leader_bruteforce(nums):
    leaders = []
    n = len(nums)
    for i in range(n):
        is_leader = True
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                is_leader = False
                break
        if is_leader:
            leaders.append(nums[i])
    return leaders

def leaderOptimal(nums):
    #we traverse from the right, and record nums. if we see it being lower than the leader element we have currently, we ignore it, else we add it to the leaders pile
    leaders = []
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
            leaders.append(nums[i])
        if nums[i] > max(leaders):
            leaders.append(nums[i])
    leaders.reverse()
    return leaders

arr = [10, 22, 12, 3, 0, 6]
ans = leaderOptimal(arr)
print(f"The leaders are: {ans}")

"""
Insight
Leaders are elements greater than all elements to their right → easiest found by traversing from the end and tracking max-so-far.
"""