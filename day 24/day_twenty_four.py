class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        if root is None:
            return
        tail = [root]
        while len(tail) != 0:
            p = tail.pop(0)
            print(p.data, end=' ')
            if p.left is not None:
                tail.append(p.left)
            if p.right is not None:
                tail.append(p.right)


T = int(input())
myTree = Solution()
root_ = None
for i in range(T):
    data_ = int(input())
    root_ = myTree.insert(root_, data_)
myTree.levelOrder(root_)
