def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def one_step():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
#for x in range(6):
#    one_step()
while not at_goal():
    if wall_in_front():
        one_step()
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
