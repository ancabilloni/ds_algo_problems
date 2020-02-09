# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseList(l):
    prev = None
    curr = l
    forw = None
    while (curr):
        forw = curr.next
        curr.next = prev
        prev = curr
        curr = forw
    return prev

def addTwoHugeNumbers(a, b):
    a_reverse = reverseList(a)
    b_reverse = reverseList(b)
    sumNode = None
    carry = 0
    _sum = 0

    while (a_reverse or b_reverse or carry):
        a_val = a_reverse.value if a_reverse else 0
        b_val = b_reverse.value if b_reverse else 0
        _sum = a_val + b_val + carry
        carry = 0
        if (_sum > 9999):
            carry = 1
            _sum %= 10000
        newNode = ListNode(_sum)
        newNode.next = sumNode
        sumNode = newNode
        a_reverse = a_reverse.next if a_reverse else None
        b_reverse = b_reverse.next if b_reverse else None
    
    return sumNode
