from treeviz.treeviz import Node as TreeNode


class Node(object):
    def __init__(self, value):
        self.value = value
        self.is_leaf = False
        self.next = None
        self.child = None


class PointerTrie(object):
    """
    Time Complexity: O(h * n)
    h = height of trie
    n = longest linked list of children
    """
    def __init__(self):
        self.root = Node(value=None)

    def insert(self, node):
        s = node.value
        cur = self.root
        ptr = 0
        while ptr < len(s):
            if cur.child:
                cur = cur.child
                if cur.value == s[ptr]:
                    ptr += 1
                else:
                    # Linear Time for searching child node
                    while cur.next:
                        if cur.next.value == s[ptr]:
                            ptr += 1
                            break
                        cur = cur.next
                    else:
                        cur.next = Node(value=s[ptr])
                        ptr += 1
                        cur = cur.next
            else:
                cur.child = Node(s[ptr])
                ptr += 1
                cur = cur.child
        cur.is_leaf = True

    def search(self, word):
        """Return True if the string exist in Trie """
        cur = self.root
        ptr = 0
        while ptr < len(word):
            if cur.child:
                cur = cur.child
                if cur.value == word[ptr]:
                    ptr += 1
                else:
                    # Linear Time for searching child node
                    while cur.next:
                        if cur.next.value == word[ptr]:
                            ptr += 1
                            break
                        cur = cur.next
                    else:
                        return False
            else:
                return False
        if not cur.is_leaf:
            return False
        return True

    def _dfs(self, tree_node, trie_node):
        trie_node = trie_node.child
        while trie_node:
            # Add additional brackets for leaves
            value = trie_node.value if not trie_node.is_leaf else "[{}]".format(trie_node.value)
            cur_tree_node = TreeNode(value)
            cur_tree_node = self._dfs(cur_tree_node, trie_node)
            tree_node.add_child(cur_tree_node)
            trie_node = trie_node.next
        return tree_node

    def visualize(self):
        tree_root = TreeNode(' ')
        tree_root = self._dfs(tree_root, self.root)
        tree_root.visualize()


if __name__ == "__main__":
    pointer_trie = PointerTrie()
    pointer_trie.insert(Node("apple"))
    pointer_trie.insert(Node("applepie"))
    pointer_trie.insert(Node("application"))
    pointer_trie.insert(Node("apps"))
    pointer_trie.insert(Node("ball"))
    pointer_trie.visualize()
