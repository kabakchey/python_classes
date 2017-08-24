
class BinarySearchTree:

    class BSTNode:
        def __init__(self, value, left_child = None, right_child = None):
            self.value = value
            self.left = left_child
            self.right = right_child

        def __str__(self):
            return "%s" % self.value

        def __lt__(self, other):
            return self.value < other.value

    def __init__(self, *values):
        self.root = None
        self.traversed_path = []
        self.visited_nodes = set()

        for v in values:
            self.add(v)

    def __next__(self):
        pass

    def __iter__(self):
        pass


    def add(self, value):
        if value is None:
            raise ValueError("Invalid value: 'None' violates BST invariant")

        node, found = self.find(value)
        if node is None:
            self.root = BinarySearchTree.BSTNode(value)
        elif found:
            old_node = node.rigth
            node.rigth = BinarySearchTree.BSTNode(value)
            node.rigth.right = old_node
        elif value < node.value:
            node.left = BinarySearchTree.BSTNode(value)
        elif value > node.value:
            node.right = BinarySearchTree.BSTNode(value)

    def remove(self, value):
        pass

    # good BST should be balanced to guarantee log(N) time complexity: http://bit.ly/1V5RqKL
    def balance(self, value):
        pass

    def find(self, value):
        node = self.root
        current = node

        while not current is None:
            if node.value > value:
                node, current = current, node.left
            elif node.value < value:
                node, current = current, node.right
            else:
                break
        return node, (not node is None and node.value == value)

    # called when 'in' is used
    def __contains__(self, value):
        _, status = self.find(value)
        return status

    def __str__(self):
        return "BST: root=%s" % self.root


########################################################
# Tests
########################################################
values = (5, 3, 42, 0, 7, -7, 17)
tree = BinarySearchTree(*values)
print(tree)

# 1
assert values[0] in tree
assert 100**500 not in tree

# # 2
# assert len(list(tree)) == len(values)
# assert min(list(tree)) == min(values)
# assert max(list(tree)) == max(values)
# assert list(tree)[ 0] == min(values)
# assert list(tree)[-1] == max(values)
# assert list(tree) == sorted(values)
#
# # 3
# [x for x in tree if x > 0] == sorted([x for x in values if x > 0])
