import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_series = data.state
states = states_series.tolist()
turtle = turtle.Turtle()
turtle.hideturtle()
score = 0
turtle.penup()
game_is_on = True
correct_guesses = []
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        row = data[data.state == answer_state]
        turtle.goto(int(row.x.item()), int(row.y.item()))
        turtle.write(arg=answer_state, align='center', font=('Arial', 5, 'normal'))
        score += 1
        correct_guesses.append(answer_state)
    if score == 50:
        game_is_on = False


missing_states = [state for state in states if state not in correct_guesses]

learning_data = pandas.DataFrame(missing_states)
learning_data.to_csv("learn.csv")
print(learning_data)




