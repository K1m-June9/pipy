from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

#라디오버튼 -> 여러 개 중 택1

label1 = Label(root, text="메뉴를 선택").pack()

burger_var = IntVar() #StringVar()을 사용하여 value="~~"로 사용 가능
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() #기본값 선택
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

def btncmd():
    print(burger_var.get()) # 선택된 라디오 항목의 값(value)을 출력
btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()