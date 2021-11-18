import re

class Solution:
    def isPalindrome(self, s):
        s = re.sub(r'[\W_]+', '', s)
        string_length = len(s)
        if string_length < 2:
            return True

        s = s.lower()
        first_half = s[0:string_length//2]
        if string_length % 2 == 0:
            second_half = s[string_length // 2:string_length]
        else:
            second_half = s[(string_length // 2) + 1:string_length]

        #print(s)
        second_half = second_half[::-1]

        return first_half == second_half


if __name__ == '__main__':
    s =  Solution()
    test = "A man, a plan, a canal: Panama"
    test = "race a car"
    test = " "
    test = "MiiM"
    test = "ab_a"
    ans = s.isPalindrome(test)
    print(ans)