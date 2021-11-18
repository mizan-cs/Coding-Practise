class Solution:
    def compress(self, chars):
        # ["a","a","b","b","c","c","c"]
        n = len(chars)
        current_index = 1
        previous_char = chars[0]

        count = 1

        i = 1
        while i < n:
            if previous_char == chars[i]:
                count = count +1
            else:
                if count > 1:
                    count_str = str(count)
                    for ch in count_str:
                        chars[current_index] = ch
                        current_index += 1
                previous_char = chars[i]
                chars[current_index] = chars[i]
                current_index += 1
                count = 1
            i += 1

        if count > 1:
            count_str = str(count)
            for ch in count_str:
                chars[current_index] = ch
                current_index += 1

        return current_index
if __name__ == '__main__':
    s = Solution()
    test = ["a","a","b","b","c","c","c"]
    ans = s.compress(test)
    print(ans)