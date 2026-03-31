class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers 
        # if sum is smaller than target, increment left
        # if sum greater, decrement right 
        # return [i + 1, j + 1], run for left < right 

        left, right = 0, len(numbers) - 1

        while left < right: 
            total = numbers[left] + numbers[right] 

            if total == target: 
                return [left + 1, right + 1]
            elif total < target: 
                left += 1
            elif total > target: 
                right -= 1
            