import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)
#indeterminate -> 정해지지 않은 값
#determinate -> 끝에 도달하면 끝남
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10ms마다 움직임
# progressbar.pack()



# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="Select", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar1 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar1.pack()

def btncmd2():
    for i in range(1,101): # 1~101
        time.sleep(0.01)

        p_var2.set(i) # progressbar 의 값 설정
        progressbar1.update() # gui update

btn = Button(root, text="Select", command=btncmd2)
btn.pack()

root.mainloop()