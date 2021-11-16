class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        ans = 0
        current_index = 0
        items_checked = []
        i = 0
        while i < len(chars):
            current_item = chars[i]
            ans = ans + 2
            for j in chars[i:len(chars)]:
                i = i + 1
                if j != current_item:
                    break

        return ans