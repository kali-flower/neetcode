class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums: 
            freq[num] = 1 + freq.get(num, 0)

        heap = []
        for num in freq.keys(): 
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k: 
                heapq.heappop(heap) # if the size of the heap is larger than k, remove the smallest element 

        result = []
        for i in range(k): 
            result.append(heapq.heappop(heap)[1]) # use 1 so you can use the SECOND value of the tuple, since the first value is going to be the actual frequency (not what we want)

        return result 