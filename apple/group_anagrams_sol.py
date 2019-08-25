#! /usr/bin/env python3.6

"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

def solution(strs):

    """
    Given an array of strings, groups anagrams together
    """
    char_grps = {}
    sublists = {}
    count = 0

    for i in range(len(strs)):
        if set(list(strs[i])) not in char_grps.values():
            count += 1
            char_grps.update({count:set(list(strs[i]))})
    
    for item in strs:
        for key, chars in char_grps.items():
            if (set(list(item))) == chars:
                try:
                    if sublists[key] is not None:
                        sublists[key].append(item)
                except Exception as e:
                    print(f'key {key} not found: {e}')
                    sublists.update({key:[item]})
    print(list(sublists.values()))
    return(list(sublists.values()))
            
        

def solution2(strs):
    """
    another way to do it
    """
    final = {}
    for item in strs:
        if "".join(sorted(list(item))) not in final:
            final.update({"".join(sorted(list(item))): [item]})
        else:
            final["".join(sorted(list(item)))].append(item)
    
    return(list(final.values()))

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ['cat', 'dog', 'tac', 'god', 'act']
    print(strs)
    print(solution2(strs))
