class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLength = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            windowSize = right - left + 1
            maxFreq = max(count.values())
            replacements = windowSize - maxFreq

            while replacements > k:
                count[s[left]] -= 1
                left += 1

                windowSize = right - left + 1
                maxFreq = max(count.values())
                replacements = windowSize - maxFreq

            maxLength = max(maxLength, windowSize)

        return maxLength