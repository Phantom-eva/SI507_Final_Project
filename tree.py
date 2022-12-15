import numpy as np


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
        new_str = tree.data
        ans_1 = yes(new_str)
        return ans_1
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
    question_1 = treeNode("Do you want to watch an action movie?") 
    question_2 = treeNode("Do you want to watch an horror movie?") 
    question_3 = treeNode("Do you want to watch an adventure movie?") 
    question_4 = treeNode("Do you want to watch an comedy movie?") 
    question_5 = treeNode("Do you want to watch an science fiction movie?")
    question_6 = treeNode("Do you want to watch a movie longer than 120 minutes?")
    question_7 = treeNode("Do you want to watch a movie released after 2018?")
    question_1.right = question_2
    question_1.left = question_6
    question_2.right = question_3
    question_2.left = question_6
    question_3.right = question_4
    question_3.left = question_6
    question_4.right = question_5
    question_4.left = question_6
    question_5.right = question_6
    question_5.left = question_6
    question_6.left = question_7
    question_6.right = question_7
    return question_1


Movie_list = {}



def construct_movie_tree():
    movienode_1 = treeNode(Movie_list['all'])
    movienode_2 = treeNode(Movie_list['Action'])
    movienode_3 = treeNode(Movie_list['not Action'])
    movienode_4 = treeNode(Movie_list['Adventure'])
    movienode_1.left = movienode_2
    movienode_1.right = movienode_3


# def main():
#     q_1 = constrct_question_tree()
#     simplePlay(q_1)



# if __name__ == "__main__":
#     main()