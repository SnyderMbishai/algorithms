"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if "" in strs:
            return ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0][0]
        
        
        mn_word = min(strs, key=len)
        lngst = ""

        for i in range(len(mn_word)):
            lst = [mn_word[:i+1] == word[:i+1] for word in strs]
            if False in lst:
                if i == 0:
                    return ""
                return mn_word[:i]
            lngst = mn_word[:i+1]
        return lngst
    
    def longestCommonPrefix2(self, strs):
        if "" in strs or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0][0]
        
        lngst_idx = ""

        for i in range(len(min(strs, key=len))):
            for word in strs:
                if strs[0][:i+1] != word[:i+1]:
                    if i == 0:
                        return ""
                    return strs[0][:i]
            lngst_idx = i 
        return strs[0][:lngst_idx+1]
            
        
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix2(["flower","flow","flight"]))