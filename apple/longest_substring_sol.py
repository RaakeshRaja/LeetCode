#! /usr/bin/env python3.6


# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3.


def solution(s: str) -> int:
    """
    Returns the longest substring without repeating characters in a given
    atring
    """
    max_res = 0
    max_temp = 0 
    temp = []
    if not s:
        return -1

    for char in s:
        if char not in temp:
            max_temp += 1
            temp.append(char)
            if max_temp >= max_res:
                max_res = max_temp
        else:
            max_temp = 0
            temp = []

    return max_res

if __name__=='__main__':
    result = solution("pwwkew")
    print(result)


