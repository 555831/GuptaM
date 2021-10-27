#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)
x.circle(20)
legs = 8
length = 120
distance_between_legs = 360 / legs
x.pensize(5)
number_of_legs = 0
while (number_of_legs < legs):
  x.goto(0,0)
  x.setheading(distance_between_legs*number_of_legs)
  x.forward(length)
  number_of_legs = number_of_legs + 1
x.hideturtle()
wn = trtl.Screen()