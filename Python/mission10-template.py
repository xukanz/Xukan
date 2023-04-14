#
# CS1010S --- Programming Methodology
#
# Mission 10 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.


####################
# Helper functions #
# - print_tree     #
# - accumulate     #
####################

def print_tree(tree, print_output=True):
    """
    Helper function to print trees in this mission.

    Yes, it looks scary. Nothing to see here (:
    """
    def get_elements_at_level(tree, level):
        def helper(tree, level, cur):
            if is_empty_tree(tree) and cur < level:
                dummy = build_tree(" ", make_empty_tree(), make_empty_tree())
                return helper(left_branch(dummy), level, cur + 1) + helper(right_branch(dummy), level, cur + 1)
            if cur == level:
                if is_empty_tree(tree):
                    return (" ", )
                else:
                    return (entry(tree), )
            elif cur < level:
                return helper(left_branch(tree), level, cur + 1) + helper(right_branch(tree), level, cur + 1)
        return helper(tree, level, 0)

    def height(tree):
        if is_empty_tree(tree):
            return 0
        else:
            return 1 + max(height(left_branch(tree)), height(right_branch(tree)))

    h = height(tree)
    output_string = ""

    for level in range(h):
        indent = 2 ** (h - (level + 1)) - 1
        spacing = 2 ** (h - level) - 1

        output = " " * indent

        for i, e in enumerate(get_elements_at_level(tree, level)):
            if level == 0 or i == 0:
                output = output + str(e)
            else:
                output = output + " " * spacing + str(e)
        if print_output:
            print(output)
        else:
            output_string += output + '/'
    if not print_output:
        return output_string

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))


###########
# Task 1a #
###########

def build_tree(entry, left, right):
    # Your code here
    return [left,entry,right]


###########
# Task 1b #
###########

def entry(tree):
    if tree!=make_empty_tree():
        return tree[1]

def left_branch(tree):
    if tree!=make_empty_tree():
        return tree[0]


def right_branch(tree):
    if tree!=make_empty_tree():
        return tree[2]


###########
# Task 1c #
###########

def make_empty_tree():
    # Your code here
    return []


###########
# Task 1d #
###########

def is_empty_tree(tree):
    if tree==make_empty_tree():
        return True
    else:
        return False

t1 = build_tree(2, build_tree(1, make_empty_tree(),
                                 make_empty_tree()),
                   build_tree(3, make_empty_tree(),
                                 make_empty_tree()))
print_tree(t1)
#=> 2
#=>1 3

t2 = build_tree(5, build_tree(2, build_tree(1, make_empty_tree(),
                                               make_empty_tree()),
                                 make_empty_tree()),
                   build_tree(7, make_empty_tree(),
                                 build_tree(10, make_empty_tree(),
                                                make_empty_tree())))
print_tree(t2)
#=>   5
#=> 2   7
#=>1     10


###########
# Task 2a #
###########

def insert_tree(x, tree):
    if tree==make_empty_tree():
        return build_tree(x,make_empty_tree(),make_empty_tree())
    else:
        if x<=entry(tree):
            return build_tree(entry(tree),insert_tree(x,left_branch(tree)),right_branch(tree))
        else:
            return build_tree(entry(tree),left_branch(tree),insert_tree(x,right_branch(tree)))
           

t1 = insert_tree(5, t1)
print_tree(t1)
#=> 2           insert_tree(5, t1)        2
#=>1 3               ===>               1   3
#=>                                          5

t2 = insert_tree(6, t2)
print_tree(t2)
#=>   5         insert_tree(6, t2)        5
#=> 2   7            ===>               2   7
#=>1     10                            1   6 10

t2 = insert_tree(3, t2)
print_tree(t2)
#=>   5         insert_tree(3, t2)        5
#=> 2   7            ===>               2   7
#=>1   6 10                            1 3 6 10


###########
# Task 2b #
###########

# Time complexity of insert_tree: O(log n), where n is the number of branches of the tree
# Explanation: insert_tree function is recursively called for log2 n times until the left branch or right branch is empty



###########
# Task 2c #
###########

def contains(x, tree):
    if tree==make_empty_tree():
        return False
    elif x==entry(tree):
        return True
    elif x<entry(tree):
        return contains(x,left_branch(tree))
    else:
        return contains(x,right_branch(tree))
    

print(contains(1, t1))
#=> True

print(contains(5, t1))
#=> True

print(contains(42, t1))
#=> False

print(contains(10, t2))
#=> True

print(contains(6, t2))
#=> True

print(contains(11, t2))
#=> False


###########
# Task 2d #
###########

# Time complexity of contains: O(log n)
# Explanation: insert_tree function is recursively called for log2 n times until x equals to entry



###########
# Task 2e #
###########

def flatten(tree):
    if tree==make_empty_tree():
        return []
    elif left_branch(tree)==make_empty_tree() and right_branch(tree)==make_empty_tree():
        return [entry(tree)]
    else:
        return flatten(left_branch(tree))+[entry(tree)]+flatten(right_branch(tree))

print(flatten(t1))
#=> [1, 2, 3, 5]

print(flatten(t2))
#=> [1, 2, 3, 5, 6, 7, 10]


###########
# Task 2f #
###########

# Time complexity of flatten: O(n*(2**n)),where n is the number of branches
# Explanation: for every recursive step, flatten function is called for 2 times, resulting in a time complexity of 2**n, concatenation has a time complexity of n



###########
# Task 3a #
###########

def sort_it(lst):
    tree=accumulate(insert_tree,make_empty_tree(),lst)
    return flatten(tree)

print(sort_it([5, 3, 2, 1, 4, 6, 7, 9]))
#=> [1, 2, 3, 4, 5, 6, 7, 9]

print(sort_it([5, 3, 2, 1, 4, -1, 6, 0, 7, 9]))
#=> [-1, 0, 1, 2, 3, 4, 5, 6, 7, 9]


###########
# Task 3b #
###########

# Time complexity of sort_it: O(n*(2**n)),where n is the length of list
# Explanation: flatten function is called in the return statement
