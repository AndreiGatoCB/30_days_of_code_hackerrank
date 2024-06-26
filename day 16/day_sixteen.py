class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        new_node = Node(data)
        if head is None:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head


mylist = Solution()
T = int(input())
head_ = None
for i in range(T):
    data_ = int(input())
    head_ = mylist.insert(head_, data_)

mylist.display(head_)
