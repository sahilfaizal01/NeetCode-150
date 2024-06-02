class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for string in strs:
            count = [0] * 26 # a to z

            for c in string:
                count[ord(c) - ord('a')] += 1
            
            hashMap[tuple(count)].append(string)
        
        return hashMap.values()
