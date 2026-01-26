# here we need to find the number in the array that appears twice and also find the number that is missing. numbers in nums are 1 to n
# just put them all in a dictionary. At the end, see which element appears 0 times and which number appears 2 times

# O(n logn) space taking solution:
def findRepeatsMisses(nums):
    repeat = 0
    missing = 0
    # creating a dict to store all occurances
    numberlog = {}
    for i in nums:
        if i in numberlog:
            numberlog[i] +=1 
        else:
            numberlog[i] = 1
    #print(numberlog)
    #maxElement = nums[-1]

    #finding missing element using dict
    for i in range(1,len(nums)+1):
        if i in numberlog:
            continue
        else:
            missing = i

    #finding repeat number using dict
    for key,value in numberlog.items():
        if value == 2:
            repeat = key

    return [repeat,missing]

# Optimal XOR based solution
def findRepeatsMissesXOR(nums):
    xorall = 0
    for num in nums:
        xorall^=num
    for i in range(1,len(nums)+1):
        xorall^=i
    print(xorall)


nums = [3, 5, 4, 1, 1]
ans = findRepeatsMissesXOR(nums)
print("The repeating number and the duplicate are: ",ans)