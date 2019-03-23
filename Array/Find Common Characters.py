# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  
# For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

 

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]
 

# Note:

# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        count = [1]*len(A[0])
        for i in range(len(A)-1):
            a = list(A[i+1])
            for j in range(len(A[0])):
                for k in range(len(a)):
                    if A[0][j] == a[k]:
                        count[j] += 1
                        a.pop(k)
                        break
        res = []
        for num in range(len(count)):
            if count[num] == len(A):
                res.append(A[0][num])
        return res