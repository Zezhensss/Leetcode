# Given an array nums of n integers where n > 1,  return an array output such 
# that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums);
        a = 1;
        for k, v in enumerate(nums):
            res[k] *= a;
            a *= v;
        a = 1;
        for k, v in enumerate(nums[::-1]):
            res[~k] *= a;
            a *= v;
        return res
            