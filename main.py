BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
ANSWER_TIME = 5
WORD ={}
WORDS_KNOWN = {}
TIMER = None
data_to_learn ={}

# try:
#    open("data/words_to_learn.csc") 

#----------------------------------known words----------------------#
def is_known():
   global WORD
   if WORD in modified_data:
      modified_data.remove(WORD)
      print(len(modified_data))
      data = pandas.DataFrame(modified_data)
      data.to_csv("data/words_to_learn.csv", index=False)
   next_card()

#----------------------------------known words----------------------#


def flip_card():
  canvas.itemconfig(old_image,image=card_b)
  canvas.itemconfig(language_text,text="English",fill="white")
  canvas.itemconfig(word_text,text=f"{WORD['English']}", fill="white")



#---------------------Start timer ----------------------------#
def count_down(count):
  if count > -1:
    global TIMER
    TIMER=window.after(1000, count_down, count-1)
    time.config(text=count)
  else:
    flip_card()

def start_timer():
  count = ANSWER_TIME
  count_down(count)
#---------------------Start timer ----------------------------#

#---------------------generate random word-----------#


def next_card():
  global TIMER,WORD,WORDS_KNOWN  # Declare after_id as a global variable

  if TIMER is not None:
        window.after_cancel(TIMER)
        
  WORD = random.choice(data_to_learn)
  canvas.itemconfig(word_text, text=f"{WORD['Swahili']}")
  canvas.itemconfig(old_image, image=card_f)
  canvas.itemconfig(language_text, text="Swahili", fill="black" )
  canvas.itemconfig(word_text, text=f"{WORD['Swahili']}", fill="black")
  start_timer()



#-------------------------------------UISETUP------------------------------#
window = Tk()
window.title("Learn Swahili")
window.config(bg=BACKGROUND_COLOR,padx=20,pady=20)

canvas = Canvas(width=800, height=560 ,highlightthickness=0,bg=BACKGROUND_COLOR)
card_f = PhotoImage(file="./images/card_front.png")
card_b  = PhotoImage(file="./images/card_back.png")
old_image=canvas.create_image(400, 280, image=card_f)
language_text=canvas.create_text(400, 180, text="Swahili",font=("Ariel",20,"normal"),)
word_text = canvas.create_text(400, 250, text="Word",font=("Arial", 32, "bold"),)
canvas.grid(row=1,column=0,columnspan=2)

timer_label = Label(text="Time Left",font=("Arial",30,"normal"),bg=BACKGROUND_COLOR,pady=0)
timer_label.grid(row=0,column=0)
time = Label(text="0", font=(
    "Arial", 30, "normal"), bg=BACKGROUND_COLOR, pady=0)
time.grid(row=0, column=1)

right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')

right_button = Button(image=right,highlightthickness=0,command=is_known)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)

right_button.grid(row=2,column=0)
wrong_button.grid(row=2, column=1)
#-------------------------------------UISETUP------------------------------#

#---------------READ FROM E CSV AND RANDOMLY DISPLAY WORDS------------------#
data = pandas.read_csv("./data/swahili-english.csv")
data_to_learn=data.to_dict(orient="records")
print(len(data_to_learn))
data_to_learn = data.to_dict(orient="records")
modified_data = data_to_learn.copy()


next_card()

window.mainloop()