from turtle import Turtle, Screen


tina = Turtle()
screen = Screen()


def move_forward():
    tina.forward(10)


def move_backward():
    tina.backward(10)


def turn_right():
    tina.right(10)


def turn_left():
    tina.left(10)


def clear():
    tina.clear()
    tina.penup()
    tina.home()
    tina.pendown()


screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear, key="c")



screen.exitonclick()
