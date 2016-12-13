import turtle
turtle.setup(width=600, height=500)
turtle.bgcolor("blue")
turtle.reset()
turtle.hideturtle()
turtle.speed(0)
for i in range(1000):
turtle.forward(i)
turtle.right(98)

turtle.exitonclick()
