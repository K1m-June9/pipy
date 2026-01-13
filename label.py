from tkinter import *

root = Tk()
root.title("!!")
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)


label1 = Label(root, text = "HelloWorld")
label1.pack()

def change():
    label1.config(text="WOW")

btn = Button(root, text="click",command=change)
btn.pack()

root.mainloop()