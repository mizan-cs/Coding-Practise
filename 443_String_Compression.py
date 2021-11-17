def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    if len(chars) == 1:
        return 1
    index_completed = 0
    i = 0
    while i < len(chars):
        current_item = chars[i]
        count = 0
        for j in chars[i:len(chars)]:
            if j != current_item:
                break
            else:
                count = count +1
                i = i + 1

        if index_completed == 0:
            chars = [current_item, count] + chars[i:len(chars)]
        else:
            chars = chars[0:index_completed] + [current_item, count] + chars[i:len(chars)]
        index_completed = index_completed + 2
        i = index_completed
    return len(chars)

if __name__ == '__main__':
    test = ["a","a","a","b","b","a","a"]
    test = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    test = ["a"]
    test = ["a","a","b","b","c","c","c"]
    ans = compress(test)
    print(ans)