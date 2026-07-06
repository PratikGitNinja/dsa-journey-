"""
The problem is "Container With Most Water".
The problem link: https://leetcode.com/problems/container-with-most-water/description/
Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Solved in Time complexity: O(n) and spae complexity: O(1)
"""
# ============================================================================================
from typing import List

class MostWater:
    """This class contains the method to solve the problem "Container With Most Water"."""

    def maxArea(self, height: List[int]) -> int:
        """This method calculates the maximum area of water that can be contained."""
        maxarea = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxarea = max(maxarea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

# -------------------------------------------------------------------------------------------
height = [1,8,6,2,5,4,8,3,7]
solution = MostWater()
print(solution.maxArea(height))  # Output: 49