class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            index = abs(x) - 1
            if nums[index] < 1:
                # print(f'found {x=}')
                res.append(abs(x))
            else:
                nums[index] =  -nums[index]
            # print(nums)
        return res
         
    :
