class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lowercased = s.lower()
        print(lowercased)
        alphanumeric = [char for char in lowercased if char.isalnum()]
        reversed = alphanumeric[::-1]
        if reversed == alphanumeric:
            return True
        else:
            return False
        