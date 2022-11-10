from turtle import Turtle,Screen, circle
import random

t = Turtle()
s = Screen()
# TASK 1:-
# drawing a square.
# for _ in range(1,5):
#     t.forward(100)
#     t.left(90)

# TASK 2:-
# drawing a dashed line.
# for _ in range(10):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.forward(10)

# ANOTHER SOLUTION:-
# for _ in range(10):
#     t.forward(10)
#     t.color('#fff')
#     t.forward(10)
#     t.color('#000')
#     t.speed(3)

# Task 3:-
# drawing a polygon.
# for _ in range(5):
#     t.forward(70)
#     t.right(72)
#     t.forward(70)

# TASK 4:-
# drawing a random path.
colors = ['red','green','blue','orange','purple','pink','yellow','cyan','black']
# direction = [0,90,180,270]
# for _ in range(100):
#     t.forward(20)
#     t.setheading(random.choice(direction))
#     t.color(random.choice(colors))
#     t.pensize(10)
#     t.speed('fastest')

# TASK 4:-
# draw circles
# for _ in range(50):
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 10)
#     t.speed('fastest')

# TASK 5:-
# create a painting dots.
# t.penup()
# t.hideturtle()
# for _ in range(5):
#     for _ in range(5):
#         t.dot(20,random.choice(colors),)
#         t.forward(20)
#         t.penup()
#         t.forward(20)
#     t.setheading(90)
#     t.forward(50)
#     t.setheading(180)
#     t.forward(200)
#     t.setheading(0)

    
# s.exitonclick()

#=======================================

# EVENT LISTENERS:-
# --------------- 
# TASK 1:-
# creating a drawing turtle that is control using keyboard keys.

# def move_forward():
#     t.forward(10)
#     t.speed('fastest')

# def move_backward():
#     t.backward(10)
#     t.speed('fastest')

# def turn_left():
#     t.left(10)
#     t.speed('fastest')

# def turn_right():
#     t.right(10)
#     t.speed('fastest')

# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()

# s.listen()
# s.onkey(fun=move_forward,key='f')
# s.onkey(fun=move_backward,key='b')
# s.onkey(fun=turn_left,key='l')
# s.onkey(fun=turn_right,key='r')
# s.onkey(fun=clear,key='c')


# TASK 2:-
# creating a turtle racing game.

guess = s.textinput(title='Turtle Race',prompt='Who will win?')
print(guess)
a = Turtle('turtle')
b = Turtle('turtle')
c = Turtle('turtle')

a.penup()
b.penup()
c.penup()

a.setheading(180)
a.penup()
a.forward(300)
a.setheading(0)
a.pendown()

b.setheading(180)
b.penup()
b.forward(300)
b.setheading(0)
b.pendown()

c.setheading(180)
c.penup()
c.forward(300)
c.setheading(0)
c.pendown()



a.speed('slowest')
b.speed('slowest')
c.speed('slowest')
a.color('red')
b.color('green')
b.color('purple')
a.setheading(90)
a.forward(20)
a.setheading(0)
c.setheading(90)
c.forward(40)
c.setheading(0)

for _ in range(10):
    a.forward(random.randint(1,100))
    b.forward(random.randint(1,100))
    c.forward(random.randint(1,100))

s.exitonclick()