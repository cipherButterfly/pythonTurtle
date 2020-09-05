import turtle

pen = turtle.Pen()
pen2 = turtle.Pen()
screen = turtle.Screen()
screen.bgcolor('black')
pen.speed(30)
pen2.speed(30)
pen.pencolor('white')
pen2.pencolor('blue')
colors = ["white", "green", "blue", "pink"]

for i in range(0, 1001, 1):
    for j in range(0, 10):
        pen.forward(i)
        pen.left(i)
        pen2.back(i)
        pen2.right(i)






turtle.exitonclick()