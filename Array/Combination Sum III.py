# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:

# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = [];
        self.com(1, k, n, [], res);
        return res;
        
        
        
    def com(self, m, k, n, tem, res):
        if k == 0 and n == 0:
                return res.append(tem)
        for i in range(m, 10):
            self.com(i+1, k-1, n-i, tem+[i], res);