#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#%%
class MyLinkedList2:

    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        i = 0
        current = self.head
        while i < index:
            if current: 
                current = current.next
                i += 1
            else:
                return -1
        if current:
            return current.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val, self.head)
        self.head = new_head
        self.size = self.size + 1
        return

    def addAtTail(self, val: int) -> None:
        tail_node = ListNode(val, None)
        if self.size == 0:
            self.head = tail_node
            self.size = self.size + 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = tail_node
        self.size = self.size + 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        add_node = ListNode(val, None)
        current = self.head
        i = 0
        while i + 1 < index:
            current = current.next
            i = i + 1
        temp_next = current.next
        current.next = add_node
        add_node.next = temp_next
        self.size = self.size + 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size and index > 0:
            i = 0
            current = self.head
            while i+1 < index:
                current = current.next
                i += 1
            current.next = current.next.next
            self.size = self.size - 1
            return
        if index < self.size and index == 0:
            self.head = self.head.next
            return
        
    def printLinkList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
        return
    
    
#%%
class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head
        for i in range(index+1):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size = self.size + 1
        return

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        for i in range(self.size):
            current = current.next
        current.next = ListNode(val, None)
        self.size = self.size + 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size = self.size + 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size = self.size - 1
        return
        
    def printLinkList(self):
        current = self.dummy_head.next
        while current:
            print(current.val)
            current = current.next
        return
 
    
#%%
#       0    1    2    3 
#dummy -> 1 -> 3 -> 4 -> 5 

#%%
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.printLinkList()
obj.addAtIndex(0,10)
obj.addAtIndex(0,20)
obj.addAtIndex(1,30)
param_1 = obj.get(0)
#%%
obj.addAtTail(4)
obj.printLinkList()
#%%
obj.addAtIndex(2,5)
obj.printLinkList()
#%%
obj.deleteAtIndex(0)
obj.printLinkList()
#%%
param_1 = obj.get(1)
print(param_1)
