from tkinter import *

root = Tk() # main window

def btmcmd():
    print("버튼 클릭")

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

btn1 = Button(root, text="버튼1", command=btmcmd)
btn1.pack() # <-이거 해야 버튼이 창에 나옴



btn2 = Button(root, padx=5, pady=10, text="버튼2") #텍스트 내용에 따라 유동적 변경(pad = 여백)
btn2.pack()

btn3 = Button(root, width=10, height=3, text="버튼4") #텍스트 내용에 관계 없이 크기 유지
btn3.pack()

root.mainloop()