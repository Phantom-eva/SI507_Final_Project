import numpy as np


class treeNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)


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



# construct question tree
def constrct_question_tree():
    node_1 = treeNode("Do you want to watch an action movie?") 
    node_2 = treeNode("Do you want to watch an adventure movie?") 
    node_3 = treeNode("Do you want to watch an comedy movie?") 
    node_4 = treeNode("Do you want to watch an crime movie?") 
    node_5 = treeNode("Do you want to watch an drama movie?") 
    node_6 = treeNode("Do you want to watch an mystery movie?")
    node_7 = treeNode("Do you want to watch an romance movie?") 
    node_8 = treeNode("Do you want to watch an science fiction movie?") 
    node_9 = treeNode("Do you want to watch an thriller movie?")
    node_10 = treeNode("Do you want to watch an war movie?")
    node_1.right = node_2
    node_2.right = node_3
    node_3.right = node_4
    node_4.right = node_5
    node_5.right = node_6
    node_6.right = node_7
    node_7.right = node_8
    node_8.right = node_9
    node_9.right = node_10