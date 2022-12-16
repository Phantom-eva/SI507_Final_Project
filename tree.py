import json


class treeNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data


def simplePlay(tree):
    """
    accept a single argument, which is a tree and plays the game once by using the tree to guide its questions
    """
    if isLeaf(tree):
        return tree.data
    else:
        ans_2 = yes(tree.data)
        if ans_2 == True:
            return simplePlay(tree.left)
        elif ans_2 == False:
            return simplePlay(tree.right)

                     
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
        print("Invalid input. Please enter yes or no ")
        ans = input(prompt + " ")
    if ans == "yes":
        return True
    else:
        return False


def loadQuestionTree():
    """
    read the tree from treeFile
    """
    with open('./static/question_tree.json', 'r') as treefile:
        treedata = json.load(treefile)
        # print(json.dumps(treedata, indent=4))
        tree = constructQuestionTree(treedata)
        return tree


def constructQuestionTree(treedata):
    if "child" not in treedata:
        node = treeNode(treedata["data"])
        return node
    else:
        node = treeNode(treedata["data"])
        node.left = constructQuestionTree(treedata=treedata["child"][0])
        node.right = constructQuestionTree(treedata=treedata["child"][1])
    return node

