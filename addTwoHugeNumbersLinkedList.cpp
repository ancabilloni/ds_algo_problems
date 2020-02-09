// Singly-linked lists are already defined with this interface:
// template<typename T>
// struct ListNode {
//   ListNode(const T &v) : value(v), next(nullptr) {}
//   T value;
//   ListNode *next;
// };

/* Approach 
- Reverse two original lists
- Sum (a,b,carry) from the end of the list, save carry if sum > 9999 limit
- Add sum result to new node of sum_list
- Take care of case when one list size is greater than the other
- Take care of case when carry goes further than original max size of list
- Reverse the sum_list
- Time O(n), space O(1) if not counting creation of the sum_list else O(n)
*/

ListNode<int> * reverseLinkedList(ListNode<int> * head)
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


ListNode<int> * addTwoHugeNumbers(ListNode<int> * a, ListNode<int> * b) {
    ListNode<int> * a_reverse = reverseLinkedList(a);
    ListNode<int> * b_reverse = reverseLinkedList(b);
    ListNode<int> * sum_reverse = NULL;
    ListNode<int> * currNode = NULL;
    int carry = 0;

    while (a_reverse || b_reverse)
    {
        int a = a_reverse ? a_reverse->value : 0;
        int b = b_reverse ? b_reverse->value : 0;
        int sum = a + b + carry;
        
        carry = 0;
        if (sum > 9999)
        {
            carry = 1;
            sum = sum % 10000;
        }

        ListNode<int> * nextNode = new ListNode(sum);

        if (!sum_reverse)
        {
            sum_reverse = nextNode;
            currNode = sum_reverse;
        } else
        {
            currNode->next = nextNode;
            currNode = nextNode;
        }

        if (a_reverse) a_reverse = a_reverse->next;
        if (b_reverse) b_reverse = b_reverse->next;
    }

    // When carry expands to further than the maximum size of original lists
    if (carry)
    {
        ListNode<int> * nextNode = new ListNode(carry);
        currNode->next = nextNode;
    }

    return reverseLinkedList(sum_reverse);
}
