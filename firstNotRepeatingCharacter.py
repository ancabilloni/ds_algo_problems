"""
Brute-force:
O(n^2), O(1) space
For each character, loop through the rest of the array to find repeat
return first non-repeat

Efficient
O(n) time, O(1) space
_count array keeps track of frequency of the character in string
_order array keeps log in the character first seen in order
"""

def firstNotRepeatingCharacter(s):
    _count = [0]*26
    _order = [0]*26
    
    l = 0
    for c in s:
        _count[ord(c) - ord('a')] += 1
        if _count[ord(c) - ord('a')] == 1:
            _order[l] = ord(c) -ord('a')
            l += 1
    
    for i in _order:
        if _count[i] == 1:
            return chr(i + ord('a'))
        
    return '_'
