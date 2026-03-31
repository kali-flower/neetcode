class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        result = lists of anagrams 
        each list needs to hold anagrams

        how to find anagrams? grouping after sorting 
        same letters --> same after sorting 
        use sorted version as a key, value will be the unsorted version 
        use defaultfict of lists 
        '''

        result = defaultdict(list)

        for word in strs: 
            w_sorted = ''.join(sorted(word))
            result[w_sorted].append(word)

        return result.values() # might b wrong 