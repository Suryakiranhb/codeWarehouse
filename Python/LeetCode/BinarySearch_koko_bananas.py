import math

def valid_checker(speed, piles, hours_alotted):
    # Checking if Koko can finish all piles at this speed within allotted hours
    total_hours = sum(math.ceil(p/speed) for p in piles)
    print(f"velocity for {speed} is {total_hours}")
    return total_hours <= hours_alotted

def binary_search(piles, hours_alotted):
    low, high = 1, max(piles)  #possible speed range
    while low < high:
        mid = (low + high) // 2
        print(mid)
        if valid_checker(mid, piles, hours_alotted):
            high = mid  # mid is valid, try smaller speeds
        else:
            low = mid + 1  #mid too slow, need higher speed
    return low  # minimum valid speed

piles = [30,11,23,4,20]
hours_alotted = 6
ans = binary_search(piles, hours_alotted)
print(f"The minimum valid speed is: {ans}")


#print(nums)
#results = []

# Binary search utilized to search nums instead

'''
# Brute force approach
for number in nums:
    res = valid_checker(piles, number)
    if res:
        results.append(number)
'''
        
#print("These are all the valid ones: ",results)
#print("The minimum valid one is : ", min(results))
#print(f"ans is the position: {ans}")


