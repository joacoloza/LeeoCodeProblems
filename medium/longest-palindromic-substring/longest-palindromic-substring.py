
class Solution(object):
    def longestPalindrome(self, s):
        def center_expansion(left,right):
            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) == 0:
            return ""
        
        longest = ""

        for i in range(len(s)):
            palindrome_odd = center_expansion(i,i)
            palindrome_even = center_expansion(i,i+1)
            longest = max(longest,palindrome_odd,palindrome_even, key = len)

        return longest
        """
        :type s: str
        :rtype: str
        """

#code explain
'''
center expansion expands indeed from center to the array limits
while it checks if the chars are equal, meaning it's a palindrome
so if the length its 0 it will return nothing,
return s[left+1:right], left+1 because you want to positionate again
in the array start.
Then iterates over the array and create the palindromes, and then 
later compare they length and get the longest
'''