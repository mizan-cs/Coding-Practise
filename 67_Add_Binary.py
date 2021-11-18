class Solution:
    def addBinary(self, a, b) -> str:
        ans = int(a, 2) + int(b, 2)

        return bin(ans).replace("0b", "")


if __name__ == '__main__':
    a = "11"
    b = "1"
    s = Solution()
    ans = s.addBinary(a, b)
    print(ans)
