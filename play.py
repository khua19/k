import turtle

window = turtle.Screen()

play=turtle.Turtle()

for i in range(25):
    play.forward(100)
    play.right(108)
    play.forward(100)
    play.left(108)
    play.forward(100)
    play.right(108)
    play.forward(100)
    play.right(100)

window.exitonclick()
