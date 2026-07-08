"""
The problem is Trapping rain water.
The problem link: https://leetcode.com/problems/trapping-rain-water/
Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Solved in Time Complexity: O(n) and Space Complexity: O(1)
"""
# ================================================================================================
from typing import List

class TrappingRainWater:
    """This class contains the method to solve the problem "Trapping rain water"."""

    def trap(self, height: List[int]) -> int:
        """This method calculates the total amount of rain water that can be trapped."""
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        while left < right:
            if height[left] < height [right]:
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
                left+=1
            else:
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                right -= 1
        return water_trapped
    
# --------------------------------------------------------------------------------------------------
trapwater = TrappingRainWater()
height = [4,2,0,3,2,5]
print(trapwater.trap(height))  # Output: 9