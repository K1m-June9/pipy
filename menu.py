from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

def create_new_file():
    print("새 파일 생성 ")

menu = Menu(root)

#File
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label="New File", command= create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File ... ")
menu_file.add_separator()
menu_file.add_command(label="Save All", state = "disable")
menu_file.add_separator()
menu_file.add_command(label = "Exit", command = root.quit)
menu.add_cascade(label="File", menu = menu_file)

#Edit
menu.add_cascade(label = "Edit")
#radiobutton, checkbox 메뉴에서 사용 가능
root.config(menu=menu)
root.mainloop()