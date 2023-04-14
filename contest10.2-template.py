#
# CS1010S --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *


def AI(mat):
    # replace the following line with your code
    lst=[]
    origin_1=mat
    origin_2=mat
    origin_3=mat
    left=merge_left(mat)
    right=merge_right(origin_1)
    up=merge_up(origin_2)
    down=merge_down(origin_3)
    if left[1]==True:
        lst.append(left[2])
    if right[1]==True:
        lst.append(right[2])
    if up[1]==True:
        lst.append(up[2])
    if down[1]==True:
        lst.append(down[2])
    best=max(lst)
    if left[1]==True and left[2]==best:
        return 'a'
    if right[1]==True and right[2]==best:
        return 'd'
    if up[1]==True and up[2]==best:
        return 'w'
    if down[1]==True and down[2]==best:
        return 's'
    if left[1]==False and right[1]==False and up[1]==False and down[1]==False:
    #def helper_1():
        #return 
        return ('w', 'a', 's', 'd')[randint(0,3)]


# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
game_logic['AI'] = AI
gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
get_average_AI_score(AI, True)
