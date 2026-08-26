class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = defaultdict(list)
        
        for s in strs:
            index = "".join(sorted(s))
            table[index].append(s)

        return list(table.values())



        