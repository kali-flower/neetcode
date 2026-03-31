class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        area = l x w --> distance between 2 pointers * smaller height 
        start at ends --> biggest area could be between ends 
        update area --> result = max(result, area)
        change the SMALLER value (bottleneck)
        move towards the middle --> while left < right 
        return result
        '''
        left, right = 0, len(heights) - 1
        result = 0 

        while left < right: 
            area = (right - left) * min(heights[left], heights[right])
            result = max(area, result)

            if heights[right] <= heights[left]: 
                right -= 1
            else: 
                left += 1

        return result 
        