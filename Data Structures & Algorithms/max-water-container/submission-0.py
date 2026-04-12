class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) -1
        sum = 0
        while left_pointer < right_pointer:
            new_sum = min(heights[left_pointer],heights[right_pointer]) * (right_pointer - left_pointer)
            if new_sum > sum :
                sum = new_sum
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer +=1
            else:
                right_pointer -=1

        return sum


            


            


        