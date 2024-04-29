#%%
# use prev to indicate the last nodes that have been swapped
# curr = prev.next will the frist node to swap
# nnext = cur.next will be the second node to swap
# swap curr and nnext and the move prev to curr
# stop when curr is null or nnext is null
#%%
class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next
#%%
class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        dummy_head = ListNode(0, head)
        prev = dummy_head
        while prev:
            curr = prev.next
            if curr:
                nnext = curr.next
                if nnext:
                    temp = nnext.next
                    prev.next = nnext
                    nnext.next = curr
                    curr.next = temp
                    prev = curr
                else:
                    break
            else:
                break
        return dummy_head.next
    
#%%
Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
 #%%
S = Solution()
swap_head = S.swapPairs(Node1)
cur = swap_head
print('----------')
while cur:
    print(cur.val)
    cur = cur.next
