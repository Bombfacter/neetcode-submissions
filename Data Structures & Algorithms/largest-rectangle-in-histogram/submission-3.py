class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        maxArea = 0

        for i in range(len(heights)):
            start = i

            while stack and heights[i] < stack[-1][1]:
                idx, height = stack.pop()
                area = height * (i - idx)
                maxArea = max(area, maxArea)

                start = idx

            stack.append((start, heights[i]))

        for idx, height in stack:
            area = height * (len(heights) - idx)
            maxArea = max(area, maxArea)

        return maxArea
