import turtle
import pandas

screen=turtle.Screen()
screen.title('U.S states Game')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
timmy=turtle.Turtle()
timmy.penup()
timmy.hideturtle()
data=pandas.read_csv('50_states.csv')
answer=screen.textinput('Guess the State',"What's another state name")
row=data[data['state']==answer]
x=row['x']
y=row['y']
timmy.goto(x,y)
timmy.write(answer)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


screen.exitonclick()