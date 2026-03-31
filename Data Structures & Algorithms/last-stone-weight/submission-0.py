class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: # do this while we have 1 or 0 stones left in the heap 
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first: # if we have -8 and -7, then -7 - (-8) = 1, and negate it
                heapq.heappush(stones, -(second - first))

        # if we destroyed all the stones, we still want to return something
        stones.append(0)
        return abs(stones[0])