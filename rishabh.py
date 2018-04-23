''' this game is developed by Rishabh Sharma using python and some modules
this is on git hub as repros. sharmarishabh54\racing game  '''


# set up a screen
import turtle
import os
import pygame
import time
from random import randint

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((640, 480))

def playNotificationSound():
    pygame.mixer.music.load("atlanta.wav")
    pygame.mixer.music.play()

playNotificationSound()

	
# create one more turtle to set player name
l=turtle.Turtle()
l.shape('circle')
l.penup()
l.setpos(-50,-300)
l.pendown()
l.pencolor('darkorange')
l.write('PLAYER 1',font=('Arial',20,'normal'))
l.penup()
l.hideturtle()
l.setpos(-260,-300)
l.pendown()
l.write('PLAYER 3',font=('Arial',20,'normal'))
l.penup()
l.setpos(160,-300)
l.pendown()
l.write('PLAYER 2',font=('Arial',20,'normal'))
l.penup()




screen = turtle.Screen()

image = "car.gif"
image1 = "car1.gif"
image2 = "car.gif"


screen.addshape(image)
screen.addshape(image1)
screen.addshape(image2)

w=turtle.Screen()
w.bgcolor('white')
w.title('CAR RACING GAME')


d=randint(1,5)
# draw a border 
b=turtle.Turtle()
b.speed(0)
b.pencolor('grey')
b.penup()
b.setposition(-300,-300)
b.pendown()
b.pensize(3)

# take one for turtle for anouncing winner
g=turtle.Turtle()
g.pencolor('blue')
g.hideturtle()

for side in range(4):
    
    b.fd(600)
    b.left(90)


b.hideturtle()

line=turtle.Turtle()

line.shape('circle')
line.speed(0)


line.color('black')
line.pensize(5)
line.penup()
line.setpos(-100,-300)
line.pendown()
line.setheading(90)
for repeat in range(12):
    line.fd(20)
    line.penup()
    line.fd(10)
    line.pendown()
    line.fd(20)
line.hideturtle()
line.penup()
line.setpos(100,-300)
line.pendown()
for repeat in range(12):
    line.fd(20)
    line.penup()
    line.fd(10)
    line.pendown()
    line.fd(20)
line.hideturtle()
line.hideturtle()


# create the car

car1=turtle.Turtle()
car1.shape(image)
car1.penup()
car1.speed(0)
car1.setheading(90)
car1.setpos(-00,-300)
car1.shapesize(-2,2)

car2=turtle.Turtle()
car2.shape(image1)
car2.penup()
car2.speed(0)
car2.setheading(90)
car2.setpos(160,-300)
car2.shapesize(-2,2)

car3=turtle.Turtle()
car3.shape(image2)

car3.penup()
car3.speed(0)
car3.setheading(90)
car3.setpos(-160,-300)
car3.shapesize(-2,2)


l.setpos(-140,00)
l.write('game will start in 5 seconds',font=('Arial',20,'normal'))
l.hideturtle()
time.sleep(5)
l.clear()


# set random speed of other cars
q=randint(0,20)
r=randint(1,20)
# move the car 
car1speed=20
car2speed=q
car3speed=r
def move_up():
    y= car1.ycor()
    y=y+car1speed
    car1.sety(y)
    

#creat keyboard bindings
turtle.listen()
turtle.onkey(move_up,'Up')
# put the oponent cars in a loop
for  turn in range(200):
    car2.forward(randint(1,5))
    car3.forward(randint(1,5))

a1=car1.pos()
b1=car2.pos()
c1=car3.pos()
if a1[1]>b1[1] and a1[1]>c1[1]:
        g.pensize(4)

        g.penup()
        g.setpos(-140,-80)
        g.pendown()
        
        g.write("YOU WON",font=('Arial',50,'normal'))
        g.hideturtle()
elif(b1[1]>a1[1] and b1[1]>c1[1]):
    g.pensize(4)
    g.penup()
    g.setpos(-140,-80)
    g.pendown()
    g.write('YOU LOSE',font=('Arial',50,'normal'))
    g.penup()
    g.pencolor('cyan')
    g.setpos(-180,-140)
    g.write('PLAYER 2 IS WINNER',font=('Arial',35,'normal'))
    g.hideturtle()

else:
    g.pensize(4)
    g.penup()
    g.setpos(-140,-80)
    g.pendown()
    g.write('YOU LOSE',font=('Arial',50,'normal'))
    g.penup()
    g.pencolor('cyan')
    g.setpos(-180,-140)
    g.write('PLAYER 3 IS WINNER',font=('Arial',35,'normal'))
    g.hideturtle()
    
   
w.exitonclick()
