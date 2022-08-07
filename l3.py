
def lengthOfLongestSubstring(self,s):
    strng = {}
    spa = 0
    lemght = 0

    for i, j in enumerate (s):
        if j in strng and spa[j] >=spa:
            spa = strng[j] + 1
        else:
            lemght = max(lemght, i - spa + 1)
        spa[j] = i

    return lemght

print(lengthOfLongestSubstring("abcabcbbb"))
