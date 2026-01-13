from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자 입력")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력:")

root.mainloop()