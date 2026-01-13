import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

Label(root, text = "메뉴 선택").pack(side = "top")

Button(root, text = "주문하기").pack(side = "bottom")

frame_burger = Frame(root, relief = "solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text = "Hamburger").pack()
Button(frame_burger, text = "치즈버거").pack()
Button(frame_burger, text = "먼먼버거").pack()

frame_drink = LabelFrame(root, text = "음료")
frame_drink.pack(side = "right", fill="both", expand = True)
Button(frame_drink, text = "콜라").pack()
Button(frame_drink, text = "사이다").pack()

root.mainloop()