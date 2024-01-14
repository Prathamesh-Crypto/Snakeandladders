import turtle
import random
import time

#Screen Setup
win = turtle.Screen()
#win.bgcolor("black")
win.addshape('sandl.gif')

#Adding the Image
img = turtle.Turtle()
img.shape('sandl.gif')

steps = 1

#Player 1

p1 = turtle.Turtle()
p1.shape('circle')
p1.color('blue')
p1.width(2)
p1.speed(2)
p1.up() # move the hashtag to the begining of this sentence if u want to see the tails of the pawn
p1.goto(-252, -252) #Square 1

# DICE 

D = turtle.Turtle()
Ds = turtle.Turtle()
Dice = ''
D.color("black")
D.hideturtle()
D.up()
D.speed(0)
D.goto(0,-350)

Ds.speed(0)
Ds.hideturtle()
Ds.up()
Ds.goto(-150,-300)
Ds.down()
for i in range(2):
    Ds.forward(100)
    Ds.right(45)
    Ds.forward(5)
    Ds.right(45)
    Ds.forward(50)
    Ds.right(45)
    Ds.forward(5)
    Ds.right(45)

Ds.up()
Ds.goto(-145,-345)
Ds.left(90)
Ds.write("Reroll",font=("Courier",20,'bold'))
 
#Functionality ---

