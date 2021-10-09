
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        left = 0
        if len(matrix) == 0:
            return res
        if len(matrix[0]) == 0:
            return res
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        
        for k in range(min(len(matrix[0]), bottom), 0, -1):
            print(top, bottom, left, right)
            for i in range(left, right+1):
                res.append(matrix[top][i]) # 123
            for j in range(top+1, bottom+1):
                res.append(matrix[j][right]) #  69
            for i in range(right-1, left-1, -1):  # 87
                res.append(matrix[bottom][i])
            for j in range(bottom-1, top+1-1, -1): # 4
                res.append(matrix[j][left])
            print(res, 'done')
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res
            
# https://leetcode.com/problems/spiral-matrix/ 
