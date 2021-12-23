###  Notes ###
### Name: Yonathan toledano ###

import turtle

def draw_petal():
#these commandes creates the shape of the petal
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
#this line makes the turtle face the same angle where he started
    turtle.right(135)
#draw_petal()

def draw_flower():
#these commandes usses the petal func in order to create 4 petals.
    turtle.right(-45)
    draw_petal()
    turtle.right(-90)
    draw_petal()
    turtle.right(-90)
    draw_petal()
    turtle.right(-90)
    draw_petal()
#these commandes draw the base of the flower
    turtle.right(-135)
    turtle.forward(150)
#draw_flower()

def draw_flower_and_advance():
    draw_flower()
    turtle.right(90)
#these commandes allow the turtle to move without drawing on the board.
    turtle.penup()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(-90)
    turtle.pendown()
#draw_flower_and_advance()

def draw_flower_bed():
#we will move the tutle to the right side of the board in order to draw three flowers
    turtle.penup()
    turtle.forward(200)
    turtle.right(180)
    turtle.pendown()
#by calling the flower_and_advance func three times we'll draw three flowers as needed
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()
#draw_flower_bed()

if __name__ == "__main__" :
    draw_flower_bed()
    turtle.done

#And now we're done :)