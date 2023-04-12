class CannotRemoveRootError(Exception):
    def __init__(self):
        self.message = "You cannot remove root if it is the only element of the tree."
        super().__init__(self.message)


class BST():
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, el):
        if el < self.value:
            if self.left == None:
                sub_tree = BST(el, self)
                self.left = sub_tree
            else:
                self.left.insert(el)
        else:
            if self.right == None:
                sub_tree = BST(el, self)
                self.right = sub_tree
            else:
                self.right.insert(el)

    def search_in_tree(self, el):
        if el == self.value:
            return self
        elif el < self.value:
            if self.left:
                return self.left.search_in_tree(el)
            else:
                return None
        else:
            if self.right:
                return self.right.search_in_tree(el)
            else:
                return None

    def find_min_element(self):
        current_el = self
        # Element most on the left
        while current_el.left:
            current_el = current_el.left
        return current_el

    '''Strategy when el_to_remove has both children - function replaces it with its right child'''
    def remove_from_tree_draft(self, el_to_remove):
        el = self.search_in_tree(el_to_remove)

        # Element exists in tree
        if el != None:
            left_child_exist = False if el.left == None else True
            right_child_exists = False if el.right == None else True
            el_is_left_subtree = True if el == el.parent.left else False

            # Has both left and right subtrees
            if left_child_exist and right_child_exists:
                if el_is_left_subtree:
                    el.parent.left = el.right
                else:
                    el.parent.right = el.right
                el.right.parent = el.parent
                min_el = el.right.find_min_element()
                min_el.left = el.left
                el.left.parent = min_el.left

            # Only has left or right subtree
            elif left_child_exist or right_child_exists:
                p = el.parent
                existing_child = el.left if left_child_exist else el.right
                if el_is_left_subtree:
                    el.parent.left = existing_child
                    existing_child.parent = el.parent
                else:
                    el.parent.right = existing_child
                    existing_child.parent = el.parent
                pass

            # It's a leaf (no left or right child)
            else:
                p = el.parent
                if el_is_left_subtree:
                    el.parent.left = None
                else:
                    el.parent.right = None
                pass

    '''Strategy when el_to_remove has both children - function replaces it with its succesor'''
    def remove_from_tree(self, el_to_remove):
        el = self.search_in_tree(el_to_remove)

        # Element exists in tree
        if el != None:
            left_child_exist = False if el.left == None else True
            right_child_exists = False if el.right == None else True
            if el.parent != None:
                el_is_left_subtree = True if el == el.parent.left else False

            # Has both left and right subtrees
            if left_child_exist and right_child_exists:
                succesor = el.right.find_min_element()
                # 1. Unlink succesor if it doesn't have right child
                if succesor.right == None:
                    if succesor.value < succesor.parent.value:
                        succesor.parent.left = None
                    else:
                        succesor.parent.right = None
                # 2. If succesor has right child, link it to succesor's parent
                else:
                    if succesor.value < succesor.parent.value:
                        succesor.parent.left = succesor.right
                    else:
                        succesor.parent.right = succesor.right
                    succesor.right.parent = succesor.parent
                    succesor.right = None
                # 3. Link el's parent to succesor
                if el.parent:
                    if el_is_left_subtree:
                        el.parent.left = succesor
                    else:
                        el.parent.right = succesor
                    succesor.parent = el.parent
                # REMOVING ROOT
                else:
                    succesor.parent = None
                    self.value = succesor.value

                # 4. Link el's children to succesor
                succesor.left = el.left
                el.left.parent = succesor
                if el.right:
                    succesor.right = el.right
                    el.right.parent = succesor

            # Only has left or right subtree
            elif left_child_exist or right_child_exists:
                existing_child = el.left if left_child_exist else el.right
                if el.parent:
                    if el_is_left_subtree:
                        el.parent.left = existing_child
                        existing_child.parent = el.parent
                    else:
                        el.parent.right = existing_child
                        existing_child.parent = el.parent

                # REMOVING ROOT
                else:
                    # Existing child becomes new root
                    self.value = existing_child.value
                    self.left = existing_child.left
                    if existing_child.left:
                        existing_child.left.parent = self
                    self.right = existing_child.right
                    if existing_child.right:
                        existing_child.right.parent = self


            # It's a leaf (no left or right child)
            else:
                if el.parent:
                    if el_is_left_subtree:
                        el.parent.left = None
                    else:
                        el.parent.right = None
                # REMOVING ROOT
                else:
                    raise(CannotRemoveRootError)

    def show_tree_dependencies(self):
        l = "-"
        r = "-"
        if self.left:
            l = self.left.show_tree_dependencies()
        if self.right:
            r = self.right.show_tree_dependencies()
        print(self.value, ",", l, ",", r)
        return self.value

    def show_tree(self, big_spaces=True, show_empty_branches=True, show_empty_nodes=False):
        # (Different display options available)
        # Getting the rows
        level_nr = 1
        levels = []
        if show_empty_nodes:
            empty_str = "-"
        else:
            empty_str = " "

        while True:
            level = self.show_level(empty_str, level_nr)
            empty_level = [empty_str for i in range(2**(level_nr-1))]
            if level == empty_level:
                break
            level_nr += 1
            levels.append(level)
        # Displaying the rows
        max_len = len(levels[-1])
        if big_spaces:
            min_space = max(3, (14-2**(len(levels)-1))) + 1
        else:
            min_space = 2

        for level_nr in range(len(levels)):
            chars = levels[level_nr]
            if show_empty_branches:
                branches = [" " if level_nr==0 else "/" if (i%2==0) else "\\" for i in range(len(chars))]
            else:
                branches = [" " if level_nr==0 else "/" if (i%2==0 and chars[i]!=empty_str) else "\\" if (chars[i]!=empty_str) else " " for i in range(len(chars))]
            if big_spaces:
                space_multiplier = " "*max(3, (14-2**(level_nr))) # Parameter decided by trial and error
            else:
                space_multiplier = " "
            print((space_multiplier.join(branches)).center(max_len*min_space, " "))
            print((space_multiplier.join(levels[level_nr])).center(max_len*min_space, " "))
            print("")

    def show_level(self, empty_str, level=1):

        if level == 1:
            return [str(self.value)]
        else:
            if self.left:
                left = self.left.show_level(empty_str, level-1)
            else:
                left = []
                for i in range(2**(level-2)):
                    left.append(empty_str)

            if self.right:
                right = self.right.show_level(empty_str, level-1)
            else:
                right = []
                for i in range(2**(level-2)):
                    right.append(empty_str)

            return(left + right)

def make_tree(list):
    root = list[0]
    tree = BST(root, None)
    for el in list[1:]:
        tree.insert(el)
    return tree

# def test_removing():
#     t = make_tree([15, 75, 34, 9, 64, 73, 83, 46, 16, 56])
#     t.show_tree(1,1,1)
#     t.remove_from_tree(15)
#     t.show_tree(1,1,1)
#     t.remove_from_tree(1)
#     t.show_tree(1,1,1)

# def test_random():
#     import random
#     elements = random.sample(range(1, 100), 11)
#     print(elements[1:])
#     t = make_tree(elements[1:])
#     t.show_tree(1,1,1)
#     print(elements[1:], elements[4])
#     t.remove_from_tree(elements[4])
#     t.show_tree(1,1,1)
