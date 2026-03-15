class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        #TODO
        left_child = self.left
        if left_child is None:
            return self

        self.left = left_child.right
        if left_child.right:
            left_child.right.parent = self

        left_child.parent = self.parent
        if self.parent:
            if self.parent.left == self:
                self.parent.left = left_child
            else:
                self.parent.right = left_child
        left_child.right = self
        self.parent = left_child
        return left_child 


    def rotate_left(self):
        #TODO
        right_child = self.right
        if right_child is None:
            return self

        self.right = right_child.left
        if right_child.left:
            right_child.left.parent = self

        right_child.parent = self.parent
        if self.parent:
            if self.parent.left == self:
                self.parent.left = right_child
            else:
                self.parent.right = right_child
        right_child.left = self
        self.parent = right_child
        return right_child



class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        if node.parent == None:
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red(): 
            #TODO
            parent = node.parent
            grandparent = parent.parent

            if grandparent is None:
                break

            if parent == grandparent.left:
                uncle = grandparent.right

                # uncle red so recolour
                if uncle is not None and uncle.is_red():
                    parent.make_black()
                    uncle.make_black()
                    grandparent.make_red()
                    node = grandparent
                else:
                    # convert left-right into left-left
                    if node == parent.right:
                        node = parent
                        rotated = node.rotate_left()
                        if rotated.parent is None:
                            self.root = rotated
                        parent = node.parent
                        grandparent = parent.parent

                    # left-left case
                    parent.make_black()
                    grandparent.make_red()
                    rotated = grandparent.rotate_right()
                    if rotated.parent is None:
                        self.root = rotated

            else:
                uncle = grandparent.left

                # uncle red so recolour
                if uncle is not None and uncle.is_red():
                    parent.make_black()
                    uncle.make_black()
                    grandparent.make_red()
                    node = grandparent
                else:
                    # convert right-left into right-right
                    if node == parent.left:
                        node = parent
                        rotated = node.rotate_right()
                        if rotated.parent is None:
                            self.root = rotated
                        parent = node.parent
                        grandparent = parent.parent

                    # right-right case
                    parent.make_black()
                    grandparent.make_red()
                    rotated = grandparent.rotate_left()
                    if rotated.parent is None:
                        self.root = rotated

        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
