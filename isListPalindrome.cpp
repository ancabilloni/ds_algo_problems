// Singly-linked lists are already defined with this interface:
// template<typename T>
// struct ListNode {
//   ListNode(const T &v) : value(v), next(nullptr) {}
//   T value;
//   ListNode *next;
// };
//
/* Approach:
find the mid pointer, reverse the second half of the list
go through each half list and compare
Time O(n), Space O(1)
*/ 
ListNode<int> * reverseList(ListNode<int> * head)
{
    ListNode<int> * prev = NULL;
    ListNode<int> * forw = NULL;

    while (head)
    {
        forw = head->next;
        head->next = prev;
        prev = head;
        head = forw;
    }
    return prev;
}

bool isListPalindrome(ListNode<int> * l) {
    if (!l || !l->next) return true;

    ListNode<int> * mid = l;
    ListNode<int> * end = l;

    // Find mid pointer
    while(end)
    {
        end = end->next;
        if (end)
        {
            mid = mid->next;
            end = end->next;
        }
    }

    // reverse half end of list
    ListNode<int> * tail = reverseList(mid);

    // Compare two list
    while (tail)
    {
        if (l->value != tail->value)
            return false;
        l = l->next;
        tail = tail->next;
    }

    return true;
}
