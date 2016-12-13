import turtle

window = turtle.Screen()

kim = turtle.Turtle()
kim.pensize(30)
kim.left(90)
kim.forward(300)
kim.backward(150)
kim.right(45)
kim.forward(208)
kim.backward(208)
kim.right(90)
kim.forward(208)
kim.backward(208)
kim.penup()
kim.right(45)
kim.forward(150)
kim.left(90)
kim.forward(200)
kim.pendown()
kim.left(90)
kim.forward(150)
kim.penup()
kim.forward(50)
kim.pendown()
kim.forward(10)
kim.backward(10)
kim.penup()
kim.backward(200)
kim.right(90)
kim.forward(70)
kim.left(90)
kim.pendown()
kim.forward(150)
kim.backward(40)

for i in range(25):
    kim.right(7)
    kim.forward(5)

kim.right(4)
kim.forward(75)
kim.backward(75)
kim.right(180)

for i in range(26):
    kim.right(7)
    kim.forward(5)

kim.left(2)

kim.forward(100)

window.exitonclick()
