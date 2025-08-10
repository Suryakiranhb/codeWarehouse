# 167. Two current_sum II - Input Array Is Sorted

# brute force 
def two_current_sum(numbers, target):
    pointer1 = 0
    pointer2 = len(numbers)-1
    for i in range(0, len(numbers)):
        for j in range(i,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i+1,j+1


#2 pointer
def two_current_sum_2pointer(numbers,target):
    pointer1 = 0
    pointer2 = len(numbers)-1
    while(pointer1<pointer2 and pointer1,pointer2<len(numbers)):
        current_sum = numbers[pointer1]+numbers[pointer2]
        print("pointer1: ",pointer1, " Pointer2: ",pointer2, " current_sum = ",current_sum)
        if current_sum == target:
            return pointer1+1, pointer2+1
        elif current_sum>target:
            pointer2-=1
        elif current_sum<target:
            pointer1+=1
    return -1



numbers = [2,7,11,15]
target = 9
pointer1, pointer2  = two_current_sum_2pointer(numbers, target)
print(f"Answer is to add numbers {numbers[pointer1]} and {numbers[pointer2]}")


# Takeaway:
# Start at the ends, move the pointer that makes the sum closer to the target.