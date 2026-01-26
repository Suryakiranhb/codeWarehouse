# merge two arrays without extra space
#theres always nums2 length of space in nums1. What im thinking is we can have num1 sorted, then do insertion sort for nums2 to nums1
def inplacesort(nums1, nums2):
    nums1.sort()
    print(nums1)
    nums2.sort()
    print(nums2)
    for i in range(0,len(nums1)):
        if nums1[i] == 0:
            print("came in")
            elements = 0
            while elements < len((nums2)):
                nums1[i] = nums2[elements]
                i+=1
                elements+=1
            break
    nums1.sort()
    return nums1


nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
ans = inplacesort(nums1,nums2)
print("The merged array is: ",nums1)