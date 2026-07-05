"""
The Sum of three integers problem.
The Problem Link: https://leetcode.com/problems/3sum/description/
Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Solved in Time Complexity: O(n^2) and Space Complexity: O(n)
"""
# =======================================================================================================


class ThreeSum:
    """ The class to find the sum of three integers in an array."""

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """The function to find the sum of three integers in an array."""
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1

                    while left < right  and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif current_sum < 0:
                    left+=1
                else:
                    right-=1
        return result


# -------------------------------------------------------------------------------------------------------
nums = [-1,0,1,2,-1,-4]
three_sum = ThreeSum()
print(three_sum.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]