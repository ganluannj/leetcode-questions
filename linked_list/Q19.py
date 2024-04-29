#%%
# The idea is to use two indexes, slow and fast
# start both of them at the dummy_head, which points to the real head
# move fast till to the n+1 th element 
# then move slow and fast together until the fast is pointing to None
# now slow is at the point where the next node should be deleted
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#%%
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy_head = ListNode(0, head)
        slow, fast = dummy_head, dummy_head
        i = 0
        while i < n+1:
            if fast:
                fast = fast.next
                i += 1
            else:
                return False
            
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return dummy_head.next
    
#%%
Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node5 = ListNode(5)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
#%%
S = Solution()
new_head = S.removeNthFromEnd(Node1, 1)
cur = new_head
print('----------')
while cur:
    print(cur.val)
    cur = cur.next