class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hm1 = {}
        hm2 = {}
        left = 0

        windowSize = len(s1)

        for i in range(windowSize):
            hm1[s1[i]] = hm1.get(s1[i], 0) +1
            hm2[s2[i]] = hm2.get(s2[i], 0) +1

        if hm1 == hm2:
            return True

        for right in range(windowSize, len(s2)):
            hm2[s2[left]] -= 1
            if hm2[s2[left]] == 0:
                del hm2[s2[left]]

            left += 1
            hm2[s2[right]] = hm2.get(s2[right], 0) + 1

            if hm1 == hm2:
                return True


        return False

            
            

            