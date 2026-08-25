class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = []
        maxRight = []
        counter = 0

        curLeft = 0
        curRight = 0

        for i in range(len(height)): 

            if(height[i] > curLeft):
                curLeft = height[i]
            maxLeft.append(curLeft)
            
        for i in range(len(height) - 1, -1, -1):
            if(height[i] > curRight):
                curRight = height[i]
            maxRight.append(curRight)
        maxRight.reverse()

        for i in range(len(height)):
            counter += min(maxLeft[i], maxRight[i]) -height[i]

        return counter
