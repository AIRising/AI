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

def cube(n):
    return n**3

#print("cube(3) = ", cube(3))

def factorial(n):
    if n > 0:
        temp = 1
        for i in range(n):
            temp *= n - i
        return temp

    elif n == 0:
        return 1;
    else:
        raise Exception; "factorial: input must not be negative!"

#print("factorial(3) = ", factorial(3))
#print("factorial(0) = ", factorial(0))
#print("factorial(-1) = ", factorial(-1))

def count_pattern(pattern, lst):
    total = 0

    for i in range( len(lst)-(len(pattern)-1) ):
        temp_list = []
        for j in range(len(pattern)):
            temp_list.append(lst[i+j])

        match_count = 0
        for k in range(len(temp_list)):
            if pattern[k] == temp_list[k]:
                match_count += 1

        if match_count == len(pattern):

            total += 1

    return total

list_1 = ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')
list_2 = ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')

#print( count_pattern( ('a', 'b'), list_1 ) )
#print( count_pattern( ('a', 'b', 'a'), list_2 ) )

print("tests_1", count_pattern([2,3], [1,2,3,2,3,4,3,4,5]))
print("tests_2", count_pattern([1, [2,3]], [1, [2,3], 2, 3, 1, [2,3,4]]))
# Problem 2.2: Expression depth

def depth(expr):
    if not isinstance(expr, (list, tuple)):
        return 0
    else:
        depth = 0;
        print("Next Expression!")
        for anyItem in expr:
            print(anyItem)
        return depth

print("This should be 0")
print(depth('x'));
print("This should be 1")
print(depth(('expt', 'x', 2)))
print("This should be 2")
print(depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))
print("This should be 4")
print(depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),
1), ('/', 5, 2)))))


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    return 0


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
