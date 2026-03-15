from Part2_Implementation import XC3Tree

def experiment_3():
    print("Experiment 3 Results:")
    print("Degree | Height")
    print("-" * 10)

    # Create trees from degree 0 to 25 and print their heights
    for i in range(26):
        tree = XC3Tree(i)
        print(f"{i:6} | {tree.get_height()}")

if __name__ == "__main__":
    experiment_3()