from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Прога Наримана')
frame=Frame(window)
entry=Entry(frame)
def tog():
    if window.cget('bg')=='#FF1493':
        window.config(bg ='#00FFFF')
    else:
        window.config(bg = '#90EE90')
def dialog():
    box.showinfo('GREETING', 'WELCOME'+entry.get())
btn = Button(frame, text='ВВЕДИ ИМЯ', command=dialog)

btn=Button(window, text='click', command=dialog)
btn.pack(padx=150, pady=20)


btn_end = Button(window, text='close', command=exit)
btn_tog = Button(window, text='switch', command=tog )
btn_tog.pack(padx=150, pady=20)
btn_end.pack(padx=150, pady=20)

window.mainloop()
