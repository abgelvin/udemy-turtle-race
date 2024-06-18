from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Make your bet', prompt='Who will win the race?  Enter a color.')
colors = ['blue', 'red', 'green', 'purple', 'yellow', 'orange']
y_position = [-80, -45, -10, 25, 60, 95]

turtles = []

for i in range(len(colors)):
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_position[i])
    turtles.append(turtle)


def race(turtles):
    no_winner = True
    winner = None
    while no_winner:
        for turtle in turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance) 
            if turtle.xcor() > 215:
                winner = turtle.pencolor()
                no_winner = False
    if user_bet == winner:
        print('You win!')
    else:
        print('You lose.')
    print(f'The winner is {winner}')



race(turtles)




screen.exitonclick()