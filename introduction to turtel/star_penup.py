import turtle
turtle.Screen().bgcolor("purple")

sc=turtle.Screen()
sc.setup(400,300)
turtle.title("star pattern")

board=turtle.Turtle()
for i in range(3):
    board.forward(100)
    board.left(120)
    i+=1

board.penup()
board.right(90)

board.backward(50)
board.right(90)
board.pendown()

for j in range(3):
    board.backward(100)
    board.right(120)
    j+=1

turtle.done()