import turtle

# turtle.showturtle()


def jump(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def forward(l):
    turtle.forward(l)


def right(a):
    turtle.right(a)


def begin_fill():
    turtle.begin_fill()


def fill_color(color):
    turtle.color(color)


def end_fill():
    turtle.end_fill()


def pause():
    turtle.done()

def left(a):
    turtle.left(a)