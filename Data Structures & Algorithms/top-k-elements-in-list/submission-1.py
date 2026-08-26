import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        l = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, frequency in count.items():
            l.append((-frequency, num))

        heapq.heapify(l)

        result = []

        for i in range(k):
            pair = heapq.heappop(l)
            result.append(pair[1])


        return result


        