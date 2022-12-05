def simplePlay(tree):
    """
    accept a single argument, which is a tree and plays the game once by using the tree to guide its questions
    """
    if isLeaf(tree):
        new_str = "Is it " + tree[0] + "?"
        ans_1 = yes(new_str)
        return ans_1
    else:
        ans_2 = yes(tree[0])
        if ans_2 == True:
            return simplePlay(tree[1])
        elif ans_2 == False:
            return simplePlay(tree[2])

                     
def isLeaf(tree):
    """
    helper function to check if a node is a leaf
    return true if the tree is a leaf, return false if it is an internal node
    """
    if tree.left == None and tree.right == None:
        return True
    else:
        return False


def yes(prompt):
    """
    uses the prompt to ask the user a yes/no question
    return true if answer is yes, return false if answer is no
    """
    ans = input(prompt + " ")
    while ans != "yes" and ans != "no":
        print("input format error! ")
        ans = input(prompt + " ")
    if ans == "yes":
        return True
    else:
        return False


def playLeaf(tree):
    """
    play the game given a leaf node
    """
    ans_1 = yes("Is it " + tree[0] + "?")
    if ans_1 == True:
        print("I got it!")
        return tree, True
    elif ans_1 == False:
        ans_2 = input("Drats! What was it? ")
        ans_3 = input("What's a question that distinguishes between " + ans_2 + " and " + tree[0] + "? ")
        ans_4 = input("And what's the answer for " + ans_2 + "? ")
        if ans_4 == "yes":
            tree = (ans_3,(ans_2, None, None), (tree[0], None, None))
        elif ans_4 == "no":
            tree = (ans_3,(tree[0], None, None), (ans_2, None, None))
        return tree, False