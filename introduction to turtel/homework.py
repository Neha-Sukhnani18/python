import turtle

def draw_triangle(t, size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(3):
        t.forward(size)
        t.left(120)
def draw_rectangle(t, width, height, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_hexagon(t, size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(6):
        t.forward(size)
        t.left(60)
def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.title("Shapes with Turtle")
my_turtle = turtle.Turtle()
my_turtle.speed(2)
draw_triangle(my_turtle, 100, -250, 50)
draw_rectangle(my_turtle, 150, 75, -50, 50)
draw_hexagon(my_turtle, 60, 150, 50)
my_turtle.hideturtle()
screen.exitonclick()
if __name__ == "__main__":
    main()
    