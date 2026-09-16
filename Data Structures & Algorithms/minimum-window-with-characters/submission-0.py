class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        needMap = {}
        for char in t:
            needMap[char] = needMap.get(char, 0) + 1

        windowMap = {}

        need = len(needMap)
        have = 0
        left = 0

        minWindowLength = float("inf")
        leftIndex = 0
        rightIndex = 0

        for right in range(len(s)):
            if s[right] in needMap:
                windowMap[s[right]] = windowMap.get(s[right], 0) + 1

                if windowMap[s[right]] == needMap[s[right]]:
                    have += 1

            while have == need:
                windowLength = right - left + 1

                if windowLength < minWindowLength:
                    minWindowLength = windowLength
                    leftIndex = left
                    rightIndex = right

                if s[left] in needMap:
                    windowMap[s[left]] -= 1

                    if windowMap[s[left]] < needMap[s[left]]:
                        have -= 1

                left += 1

        if minWindowLength == float("inf"):
            return ""

        return s[leftIndex:rightIndex + 1]