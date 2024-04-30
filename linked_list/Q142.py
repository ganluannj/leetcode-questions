#%%
# the idea is to store the node in a set 
# go through the linkedList until find end node or find a node already
# in the set 
# the first node found already in the set, is the start of the cycle 
# if find the end node, then there will be no cycle
#%%
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = next
#%%
class Solution:
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        nodes_set = set()
        cur = head
        while cur:
            if cur in nodes_set:
                return cur
            nodes_set.add(cur)
            cur = cur.next
        return None
#%%
# the second idea is to use fast and slow index, each time fast index 
# move 2 nodes and slow index moves 1 node 
# if there is cycle in the linkedlist, they will eventuall meet with each other
# A -> B -> C -> D -> E
#           |          |
#           J          F
#           |          |
#           I <- H <- G
# say the slow and fast meet at H, the distance between A to C is x, 
# and the distance between C to H is y, and distance from H to C is z
# thus slow index moves x+y and fast moves x + y + n (y+z), n is the number
# of loops that fast moves in the cycles before slow and fast meet 
# x + y + n (y+z) = 2 (x+y)
# x = z + (n-1)(y+z)
# thus if we put one index1 at the begining and another index2 at H, 
# eventually they will meet at the entrance of the loop, no matter how
# many loops index2 has move in the cycle
#%%
class Solution2:
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: # there will be cycle
                index1 = head
                index2 = slow
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None