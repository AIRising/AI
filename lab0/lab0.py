import math
import random

# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x**3

#print(cube(3))

def factorial(x):
    if x < 0:
        raise Exception ("factorial: input must not be negative")
    factorialNum=1;
    y = x
    while y>1:
        factorialNum *= y
        y -= 1
    return factorialNum

#print("Factorial of 4 is: ")
#print(factorial(4))

def count_pattern(pattern, lst):
    if (len(pattern) == 0) or (len(lst) == 0):
        raise Exception ("Cannot pass empty patterns or list into this function")
    if not isinstance(lst,(list,tuple)):
        return 0;
    lstLen = len(lst)
    patternMatches = 0
    patternMatch = False
    for index in range(lstLen - len(pattern) + 1):
        for patternIndex in range(len(pattern)):
            if (patternIndex + index) < lstLen:
                if(lst[patternIndex + index] == pattern[patternIndex]):
                    patternMatch = True
                else:
                    patternMatch = False
                    break
            else:
                patternMatch = False
        if patternMatch is True:
            patternMatches+=1
            patternMatch = False
    return patternMatches;

#print("This should return 0")
#print(count_pattern( ('a', 'b'), 'a'))
#print("This should return 2")
#print(count_pattern( ('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')))
#print("This should return 3")
#print(count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a','b', 'a')))


# Problem 2.2: Expression depth

def depthMapSolutionCheat(expr):
    if not isinstance(expr, (list, tuple)):
        return 0
    # this says: return the maximum depth of any sub-expression + 1
    return max(map(depthMapSolutionCheat, expr)) + 1

def depth(exp):
    if not isinstance(exp, (list, tuple)):
        return 0
    depthList = [0]
    for item in exp:
        godeeper(item, 1, depthList)
    return max(depthList)
        

def godeeper(exp, depthCount, depthList):
    depthList.append(depthCount)
    if not isinstance(exp, (list,tuple)):
        return
    for item in exp:
        godeeper(item, depthCount+1,depthList)
    return
    

#print("This should be 0")
#print(depth('x'));
#print("This should be 1")
#print(depth(('expt', 'x', 2)))
#print("This should be 2")
#print(depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))
#print("This should be 4")
#print(depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),
#1), ('/', 5, 2)))))
#print("This should be 1")
#print(depth([['expt', 'x', 2]]))
#print("This should be 3")
#print(depth([['+', ['expt', 'x', 2], ['expt', 'y', 2]]]))

def recursiveTest(someInt):
    someInt-=1;
    if(someInt <= 0):
        return 12
    return recursiveTest(someInt)

#print(recursiveTest(10))


# Problem 2.3: Tree indexing

class RandomTree:
    def __init__(self, treeData):
        self.children = []
        for subTree in treeData:
            if isinstance(subTree, (list, tuple)):
                self.children.append(RandomTree(subTree))
            else:
                self.children.append(subTree)

    def __getitem__(self,index):
        if isinstance(index, (list, tuple)):
            if(len(index) > 1):
                return self.children[index[0]][tuple([x for x in index if x != index[0]])]
            else:
                return self.children[index[0]]
        else:
            return self.children[index]

    def __str__(self):
        return "(%s)" % ", ".join(map(str,self.children))

def tree_ref(tree, index):
    randomTree = RandomTree(tree)
    return str(randomTree[index])        

#print("Tree in action should return 7")
#print(tree_ref((((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10)), (2)))
#print("Tree in action should return 9")
#print(tree_ref(tree, (3,1)))
#print("Tree in action should return (8, 9, 10)")
#print(tree_ref(tree, (3,)))
#print("Tree in action should return ((1, 2), 3))")
#print(tree_ref(tree, (0,)))

#sample_tree = [[[1, 2], 3], 7, [4, [5, 6]], [8, 9, 10]]
#randomIndex = random.randint(0,len(sample_tree)-1)
#print(tree_ref(sample_tree, randomIndex))

# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = ""

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = ""

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = ""

# How many hours did this lab take?
HOURS = ""
