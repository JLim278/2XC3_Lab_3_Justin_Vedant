import random
import matplotlib.pyplot as plt
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
        if self.root is None:
            return 0

        stack = [(self.root, 1)]
        height = 0

        while stack:
            node, level = stack.pop()
            if level > height:
                height = level
            if node.left is not None:
                stack.append((node.left, level + 1))
            if node.right is not None:
                stack.append((node.right, level + 1))
        return height

def do_swaps(values, swap_count):
    swapped_list = values[:]
    n = len(swapped_list)

    for _ in range(swap_count):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        swapped_list[i], swapped_list[j] = swapped_list[j], swapped_list[i]

    return swapped_list

def experiment_2():
    list_length = 10000
    runs = 10
    swap_counts = [0, 1, 2, 3, 4, 5, 10, 25, 50, 100]

    sorted_list = list(range(list_length))
    average_differences = []

    for swaps in swap_counts:
        differences = []

        for _ in range(runs):
            values = do_swaps(sorted_list, swaps)

            bst = BST()
            for value in values:
                bst.insert(value)

            rbt = RBTree()
            for value in values:
                rbt.insert(value)

            bst_height = bst.get_height()
            rbt_height = rbt.get_height()
            difference = bst_height - rbt_height
            differences.append(difference)

        average_difference = sum(differences) / runs
        average_differences.append(average_difference)

        print("Swaps =", swaps)
        print("Average height difference =", average_difference)
        print()

    plt.plot(swap_counts, average_differences, marker="o")
    plt.xlabel("Number of swaps")
    plt.ylabel("Average difference in height")
    plt.title("Experiment 2")
    plt.grid(True)
    plt.show()

    print("Experiment 2:")
    print("List length =", list_length)
    print("Number of runs =", runs)
    print("Swap counts =", swap_counts)

if __name__ == "__main__":
    experiment_2()