def Main_game(x,y):
    global steps

    table = {1: (-252, -252),
         2: (-196, -252),
         3: (-140, -252),
         4: (-84, -252),
         5: (-28, -252),
         6: (28, -252),
         7: (84, -252),
         8: (140, -252),
         9: (196, -252),
         10: (252, -252),
         
         11: (252, -196),
         12: (196, -196),
         13: (140, -196),
         14: (84, -196),
         15: (28, -196),
         16: (-28, -196),
         17: (-84, -196),
         18: (-140, -196),
         19: (-196, -196),
         20: (-252, -196),
         
         21: (-252, -140),
         22: (-196, -140),
         23: (-140, -140),
         24: (-84, -140),
         25: (-28, -140),
         26: (28, -140),
         27: (84, -140),
         28: (140, -140),
         29: (196, -140),
         30: (252, -140),
         
         31: (252, -84),
         32: (196, -84),
         33: (140, -84),
         34: (84, -84),
         35: (28, -84),
         36: (-28, -84),
         37: (-84, -84),
         38: (-140, -84),
         39: (-196, -84),
         40: (-252, -84),
         
         41: (-252, -28),
         42: (-196, -28),
         43: (-140, -28),
         44: (-84, -28),
         45: (-28, -28),
         46: (28, -28),
         47: (84, -28),
         48: (140, -28),
         49: (196, -28),
         50: (252, -28),
         
         51: (252, 28),
         52: (196, 28),
         53: (140, 28),
         54: (84, 28),
         55: (28, 28),
         56: (-28, 28),
         57: (-84, 28),
         58: (-140, 28),
         59: (-196, 28),
         60: (-252, 28),
         
         61: (-252, 84),
         62: (-196, 84),
         63: (-140, 84),
         64: (-84, 84),
         65: (-28, 84),
         66: (28, 84),
         67: (84, 84),
         68: (140, 84),
         69: (196, 84),
         70: (252, 84),
         
         71: (252, 140),
         72: (196, 140),
         73: (140, 140),
         74: (84, 140),
         75: (28, 140),
         76: (-28, 140),
         77: (-84, 140),
         78: (-140, 140),
         79: (-196, 140),
         80: (-252, 140),
         
         81: (-252, 196),
         82: (-196, 196),
         83: (-140, 196),
         84: (-84, 196),
         85: (-28, 196),
         86: (28, 196),
         87: (84, 196),
         88: (140, 196),
         89: (196, 196),
         90: (252, 196),
         
         91: (252, 252),
         92: (196, 252),
         93: (140, 252),
         94: (84, 252),
         95: (28, 252),
         96: (-28, 252),
         97: (-84, 252),
         98: (-140, 252),
         99: (-196, 252),
         100: (-252, 252)}
    
    snake = {
         28: (252, -252),
         37: (-140, -252),
         47: (-28, -196),
         75: (196, -84),
         94: (252, 140),
         96: (-196, -28),
    } #28, 37, 47, 75, 94, 96

    if (x > -154 and x < -47 and y > -357 and y < -300):
        D.clear()
        Dice = random.randint(1,6)
        D.write(Dice,font=("Courier",20,'bold'))
        steps = steps + Dice
        if steps > 100:
            D.clear()
            steps = steps - Dice
            D.write("Invalid the the rolled number is higher than the distance needed to reach 100, please reroll",font=("Courier",20,'bold'))
        time. sleep(0.5)
        print(steps)
        p1.goto(table[steps])

        if steps == 100:
            D.clear()
            D.write("YOU WIN !!!!",font=("Courier",20,'bold'))
            
    '''if steps in snake :
        print("Snake")
        p1.goto(table[steps])
        p1.speed(5)
        p1.goto(snake[steps])
        for i in table:
            if i == p1.pos():
                steps = i'''
    
    #snakes --/--
    if steps == 28: #28
        print("Snake")
        p1.speed(3)
        p1.goto(table[10])
        p1.speed(2)
        steps = 10
        time. sleep(0.5)
    
    if steps == 37: #37
        print("Snake")
        p1.speed(3)
        p1.goto(table[3])
        p1.speed(2)
        steps = 3
        time. sleep(0.5)

    if steps == 47: #47
        print("Snake")
        p1.speed(3)
        p1.goto(table[16])
        p1.speed(2)
        steps = 16
        time. sleep(0.5)

    if steps == 75: #75
        print("Snake")
        p1.speed(3)
        p1.goto(table[32])
        p1.speed(2)
        steps = 32
        time. sleep(0.5)

    if steps == 94: #94
        print("Snake")
        p1.speed(3)
        p1.goto(table[71]) 
        p1.speed(2)
        steps = 71
        time. sleep(0.5)

    if steps == 96: #96
        print("Snake")
        p1.speed(3)
        p1.goto(table[42]) 
        p1.speed(2)
        steps = 42
        time. sleep(0.5)

    #Ladders --/--
    if steps == 4: #28
        print("Ladder")
        p1.speed(3)
        p1.goto(table[56])
        p1.speed(2)
        steps = 56
        time. sleep(0.5)
    
    if steps == 12: #37
        print("Ladder")
        p1.speed(3)
        p1.goto(table[50])
        p1.speed(2)
        steps = 50
        time. sleep(0.5)

    if steps == 14: #47
        print("Ladder")
        p1.speed(3)
        p1.goto(table[55])
        p1.speed(2)
        steps = 55
        time. sleep(0.5)

    if steps == 22: #75
        print("Ladder")
        p1.speed(3)
        p1.goto(table[58])
        p1.speed(2)
        steps = 58
        time. sleep(0.5)

    if steps == 41: #94
        print("Ladder")
        p1.speed(3)
        p1.goto(table[79]) 
        p1.speed(2)
        steps = 79
        time. sleep(0.5)

    if steps == 54: #96
        print("Ladder")
        p1.speed(3)
        p1.goto(table[88]) 
        p1.speed(2)
        steps = 88
        time. sleep(0.5)

# Tools -----

''' 
WHOLE GRID IS 540x540 pixels
1block is of 280/5 pixels and half of 1 block is 28 pixels

10-11 20-21 30-31 40-41 50-51 60-61 70-71 80-81 90-91 100
'''

def get_mouse_coords(x,y):
   print(x,y)
#turtle.onscreenclick(get_mouse_coords)

#print(p1.position())
turtle.onscreenclick(Main_game)
turtle.mainloop()