class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # counts how many times each thing occurs 
        freq = [[] for i in range(len(nums) + 1)] # index = counts of element, values = which elements appear that many times 
        # ^ empty array of empty arrays 

        for num in nums: 
            counts[num] = 1 + counts.get(num, 0)

        for num, count in counts.items(): # return every single key-val pair    
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1): 
            for val in freq[i]: 
                result.append(val)
                if len(result) == k: 
                    return result 