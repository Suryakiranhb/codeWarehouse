#217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Hashmap tutorial basically
def containsDuplicate(nums):
    hashset = {}
    results = []
    for num in nums:
        hashset[num] = hashset.get(num,0)+1
        # The above can also be done with: hashset[nun]+=1 but this will not work if num isnt already in the hashset. The line above adds a deafault 0 if its not there already
    print("Hashset: ",hashset)
    for key,value in hashset.items():
        if value>=2:
            results.append(key)
    return results

nums = [1,2,3,1]
ans = containsDuplicate(nums)
print("The results are: ",ans)