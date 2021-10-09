from typing import List

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
        
        print('-----------')
        # TODO: STOP criteria here
        for k in range(max(len(matrix[0]), bottom), 0, -1):
            print(top, bottom, left, right)
            if bottom >= 0:
                for i in range(left, right+1):
                    res.append(matrix[top][i]) # 123
            # print(res, 'topdone')
            for j in range(top+1, bottom+1):
                res.append(matrix[j][right]) #  69
            # print(res, 'rightdone')
            if bottom != top:
                for i in range(right-1, left-1, -1):  # 87
                    res.append(matrix[bottom][i])
            # print(res, 'bottomdone')
            if left != right:
                for j in range(bottom-1, top+1-1, -1): # 4
                    res.append(matrix[j][left])
            print(res, 'leftdone')
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return res

s = Solution()
            
def test_x():
    m = [[1]]
    assert s.spiralOrder(m) == [1]

def test_y():
    m = [[1,2,3],[4,5,6],[7,8,9]]
    assert s.spiralOrder(m) == [1,2,3,6,9,8,7,4,5]
        
def test_z():
    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    assert s.spiralOrder(m) ==  [1,2,3,4,8,12,11,10,9,5,6,7]

def test_4():
    m = [[6,9,7]]
    assert s.spiralOrder(m) ==  [6,9,7]

def test_5():
    m = [[1],[2],[3]]
    assert s.spiralOrder(m) ==  [1,2,3]


def test_6():
    m = [[2,5,8],[4,0,-1]]
    assert s.spiralOrder(m) == [2,5,8,-1,0,4]

            
# https://leetcode.com/problems/spiral-matrix/ 

# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [[1]]
# [1]
