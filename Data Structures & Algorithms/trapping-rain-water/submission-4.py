class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        for index,length in enumerate(height):
            left_max = max(height[:index], default=0)
            right_max = max(height[index + 1:], default= 0 )
            res = min(left_max,right_max)- length
            if res > 0:
                sum +=res

        return sum
                    
        