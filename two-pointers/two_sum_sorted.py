"""
Two Sum in a Sorted Array
Link for the problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
Example: 
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Solved it in Time Complexity: O(n) and Space Complexity: O(1)
"""
# ====================================================================================================

from typing import List

class TwoSumSorted:
    """ The sum of two numbers in a sorted array and achieve O(n) time complexity and O(1) space complexity using two pointers approach."""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ The two sum of a sorted array and achieve O(n) time complexity and O(1) space complexity using two pointers approach."""
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left+=1
            elif current_sum > target:
                right-=1
            else:
                return [left+1,right+1]
        return []

# -------------------------------------------------------------------------------------------------------
numbers = [2,7,11,15]
target = 9
two_sum_sorted = TwoSumSorted()
print(two_sum_sorted.twoSum(numbers, target))  # Output: [1, 2]