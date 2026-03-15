class XC3Tree:
    def __init__(self, degree):
        self.degree = degree
        self.children = []
        
        # Loop to create each child. 
        for i in range(degree):
            if i < 2:
                # The first two children (index 0 and 1) are always leaves (degree 0)
                child_degree = 0
            else:
                # Since 'i' is 0 indexed, the actual position is (i + 1)
                # So (i + 1) - 2 simplifies to (i - 1)
                child_degree = i - 1
                
            # Create the child tree and add it to our list
            self.children.append(XC3Tree(child_degree))

    def get_degree(self):
        # Give the degree of the current tree
        return self.degree

    def get_height(self):
        # A tree with a degree of 0 has no children so its height is 0
        if self.degree == 0:
            return 0
        
        # Find the tallest child by checking each one
        tallest = 0
        for child in self.children:
            current_height = child.get_height()
            if current_height > tallest:
                tallest = current_height
                
        return 1 + tallest

    def get_num_nodes(self):
        # Start the count at 1 to include the current node
        count = 1
        
        # Add up all the nodes inside every child
        for child in self.children:
            count += child.get_num_nodes()
            
        return count