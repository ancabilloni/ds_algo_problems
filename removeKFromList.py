# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# Time: O(n), space O(1)

""" My long solution, using two temp pointer Node holders """
def removeKFromList(l, k):
    q = l
    # Check if node start with k and remove
    while q is not None and q.value == k:
        l = q.next
        q = l

    # Check if list is empty
    if q is None:
        return l

    p = l.next

    # Check middle node and end node
    while p:
        # print (q.value, p.value)
        if p.value == k:
            while p and p.value == k:
                q.next = p.next
                p = p.next

            if p == None: # end node
                return l
            else: # middle node
                q = p
                p = p.next
        else:
            q = p
            p = p.next

    return l

""" Other user clean solution """
def removeKFromList(l, k):
    tmp = l

    while tmp:
        if tmp.next and tmp.next.value == k:
            tmp.next = tmp.next.next
        else:
            tmp = tmp.next
    return l.next if l and l.value == k else l
