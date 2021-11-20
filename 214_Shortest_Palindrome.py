class Solution:
    def isNotPalindrome(self, s):
        return s != s[::-1]
    def shortestPalindrome(self, s):
        main_s = s
        current_index = len(s) - 1
        chars_to_add = ''

        while self.isNotPalindrome(s):
            chars_to_add = chars_to_add + main_s[current_index]
            current_index = current_index - 1
            s = chars_to_add + main_s

        return s

if __name__ == '__main__':
    test = "acecaaa"
    test = "abcd"
    s = Solution()
    ans = s.shortestPalindrome(test)
    print(ans)
