class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]
        #print(output)
        
        p = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i]*p
            p *= nums[i]
        return output
