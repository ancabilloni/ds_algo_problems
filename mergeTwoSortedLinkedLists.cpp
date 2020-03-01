// Time O(l1.length + l2.length)

// Complete the mergeLists function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */


SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2)
{
  SinglyLinkedListNode * g = new SinglyLinkedListNode(-1);
  SinglyLinkedListNode * g_next = g;
  while (head1 && head2)
  {
    if (head1->data < head2->data)
    {
      g_next->next = head1;
      head1 = head1->next;
    } else
    {
      g_next->next = head2;
      head2 = head2->next;
    }
    g_next = g_next->next;
  }
  g_next->next = head1 ? head1 : head2;
  return g->next;
}
