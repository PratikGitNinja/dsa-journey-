"""
The valid palindrome problem.
Problem Link: https://leetcode.com/problems/valid-palindrome/description/
Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Solved in Time complexity: O(n) and Space complexity: O(1)
"""
# =======================================================================================================
class IsPalindrome:
    """ The class to check the string is palindrome or not."""

    def isPalindrome(self,s: str) -> bool:
        """ Check the string is palindrome or not using two pointers approach."""
        left = 0
        right = len(s) - 1
        
        while left<right:
            if not s[left].isalnum():
                left +=1
            elif not s[right].isalnum():
                right-=1
            else:
                if s[left].lower() == s[right].lower():
                    left +=1
                    right -=1
                else:
                    return False
        return True

# -------------------------------------------------------------------------------------------------------
s = "A man, a plan, a canal: Panama"
is_palindrome = IsPalindrome()
print(is_palindrome.isPalindrome(s))  # Output: True