class Solution:
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        while 1 < n:
            if n % 2 != 0:
                return False
            n = n // 2

        return True

        # Without root
        #return (n and (not (n & (n - 1))))
if __name__ == '__main__':
    s = Solution()
    test = -16
    ans = s.isPowerOfTwo(test)
    print(ans)