def turn_around():
    turn_left();
    turn_left();
 

    
turn_right()

for i in range(1,7):  
    move()
    jump()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

i=1
while i<=6:
    move()
    jump();
    i+=1




def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    


while not at_goal():
    move()
    jump()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    


while at_goal!=True:
    if(wall_in_front()):
        jump()
    else:
        move()



def jump():
    turn_left()
    while(wall_on_right() and not wall_in_front()):
        move()
    turn_right()
    if(front_is_clear()):
        move()
    turn_right()
    if(front_is_clear()):
        move()
    while(wall_on_right() and not wall_in_front()):
        move()
    turn_left()
    
while at_goal()!=True:
    if(right_is_clear() and front_is_clear()):
        move()
    elif(wall_in_front()):
       turn_right()
    else:
        jump()