class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = {}

        for num in nums:
            if num in array:
                return True
            array[num] = 1

        return False
            