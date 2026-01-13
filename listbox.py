from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

listbox = Listbox(root, selectmode="extended", height=0)#height=0이면 리스트 전체를 보여줌
listbox.insert(0,"apple")
listbox.insert(1,"starr")
listbox.insert(2,"banana")
listbox.insert(END,"watermelon")
listbox.insert(END,"grape")
listbox.pack()

def btncmd():
    #delete
    #listbox.delete(0) #맨 앞 항목을 삭제
    #개수 확인
    #print("list = ", listbox.size())
    #항목 확인(0~2)
    #print("1~3번 항목: ", listbox.get(0, 2))
    #선택된 항목 확인(위치로 반환)
    print("선택된 항목: ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()