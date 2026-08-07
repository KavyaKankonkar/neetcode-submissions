class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i,num in enumerate(nums):
            digit=(target-num)
            if digit in num_map:
                return [num_map[digit],i]
            else:
                num_map[num]=i

