import random
from rbt import RBTree

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                current = current.right

    def get_height(self):
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))


def experiment_1():
    list_length = 10000
    runs = 20

    bst_heights = []
    rbt_heights = []
    differences = []

    for run in range(1, runs + 1):
        values = random.sample(range(list_length * 10), list_length)

        bst = BST()
        for value in values:
            bst.insert(value)

        rbt = RBTree()
        for value in values:
            rbt.insert(value)

        bst_height = bst.get_height()
        rbt_height = rbt.get_height()
        difference = bst_height - rbt_height

        bst_heights.append(bst_height)
        rbt_heights.append(rbt_height)
        differences.append(difference)

        print("Run", run)
        print("BST height =", bst_height)
        print("RBT height =", rbt_height)
        print("Height difference =", difference)
        print()

    average_difference = sum(differences) / runs
    average_bst_height = sum(bst_heights) / runs
    average_rbt_height = sum(rbt_heights) / runs
    print("Experiment 1 Summary")
    print("List length =", list_length)
    print("Number of random lists =", runs)
    print("Average BST height =", average_bst_height)
    print("Average RBT height =", average_rbt_height)
    print("Average height difference =", average_difference)


if __name__ == "__main__":
    experiment_1()