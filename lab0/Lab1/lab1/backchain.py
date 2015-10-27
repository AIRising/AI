from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    orExpression = OR(hypothesis)
    for rule in rules:
        for expression in rule.consequent():
            thisMatch = match(expression, hypothesis)
            if(thisMatch):
                for antecedantExpression in rule.antecedent():
                    orExpression.append(backchain_to_goal_tree(rules, antecedantExpression))
    return orExpression

# Here's an example of running the backward chainer - uncomment
# it to see it work:
print(backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin'))


#OR(
# 'opus is a penguin',
# AND(
# OR('opus is a bird', 'opus has feathers', AND('opus flies', 'opus
#lays eggs'))
# 'opus does not fly',
# 'opus swims',
# 'opus has black and white color' ))