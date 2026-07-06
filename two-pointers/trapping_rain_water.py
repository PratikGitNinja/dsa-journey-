"""
The problem is Trapping rain water.
The problem link: https://leetcode.com/problems/trapping-rain-water/
Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""

from typing import List

class TrappingRainWater:
    """This class contains the method to solve the problem "Trapping rain water"."""

    def trap(self, height: List[int]) -> int:
        """This method calculates the total amount of rain water that can be trapped."""
        
        