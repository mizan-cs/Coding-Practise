def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    if len(chars) == 1:
        return len(chars)
    index_completed = 0
    i = 0
    while i < len(chars):
        current_item = chars[i]
        count = 0
        if index_completed == 0:
            i = 1

        for j in chars[i:len(chars)]:
            if j != current_item:
                break
            else:
                count = count +1
                i = i + 1
        if index_completed == 0:
            if count > 1:
                chars = [current_item, count] + chars[i:len(chars)]
                index_completed = index_completed + 2
            else:
                chars = [current_item] + chars[i:len(chars)]
                index_completed = index_completed + 1
        else:
            if count > 9:
                chars = chars[0:index_completed] + [current_item]+ list(str(count)) + chars[i:len(chars)]
                index_completed = index_completed + len(str(count)) + 1
            else:
                chars = chars[0:index_completed] + [current_item, count] + chars[i:len(chars)]
                index_completed = index_completed + 2
        i = index_completed

    print(chars)
    return len(chars)

if __name__ == '__main__':
    test = ["a","a","b","b","c","c","c"]
    test = ["a"]
    test = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    test = ["a","a","a","b","b","a","a"]
    ans = compress(test)
    print(ans)