class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        i = 0
        while i < l//2:
            s[i], s[l-i-1] = s[l-i-1],s[i]
            i += 1



if __name__ == '__main__':
    s = Solution()
    test = ["h","e","l","l","o"]

    s.reverseString(test)
    #print(ans)