import tkinter as tk
from tkinter import messagebox
import random
import pygame

after_id = None

def move_button():
  condition = True
  while condition:
    nx = random.randint(0, 275)
    ny = random.randint(0, 275)
    if not ((110 < nx < 250) and (110 < ny < 190)):
      moving_button.place(x=nx, y=ny)
      condition = False


def show_message():
  pygame.init()
  pygame.mixer.music.load('hdd.wav')
  pygame.mixer.music.play()
  messagebox.showinfo('Question', "Do you really like this sound?")


def change_position(event):
  move_button()


def enter(event):
  global after_id
  blink()


def leave(event):
  static_button.config(bg = '#fc1717')
  global after_id
  if after_id:
    root.after_cancel(after_id)
  after_id = None


def blink():
  global after_id
  current_color = static_button.cget('bg')
  if current_color == '#fc1717':
    next_color = '#b00202'
  else:
    next_color = '#fc1717'
  static_button.config(bg = next_color)
  after_id = root.after(175, blink)


root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
crd_x = (width - 350) // 2
crd_y = (height - 350) // 2

root.title('Quiz')
root.geometry(f'350x350+{crd_x}+{crd_y}')
root.resizable(False, False)

button_font = ('Helvetica', 13)

moving_button = tk.Button(root, text='SSD', font=button_font, bg = 'green', fg = 'white')
moving_button.place(x=110, y=150)

static_button = tk.Button(root, text='HDD', command=show_message, font=button_font, bg = '#fc1717', fg = 'white')
static_button.place(x=180, y=150)

moving_button.bind('<Enter>', change_position)

static_button.bind('<Enter>', enter)
static_button.bind('<Leave>', leave)

root.mainloop()
