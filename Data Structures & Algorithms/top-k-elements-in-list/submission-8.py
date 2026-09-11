class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for idx, num in enumerate(nums):
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        minq = []

        for num, count in counts.items():
            heapq.heappush(minq, (-count, num))
        
        result = []

        for i in range(k):
            count, num = heapq.heappop(minq)
            result.append(num)
        
        return result