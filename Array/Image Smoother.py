# Given a 2D integer matrix M representing the gray scale of an image, 
# you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. 
# If a cell has less than 8 surrounding cells, then use as many as you can.

# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row = len(M[0]);
        col = len(M);
        ans = [[0] * row for _ in M]
        for i in range(0, col):
            for j in range(0, row):
                a = 0;
                n = 0;
                for ti in (i-1, i, i+1):
                    for tj in (j-1, j, j+1):
                        if 0 <= ti < len(M) and 0 <= tj < len(M[0]):
                            a, n = a + M[ti][tj], n + 1
                ans[i][j] = a//n;
        return ans