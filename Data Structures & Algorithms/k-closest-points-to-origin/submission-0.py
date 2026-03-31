class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = [] # initialize the heap 

        for x, y in points: 
            distance = (x**2) + (y**2)
            heap.append([distance, x, y])

        heapq.heapify(heap) # this reorders the heap we made based on 1st val
        while k > 0: 
            distance, x, y = heapq.heappop(heap) # get 3 values 
            result.append([x, y])
            k -= 1 

        return result 