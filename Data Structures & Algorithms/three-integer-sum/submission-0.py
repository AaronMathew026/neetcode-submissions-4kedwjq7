class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()

        for index, val in enumerate(nums):
            if index > 0 and val ==nums[index-1]:
                continue
            left = index+ 1
            right = len(nums) -1
            while left < right:
                threesum = val + nums[left] + nums[right]
                if threesum > 0:
                    right -=1
                elif threesum < 0:
                    left +=1
                else:
                    res.append([val,nums[left],nums[right]])
                    left +=1
                    while nums[left] == nums[left- 1] and left < right:
                        left +=1

        return res



        