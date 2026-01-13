import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

values = [str(i)+"일" for i in range(1,32)] # 1 ~ 31
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height = 5, values = values, state="readonly") # state => 상태 정보 설정
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()