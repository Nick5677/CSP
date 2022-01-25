# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
fillcolor= input("choose color ")
painter.begin_fill()

# create the robot head
painter.pensize(4)

painter.setheading(45)
painter.fillcolor(fillcolor)
painter.circle(70,360,4)
painter.end_fill()

painter.penup ()
painter.goto(-80,40)

# create the robot mouth
fillcolor= input("choose color ")
painter.begin_fill()

painter.pendown ()
painter.pensize(3)

painter.setheading(40)
painter.fillcolor(fillcolor)
painter.circle(40,360,4)
painter.end_fill()





# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()