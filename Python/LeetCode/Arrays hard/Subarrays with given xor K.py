# XOR is done by a ^ b. this converts a and b integers into binary and then adds them 
def xorBruteforce(arr,k):
    xorDict = {}
    count = 0
    for i in range(0,len(arr)-1):
        xors = arr[i]
        xors = 0
        for j in range(i,len(arr)):
            xors^=arr[j]
            if xors == k:
                count+=1
    return count

## LOGIC ##
'''
works on the basis of "at each index, I count how many previous prefix XORs would produce K if XORed with my current prefix." 
like, basically, we can do 'wanted number' XOR 'number we have' to get the 'number that we wannna XOR' to the 
'number we already have' to get the 'wanted number'

math:
we 6 right? since thats K.
lets say by doing arr[0]^arr[1] we get the XOR answer x.
now, what do we xor to x to get K? 
we get that by the operation: x^6 = number to XOR 
X^number to XOR = 6

We store this in a dictionary, and ask it hey, this number to XOR, is it there in dict? 
if so, how many times? and increase count using that. Final count is the number of subarrays.
'''
def xorDict(arr, K):
    xorDict = {0: 1}
    prefixXor = 0
    count = 0

    for num in arr:
        # math part:
        prefixXor ^= num
        needed = prefixXor ^ K

        if needed in xorDict:
            count += xorDict.get(needed)

        xorDict[prefixXor] = xorDict.get(prefixXor, 0) + 1
        # the above line essentially means:
        # current_count = xorDict.get(prefixXor, 0)
        # new_count = current_count + 1
        # xorDict[prefixXor] = new_count


    return count


arr = [4, 2, 2, 6, 4] 
k = 6
ans = xorDict(arr,k)
print(f"There are {ans} subarrays which xor to {k}")