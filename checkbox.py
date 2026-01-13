from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

chkvar = IntVar() #chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="숨쉬기", variable=chkvar)
#chkbox.select() #자동 선택 처리
#chkbox.deselect() # 선택 처리 해제
chkbox.pack()

def btncmd():
   print(chkvar.get()) #0-> check X, 1->check

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()