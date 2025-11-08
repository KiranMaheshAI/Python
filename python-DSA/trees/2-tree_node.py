from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children

    def get_data(self):
        return self.data

    def print(self):
        print(self.data)
        for child in self.children:
            child.print()

def print_tree(tree_node):
    print(tree_node.get_data())
    for child in tree_node.get_children():
        print_tree(child)
    print()

def print_tree_detailed(root):
    if root is None:
        return
    print(f"{root.get_data()}:", end=" ")
    for child in root.get_children():
        print(child.get_data(), end=" ")
    print()
    for child in root.get_children():
        print_tree_detailed(child)

# Output as :
# 1:2,3,4
# 2:4,5
# 3:6,7
# 4:8,9

def take_input():
    root_data = int(input("Enter the root data: "))
    if root_data == -1:
        return None
    root = TreeNode(root_data)
    print(f"Enter the number of children for {root_data}: ")
    num_children = int(input())
    for i in range(num_children):
        child = take_input()
        root.add_child(child)
    return root

def take_input_level_wise():
    root_data = int(input("Enter the root data: "))
    if root_data == -1:
        return None
    root = TreeNode(root_data)
    q = deque([root])
    while q.is_empty():
        current_node = q.popleft()
        print(f"Enter the number of children for {current_node.get_data()}: ")
        num_children = int(input())
        for i in range(num_children):
            child_data = int(input(f"Enter the {i+1}th child of {current_node.get_data()}: "))
            child = TreeNode(child_data)
            current_node.add_child(child)
            q.append(child)
    return root


def count_nodes(root):
    if root is None:
        return 0
    count = 1
    for child in root.get_children():
        count += count_nodes(child)
    return count

def height_of_tree():
    if root is None:
        return 0
    height = 0
    for child in root.get_children():
        height = max(height, height_of_tree(child))
    return height + 1

def height_of_tree_iterative(root):
    if root is None:
        return 0
    height = 0
    q = deque([root])
    while q.is_empty():
        current_node = q.popleft()
        for child in current_node.get_children():
            q.append(child)
        height += 1
    return height
    

if __name__ == "__main__":
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root.add_child(child1)
    root.add_child(child2)
    print(root.get_data())
    print(root.get_children())