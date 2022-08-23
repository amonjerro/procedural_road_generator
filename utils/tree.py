class Node:
    def __init__(self, data):
        self.data = data
        self._left = None
        self._right = None
        self._height = None
        self.parent = None
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right

    @property
    def height(self):
        if self._height is None:
            self._height = self.calculate_height()
        
        return self._height

    def calculate_height(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        height = 1 + max(left_height, right_height)
        return height
    
    def recalculate_height(self):
        self._height = self.calculate_height()
    
    def update_heights(self):
        self.recalculate_height()

        if self.parent is not None:
            self.parent.update_heights()

    @property
    def grandparent(self):
        if self.parent is None or self.parent.parent is None:
            return None
        return self.parent.parent
    
    @left.setter
    def left(self, node):
        if node is not None:

            # Tell the child who its new parent is
            node.parent = self

        self._left = node

    @right.setter
    def right(self, node):

        if node is not None:

            # Tell the child who its new parent is
            node.parent = self

        self._right = node
    
    def balance(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        return left_height - right_height