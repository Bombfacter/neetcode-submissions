class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        

        for idx, num in enumerate(nums):
            needed = target - num

            if needed in count:
                
                return [count[needed], idx]

            else:
                count[num] = idx

            