import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S states Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
data = pandas.read_csv('50_states.csv')
# print(answer)
# print(row)
# x=int(row.x)
# y=int(row.y)
# print(x)
# correct = 0
all_states=data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        f'{len(guessed_states)}/50 States Correct', "What's another state name").title()
    row = data[data['state']==answer]
    if(answer=='Exit'):
        break
    if (not row.empty):
        timmy.goto(int(row.x), int(row.y))
        timmy.write(answer, False, 'center', ('Arial', 10, 'bold'))
        # correct += 1
        guessed_states.append(answer)
        
learn_states=[state for state in all_states if not state in guessed_states]
# for state in all_states:
#     if not state in guessed_states:
#         learn_states.append(state)

dic={
    "state":learn_states
}
# print(learn_states)
learn=pandas.DataFrame(dic)
learn.to_csv('vancho_states')
# if guessed_states
# serires.item()
# gets the first value of column in the series
# def get_mouse_click_coor(x,y):g
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


# screen.exitonclick()
