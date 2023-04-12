from BST_trees import BST, CannotRemoveRootError, make_tree

class AVL(BST):
    def __init__(self, value, parent):
        super().__init__(value, parent)
        self.height = 1
        self.bf = 0

    def go_preorder(self, values=None, show_bf=False):
        if values == None:
            values = []
        if show_bf:
            values.append((self.value, self.bf))
        else:
            values.append(self.value)
        if self.left:
            values = self.left.go_preorder(values, show_bf)
        if self.right:
            values = self.right.go_preorder(values, show_bf)
        return values

    def go_postorder(self, values=None, show_bf=False):
        if values == None:
            values = []
        if self.left:
            values = self.left.go_postorder(values, show_bf)
        if self.right:
            values = self.right.go_postorder(values, show_bf)

        if show_bf:
            values.append((self.value, self.bf))
        else:
            values.append(self.value)
        return values

    def update_balance(self):
        left_height, right_height = 0, 0
        if self.left:
            left_height = self.left.height
        if self.right:
            right_height = self.right.height

        self.bf = left_height - right_height
        additional_height = max(left_height, right_height)
        self.height = additional_height + 1

        if self.parent:
            self.parent.update_balance()

    def update_balance_postorder(self):
        nodes = self.go_postorder()
        for node in nodes:
            if node != None:
                node = self.search_in_tree(node)
                if node.left==None and node.right==None:
                    node.update_balance()

    def RR_rotation(self):
        unbalanced_node = self
        R_node = self.right

        if unbalanced_node.parent:
            # relink R_node's left child if it has one
            if R_node.left:
                unbalanced_node.right = R_node.left
                R_node.left.parent = unbalanced_node
                R_node.left = None
            else:
                unbalanced_node.right = None
            # rotation
            R_node.left = unbalanced_node
            R_node.parent = unbalanced_node.parent
            if unbalanced_node.value < unbalanced_node.parent.value:
                unbalanced_node.parent.left = R_node
            else:
                unbalanced_node.parent.right = R_node
            unbalanced_node.parent = R_node

            unbalanced_node.update_balance()
        # ROOT
        else:
            root_value = unbalanced_node.value
            unbalanced_node.value = R_node.value
            R_node.value = root_value
            if R_node.right:
                unbalanced_node.right = R_node.right
                R_node.right.parent = unbalanced_node
                R_node.right = None
            if R_node.left:
                R_node.right = R_node.left
                R_node.left = None
            if unbalanced_node.left:
                R_node.left = unbalanced_node.left
                R_node.left.parent = unbalanced_node
            unbalanced_node.left = R_node


            R_node.update_balance()

    def LL_rotation(self):
        unbalanced_node = self
        L_node = self.left

        if unbalanced_node.parent:
            # relink L_node's right child if it has one
            if L_node.right:
                unbalanced_node.left = L_node.right
                L_node.right.parent = unbalanced_node
                L_node.right = None
            else:
                unbalanced_node.left = None
            # rotation
            L_node.right = unbalanced_node
            L_node.parent = unbalanced_node.parent
            if unbalanced_node.value < unbalanced_node.parent.value:
                unbalanced_node.parent.left = L_node
            else:
                unbalanced_node.parent.right = L_node
            unbalanced_node.parent = L_node

            unbalanced_node.update_balance()
        # ROOT
        else:
            root_value = unbalanced_node.value
            unbalanced_node.value = L_node.value
            L_node.value = root_value
            if L_node.left:
                unbalanced_node.left = L_node.left
                L_node.left.parent = unbalanced_node
                L_node.left = None
            if L_node.right:
                L_node.left = L_node.right
                L_node.right = None
            if unbalanced_node.right:
                L_node.right = unbalanced_node.right
                L_node.right.parent = unbalanced_node
            unbalanced_node.right = L_node

            L_node.update_balance()

    def RL_rotation(self):
        self.right.LL_rotation()
        self.RR_rotation()

    def LR_rotation(self):
        self.left.RR_rotation()
        self.LL_rotation()

    def fix_balance(self):
        balances = self.go_postorder(show_bf=True)
        unbalanced_node = None
        for node, bf in balances:
            if abs(bf) == 2:
                unbalanced_node = self.search_in_tree(node)

        if unbalanced_node:
            left_h, right_h = 0, 0

            if unbalanced_node.bf == 2:
                # L - R = 2 -> left greater -> LX rotation will be used
                child_of_unbalanced_node = unbalanced_node.left
            else:
                # L - R = -2 -> right greater -> RX rotation will be used
                child_of_unbalanced_node = unbalanced_node.right

            # We now LX or RX rotation is needed -> left/right child of unbalanced_node will be used
            # Using LL/LR RL/RR depends on which child's subtree is higher
            if child_of_unbalanced_node.left:
                left_h = child_of_unbalanced_node.left.height
            if child_of_unbalanced_node.right:
                right_h = child_of_unbalanced_node.right.height

            #LX
            if child_of_unbalanced_node == unbalanced_node.left:
                if left_h > right_h:
                    unbalanced_node.LL_rotation()
                else:
                    unbalanced_node.LR_rotation()
            #RX
            else:
                if left_h > right_h:
                    unbalanced_node.RL_rotation()
                else:
                    unbalanced_node.RR_rotation()

            # check the balance after rotation
            self.fix_balance()

    def insert(self, el, is_subprocess=0):
        if el < self.value:
            if self.left == None:
                sub_tree = AVL(el, self)
                self.left = sub_tree
            else:
                self.left.insert(el, is_subprocess=1)
        else:
            if self.right == None:
                sub_tree = AVL(el, self)
                self.right = sub_tree
            else:
                self.right.insert(el, is_subprocess=1)
        el = self.search_in_tree(el)
        if el != None:
            el.update_balance()
        self.fix_balance()

    def remove_from_tree(self, el):
        super().remove_from_tree(el)
        # First call of the remove function, not nested
        if self.parent == None:
            # self.show_tree(1,0,1)
            # print(self.go_postorder(show_bf=True))
            self.update_balance_postorder()
            self.fix_balance()

def make_AVL_tree(list):
    root = list[0]
    tree = AVL(root, None)
    for el in list[1:]:
        tree.insert(el)
        # tree.show_tree(1,0,1)
        # print(tree.go_postorder(show_bf=True))
    return tree


# t = make_AVL_tree([4,3,3.5,3.2,3.6,2,1,5])
# t = make_AVL_tree([1,2,3,4,5,6])
# t = make_AVL_tree([5,4,2,1,6,3,9,0,8,7])
# t.show_tree(1,0,1)
# print(t.go_preorder(show_bf=True))
# t.insert(6)
# t.show_tree(1,0,1)
# print(t.go_preorder(show_bf=True))
# t.insert(7)
# t.show_tree(1,0,0)
# print(t.go_preorder(show_bf=True))
