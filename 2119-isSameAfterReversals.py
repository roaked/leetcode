"""Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. 
Return true if reversed2 equals num. Otherwise return false."""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse = str(num)
        reverse = reverse[::-1]
        return True if not reverse.startswith('0') or len(reverse) == 1 else False

print(Solution().isSameAfterReversals(num = 526))
print(Solution().isSameAfterReversals(num = 1800))
print(Solution().isSameAfterReversals(num = 0))