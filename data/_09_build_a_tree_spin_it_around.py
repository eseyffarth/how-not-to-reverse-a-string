# 9/20: Build a tree, spin it around

import itertools

def build_tree(word):
    if len(word) == 1:
        return word
    return [word[0], build_tree(word[1:])]

def tree_swap (tree):
    return list(tree[-1]) + list(tree[0])

def tree_reverse(word):
    tree = build_tree(word)
#     print("Initial tree: {}\n".format(tree))     # UNCOMMENT THIS!
    return "".join(tree_walk(tree))

def tree_walk(tree):
#     print(tree)                                  # UNCOMMENT THIS!
    if len(tree[1]) == 1:
        tree = tree_swap(tree)
    else:
        tree = tree_walk(tree[-1]) + list(tree[0])
#     print(tree)                                  # UNCOMMENT THIS!
    return tree

print(tree_reverse("my head hurts"))