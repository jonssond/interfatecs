from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right

    def bfs(self):
        if self.root is None:
            return []
        nodes_in_level_order = []
        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            nodes_in_level_order.append(str(current_node.value))
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return nodes_in_level_order
            



def main():
    testes = int(input())

    for i in range(1, testes + 1):
        tree = BinarySearchTree()

        qtd_nos = int(input())
        nos = list(map(int, input().split()))

        for no in nos:
            tree.insert(no)

        bfs_result = tree.bfs()
        
        print(f"Case {i}:")
        print(' '.join(bfs_result))
        print()

if __name__ == "__main__":
    main()

