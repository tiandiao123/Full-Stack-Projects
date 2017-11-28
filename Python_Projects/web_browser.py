import webbrowser
import os
import turtle

def open_youtube():
	webbrowser.open("https://www.youtube.com/")


def rename_files():
	file_list = os.listdir("/home/lixx3527/Desktop")
	print(file_list)



def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	window.exitonclick()


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(250)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()