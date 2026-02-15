import turtle
turtle.Screen().bgcolor("pink")

sc=turtle.Screen()
sc.setup(400,300)
turtle.title("plygon on a canvas")
board=turtle.Turtle()
for i in range(6):
    board.forward(100)
    board.right(60)
    i+=1
turtle.done()