import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()

root.title("Gui Practice") # 제목
root.geometry("640x480+400+300") #크기(가로*세로 + x좌표 + y좌표)(좌표 = 창이 뜨는 위치)

def info():
    msgbox.showinfo("알림","정상완료")

def warn():
    msgbox.showwarning("경고","비정상")

def error():
    msgbox.showerror("에러","Error")

def okcancel():
    msgbox.askokcancel("확인/ 취소","ㄹㅇ 할건가")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소","Re?")

def yesno():
    msgbox.askyesno("예/아니오","y / n")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="할건지말건지머할건지")
    #Y: 저장 후 종료
    #N: 걍 종료
    #C: 취소
    #response = True, False, None -> Yes 1, No 0, 그 외

Button(root, command=info, text="INFO").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="error").pack()
Button(root, command=okcancel, text="cancel").pack()
Button(root, command=retrycancel, text="Retry").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()

root.mainloop()