import turtle
import pandas

screen = turtle.Screen()
screen.title = "U.S States Game."

image = "./find_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)





states_info = pandas.read_csv("./find_states_game/50_states.csv")
states_list = states_info["state"].to_list()
guessed_states = []

while len(guessed_states) < len(states_list):
    answer_input = screen.textinput("Guess the State",
                                    "What is the another state's name?").title()

    if answer_input == "Exit":
        # missing_sates = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_sates.append(state)
        # new_data = pandas.DataFrame(missing_sates)
        # new_data.to_csv("./find_states_game/states_to_learn.csv")
        # break
    
        missing_sates = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_sates)
        new_data.to_csv("./find_states_game/states_to_learn.csv")
        break
    
    if answer_input in states_list:
        guessed_states.append(answer_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_info[states_info.state == answer_input]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_input)
    
screen.exitonclick()

