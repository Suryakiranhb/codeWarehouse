#majority element 1

def majorityElement(nums):
    # since they want me to find n/2 here, the element can only appear once and be the maximum apprearing number
    number = 0
    count = 0
    for i in range(0,len(nums)):
        if number == 0 and count == 0:
            number = nums[i]
            count+=1
        elif nums[i] == number:
            count+=1
        else:
            count-=1
    
    #checking if the number truly is apearing more than n/2 times:
    number_counter = 0
    for i in range(0,len(nums)):
        if nums[i] == number:
            number_counter+=1
    if number_counter>(len(nums)//2):
        return number
    else:
        print(f"number {number} appears {number_counter} times. Not sure")



nums = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(nums)
print(f"The number is {ans}")