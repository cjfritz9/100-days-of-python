from tkinter import *
from math import floor
from PIL import Image, ImageTk
import os, sys
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
HEADING_FONT = ("Sans", 38, "bold")
COUNTDOWN_FONT = ("Sans", 35, "bold")
CHECK_FONT = ("Courier", 24, "bold")
CHECKMARK = "✔️"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- COMPILE HELPERS ------------------------------- #
if getattr(sys, 'frozen', False):
  import pyi_splash
  pyi_splash.close()

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  
  except Exception:
    base_path = os.path.dirname(os.path.abspath(__file__))

  # print(os.path.join(base_path, relative_path))
  return os.path.join(base_path, relative_path)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global reps

  reps = 0
  heading_label.config(text="Timer", fg=GREEN)
  checkmark_label["text"] = ""
  canvas.itemconfig(countdown_text_shadow, text="25:00")
  canvas.itemconfig(countdown_text, text="25:00")
  window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps

  window.attributes('-topmost', True)

  reps += 1

  if reps == 9:
    reps = 1

  if reps % 8 == 0:
    heading_label.config(text="Long break! 🍵", fg=RED)
    countdown(LONG_BREAK_MIN * 60)
    checkmark_label["text"] = ""
  elif reps % 2 == 0:
    heading_label.config(text="Short break! 🧘", fg=PINK)
    countdown(SHORT_BREAK_MIN * 60)
  else:
    heading_label.config(text="Work! 💻", fg=GREEN)
    countdown(WORK_MIN * 60)
    checkmarks = CHECKMARK
    for _ in range(floor(reps / 2)):
      checkmarks += CHECKMARK
    checkmark_label["text"] = checkmarks

  window.focus_force()
  window.attributes('-topmost', False)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
  global reps

  minutes = floor(count / 60)
  seconds = count % 60
  if seconds < 10:
    seconds = f"0{seconds}"
    
  remaining_time = f"{minutes}:{seconds}"
  canvas.itemconfig(countdown_text, text=remaining_time)
  canvas.itemconfig(countdown_text_shadow, text=remaining_time)
  if count > 0:
    global timer
    timer = window.after(1000, countdown, count - 1)
  else:
    start_timer()

# ---------------------------- UI SETUP ------------------------------- #

# ------------------ WINDOW --------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# ------------------ CANVAS --------------------- #
canvas = Canvas(width=460, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = Image.open(resource_path('tomato.png'))
tomato_img = ImageTk.PhotoImage(tomato_img)
canvas.create_image(230, 120, image=tomato_img)
countdown_text_shadow = canvas.create_text(231, 132, text="00:00", font=COUNTDOWN_FONT)
countdown_text = canvas.create_text(231, 130, text="00:00", font=COUNTDOWN_FONT, fill="white")
canvas.grid(column=1, row=1)

# ------------------ LABELS --------------------- #
heading_label = Label(text="Timer", font=HEADING_FONT, fg=GREEN, bg=YELLOW)
heading_label.grid(column=1, row=0)

checkmark_label = Label(text="", font=CHECK_FONT, fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=5)

# ------------------ BUTTONS --------------------- #
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=2)

# ------------------ LOOP --------------------- #
window.mainloop()