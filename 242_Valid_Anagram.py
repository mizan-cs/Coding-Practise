class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return "".join(sorted(s)) == "".join(sorted(t))

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    sol = Solution()

    test = sol.isAnagram(s,t)
    print(test)