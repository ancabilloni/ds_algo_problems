# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
# def isListPalindrome(l):
#     """ Time & Space: O(n)"""
#     s = []
#     tmp = l
#     while tmp:
#         s.append(tmp.value)
#         tmp = tmp.next

#     tmp = l
#     while tmp:
#         if s.pop() != tmp.value:
#             return False
#         tmp = tmp.next

#     return True

def isListPalindrome(l):
    """ Time O(n), Space O(1) """
    if not l or not l.next:
        return True

    mid_ptr = l # jump 1 pointer
    end_ptr = l # jump 2 pointers
    odd = False

    # Find mid pointer and if list is odd length
    while end_ptr:
        end_ptr = end_ptr.next
        if end_ptr:
            mid_ptr = mid_ptr.next
            end_ptr = end_ptr.next
        else:
            odd = True

    # Reverse second list
    if odd:
        mid_ptr = mid_ptr.next

    prev_ptr = None
    curr_ptr = mid_ptr
    next_ptr = None

    while curr_ptr:
        next_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr

    # Compare two lists
    while prev_ptr:
        if l.value != prev_ptr.value:
            return False
        prev_ptr = prev_ptr.next
        l = l.next

    return True


    
