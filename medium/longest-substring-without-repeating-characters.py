class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxN = 0
       
        for index,char in enumerate(s):
            auxN = 1
            auxI = index + 1 
            seen_chars = set(char) #if a num is in here it's probably repeating
            
            while ((auxI < len(s)) and (s[auxI] not in seen_chars)):
                seen_chars.add(s[auxI])
                auxN += 1
                auxI += 1

            if (auxN > maxN):
                maxN = auxN
        
        return maxN
        """
        :type s: str
        :rtype: int
        """
# it could be a better version