import os
from tkinter import *

root = Tk()

root.title("제목 없음 - 메모장")  # 제목
root.geometry("640x480+400+300")  # 크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(file, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 새로운 내용 본문에 입력


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

#스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#빈껍데기
menu.add_cascade(label="편집", menu=menu_file)
menu.add_cascade(label="서식", menu=menu_file)
menu.add_cascade(label="보기", menu=menu_file)
menu.add_cascade(label="도움말", menu=menu_file)

#본문
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side = "left",fill="both", expand = True)


scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
