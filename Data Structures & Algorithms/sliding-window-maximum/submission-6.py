from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        left = 0

        for right in range(len(nums)):
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()

            dq.append(right)

            left = right - k + 1
            if dq and (dq[0] < left):
                dq.popleft()

            if right >= k - 1:
                result.append(nums[dq[0]])

        return result
            