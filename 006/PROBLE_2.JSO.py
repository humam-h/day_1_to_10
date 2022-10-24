def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_right()
            move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
    
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
