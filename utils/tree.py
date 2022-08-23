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

    def get_key(self, **kwargs):
        return self.data
    
    def get_value(self):
        return self.data
    
    @property
    def height(self):
        if self._height is None:
            self._height = self.calculate_height()
        
        return self._height
    
    def is_leaf(self):
        return self.left is None and self.right is None

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
    
    def maximum(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def minimum(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

class Tree:
    
    @staticmethod
    def find(root:Node, key, **kwargs):
        node = root
        while node is not None:
            if key == node.get_key(**kwargs):
                break
            elif key < node.get_key(**kwargs):
                node = node.left
            else:
                node = node.right
        
        return node
    
    @staticmethod
    def find_value(root:Node , query:Node , compare=lambda x, y: x == y, **kwargs):
        key = query.get_key(**kwargs)
        node = root

        while node is not None:
            if key == node.get_key(**kwargs):
                if compare(node.data, query.data):
                    return node
                
                left = Tree.find_value(node.left, query, compare, **kwargs)
                if left is None:
                    right = Tree.find_value(node.right, query, compare, **kwargs)
                    return right
                
                return left
            
            elif key < node.get_key(**kwargs):
                return Tree.find_value(node.left, query, compare, **kwargs) or \
                       Tree.find_value(node.right, query, compare, **kwargs)
            
            else:
                return Tree.find_value(node.right, query, compare, **kwargs) or \
                       Tree.find_value(node.left, query, compare, **kwargs)
    
    @staticmethod
    def find_leaf_node(root: Node, key, **kwargs):
        node = root
        while node is not None:
            if node.is_leaf():
                return node
            
            elif key == node.get_key(**kwargs) and not node.is_leaf():
                if node.left is not None:
                    return node.left.maximum()
                
                return node.right.minimum()
            
            elif key < node.get_key(**kwargs):
                node = node.left
            else:
                node = node.right
        
        return node
    
    @staticmethod
    def insert(root: Node, node: Node, **kwargs):
        node_key = node.get_key(**kwargs) if node is not None else None
        root_key = root.get_key(**kwargs) if node is not None else None

        if root is None:
            return node
        
        elif node_key < root_key:
            root.left = Tree.insert(root.left, node, **kwargs)
        
        else:
            root.right = Tree.insert(root.right, node, **kwargs)
        
        root.recalculate_height()
        balance = root.balance()

        # Self-Rotation for balance
        if balance > 1 and node < root.left.get_key(**kwargs):
            return Tree.rotate_right(root)

        if balance < -1 and node_key > root.right.get_key(**kwargs):
            return Tree.rotate_left(root)

        if balance > 1 and node_key > root.left.get_key(**kwargs):
            root.left = Tree.rotate_left(root.left)
            return Tree.rotate_right(root)

        if balance < -1 and node_key < root.right.get_key(**kwargs):
            root.right = Tree.rotate_right(root.right)
            return Tree.rotate_left(root)
    
    @staticmethod
    def delete(root: Node, key: int, **kwargs):

        if root is None:
            return root

        elif key < root.get_key():
            root.left = Tree.delete(root.left, key)

        elif key > root.get_key():
            root.right = Tree.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = root.right.minimum()
            root.data = temp.data
            root.right = Tree.delete(root.right, temp.value.get_key(**kwargs))

        # If the tree has only one node, simply return it
        if root is None:
            return root

        # Update the height of the ancestor node
        root.update_height()

        # Balance the tree
        root = Tree.balance(root)

        return root

    @staticmethod
    def balance_and_propagate(node):
        node = Tree.balance(node)

        if node.parent is None:
            return node

        return Tree.balance_and_propagate(node.parent)

    @staticmethod
    def balance(node):

        # If the node is unbalanced, then try out the 4 cases

        # Case 1 - Left Left
        if node.balance > 1 and node.left.balance >= 0:
            return Tree.rotate_right(node)

        # Case 2 - Right Right
        if node.balance < -1 and node.right.balance <= 0:
            return Tree.rotate_left(node)

        # Case 3 - Left Right
        if node.balance > 1 and node.left.balance < 0:
            node.left = Tree.rotate_left(node.left)
            return Tree.rotate_right(node)

        # Case 4 - Right Left
        if node.balance < -1 and node.right.balance > 0:
            node.right = Tree.rotate_right(node.right)
            return Tree.rotate_left(node)

        return node

    @staticmethod
    def rotate_left(z):
        grandparent = z.parent
        y = z.right
        T2 = y.left

        # Appoint new parent to root of sub tree
        y.parent = grandparent

        # And point the parent back
        if grandparent is not None:
            if z.is_left_child():
                grandparent.left = y
            else:
                grandparent.right = y

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights (z has to be updated first, because it is a child of y)
        z.update_height()
        y.update_height()

        # Return the new root
        return y

    @staticmethod
    def rotate_right(z):
        grandparent = z.parent
        y = z.left
        T3 = y.right

        # Appoint new parent to root of sub tree
        y.parent = grandparent

        # And point the parent back
        if grandparent is not None:
            if z.is_left_child():
                grandparent.left = y
            else:
                grandparent.right = y

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights (z has to be updated first, because it is a child of y)
        z.update_height()
        y.update_height()

        # Return the new root
        return y

    @staticmethod
    def get_leaves(root: Node, leaves=None):
        if leaves is None:
            leaves = []

        # Base case
        if root.is_leaf():
            leaves.append(root)
            return leaves

        # Step
        if root.left is not None:
            leaves += Tree.get_leaves(root.left, None)
        if root.right is not None:
            leaves += Tree.get_leaves(root.right, None)
        return leaves