from tkinter import *
import random

# Змінні, типу константи. Не будуть змінюватись
GAME_WIDTH = 1000
GAME_HEIGHT = 1000
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BG_COLOR = '#000000'


class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title('Змійка')
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text='Score: {}'.format(score), font=('consolas', 40))
label.pack()

window.mainloop()
