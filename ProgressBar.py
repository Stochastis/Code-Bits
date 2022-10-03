from tkinter import *
from tkinter.ttk import Progressbar
import time

pps = 14/3600


def step():
    for i in range(6200):
        ws.update_idletasks()
        pb['value'] += 1
        time.sleep(1)
        txt['text'] = "$" + str(round(pb['value']*pps, 2))


ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x150')
ws.config(bg='#345')


pb = Progressbar(
    ws,
    orient=HORIZONTAL,
    length=100,
    mode='determinate',
    maximum=500
)

pb['value'] = 1000

pb.place(x=40, y=20)

txt = Label(
    ws,
    text='$0.00',
    bg='#345',
    fg='#fff'

)

txt.place(x=150, y=20)

Button(
    ws,
    text='Start',
    command=step
).place(x=40, y=50)

ws.mainloop()
