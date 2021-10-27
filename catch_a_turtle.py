# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

import random as rand



#-----game configuration----
spot_size = 2
spot_color = "pink"
spot_shape = "circle"
global score
score = 0


#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.color(spot_color)


#-----game functions--------
def spot_clicked(x,y):
  change_position()
 
  

def change_position():
  spot.hideturtle()
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()

def update_score():
  global score
  score = score + 1
  print(score)
  


#-----events----------------
spot.penup()
spot.onclick(spot_clicked)





wn = trtl.Screen()
wn.mainloop()