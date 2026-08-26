class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = {}
        
        for i, num in enumerate(nums):
            needed = target - num

            if needed in count:
                return [min(i, count[needed]), max(i, count[needed])]

            count[num] = i

            




            

            