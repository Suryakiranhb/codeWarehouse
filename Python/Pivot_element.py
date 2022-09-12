class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        revsum = 0
        forsum = 0
        for i in range(0,len(nums)):
            revsum+=nums[i]
        
        for i in range(0,len(nums)):
            revsum = revsum - nums[i]
            if (revsum == forsum):
                return i
                break
            else:
                forsum+=nums[i]
        
        return(-1)    
      
      #Example testcases
      #[1,7,3,6,5,6]
      #[1,2,3]
      #[2,1,-1]
