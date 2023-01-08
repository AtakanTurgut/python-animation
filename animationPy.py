import turtle

turtle.bgcolor("grey")
turtle.pensize(2)
turtle.speed(0.50)
color = ["red", "blue", "green", "orange"]

for i in range(18):
    for j in color:
        turtle.color(j)
        turtle.circle(125)
        turtle.left(5)
        
turtle.mainloop()