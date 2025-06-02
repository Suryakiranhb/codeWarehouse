# SUBSETS

def subset(arr):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start,len(arr)):
            path.append(arr[i])
            backtrack(i+1,path)
            path.pop()

    backtrack(0,[])
    return result

subsets = subset([1,2,3])
print("Subsets are: ",subsets)



#SUBSETS _own
def subset_helper(arr):
    all_subsets = []
    def backtrack(start,subarray):
        all_subsets.append(subarray[:])
        for i in range(start, len(arr)):
            subarray.append(arr[i])
            backtrack(i+1,subarray)
            subarray.pop()
    
    backtrack(0,[])
    return all_subsets

all_subsets = subset_helper([1,2,3])
print("Subsets: ",all_subsets)


### PERMUTATIONS

def permutations(nums):
    result = []
    nums.sort()
    validator = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if validator[i] == True:
                continue
            if i>0 and nums[i] == nums[i-1] and validator[i-1] == False:
                continue
            path.append(nums[i])
            backtrack(path)
            path.pop()
            validator[i] = False
    
    backtrack([])
    return result

perms = permutations([1,1,3])
print("The permutations are: ",perms)
    