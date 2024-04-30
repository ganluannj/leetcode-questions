#%%
# get the length of each linkedList, lenA and lenB
# take the case that list A is longer
# cur_A and cur_B point to the start of listA and listB
# move cur_A for (lenA-lenB) nodes
# then start comparing cur_A and cur_B and moving one by one
# and comparing cur_A and cur_B, the first code curA == curB,
# is the first common node, if no common nodes found, return None
#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#%%
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        lenA, lenB = 0, 0
        curA = headA
        curB = headB
        while curA.next:
            lenA += 1
            curA = curA.next
        while curB.next:
            lenB += 1
            curB = curB.next
        if lenA >= lenB:
            curA = headA
            for _ in range(lenA - lenB):
                curA = curA.next
            curB = headB
        if lenA < lenB:
            curB = headB
            for _ in range(lenB - lenA):
                curB = curB.next
            curA = headA
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None
#%%
Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node5 = ListNode(5)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node5
Node4.next = Node3

#%%
S = Solution()
print(S.getIntersectionNode(Node1, Node4).val)
