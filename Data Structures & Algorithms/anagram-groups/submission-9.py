class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord not in groups:
                groups[sortedWord] = []

            groups[sortedWord].append(word)

        return list(groups.values())