# lets assumeboth arrays are a single array, and take a gap in the middle, based on which we sort by swapping elements
# from both the arrays. we keep halving the gap until we end up with 1 gap at whic point, we will have a sorted array
def mergInPlace(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    totalLen = m+n 
    gap = (totalLen//2) + (totalLen%2)
    print(gap)
    
    while gap > 0:
        pointer1 = 0
        pointer2 = gap
        while pointer2<totalLen:
            if pointer1<m and pointer2<m:
                if nums1[pointer1] > nums1[pointer2]:
                    nums1[pointer1],nums1[pointer2] = nums1[pointer2],nums1[pointer1]
            elif pointer1<m and pointer2>=m:
                if nums1[pointer1] > nums2[pointer2-m]:
                    nums1[pointer1],nums2[pointer2-m] = nums2[pointer2-m],nums1[pointer1]
            else:
                #pointer1 and pointer2 both are in n if code reaches here
                if nums2[pointer1-m] > nums2[pointer2-m]:
                    nums2[pointer1-m],nums2[pointer2-m] = nums2[pointer2-m],nums2[pointer1-m]
            pointer1+=1
            pointer2+=1
        if gap == 1:
            return
        else:
            gap = (gap//2) + (gap%2)



nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
mergInPlace(nums1,nums2)
# after calling the function above, the list nums1 should be having nums2's elements and be sorted in place.
