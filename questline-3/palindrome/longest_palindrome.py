def isPalindrome(s):
    return s == s[::-1]

def longestPalindrome(s):
    maxLen = 0
    longest = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if isPalindrome(sub):
                if len(sub) > maxLen:
                    maxLen = len(sub)
                    longest = sub
    return longest

inputString = input("Enter a string: ")
result = longestPalindrome(inputString)
print("Longest Palindromic Substring is:", result)
