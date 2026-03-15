from Part2_Implementation import XC3Tree

def experiment_4():
    print("Experiment 4 Results:")
    print("Degree | Nodes")
    print("-" * 10)

    # Create trees from degree 0 to 25 and print their total node count
    for i in range(26):
        tree = XC3Tree(i)
        print(f"{i:6} | {tree.get_num_nodes()}")

if __name__ == "__main__":
    experiment_4()