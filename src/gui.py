from ZWStringConverter import *
from tkinter import *
from os import system
from tkinter import messagebox


TK_SILENCE_DEPRECATION = 1

main_win = Tk()
main_win.title('ZWS Cryptor')

main_win.geometry('320x245+570+285')
main_win.resizable(width=False, height=False)

def about(): 
    messagebox.showinfo(title="ZWS Cryptor", message="""作者：@TLHorse
一个可以将普通文本加密为零宽字符（ZWS）达到文本隐藏的效果的应用程序
• www.52pojie.cn/home.php?mod=space&uid=1321804
• github.com/TLHorse""")  # add this line

result_var = StringVar()
input_var = StringVar()
infovar = StringVar()
zwsinst = ZWStringConverter("")

infovar.set("Ready!")

def crypt(mode):
    zwsinst.targetString = input_var.get().rstrip('\n')
    if mode == "de":
        result_var.set(zwsinst.unzerowidth())
    elif mode == "en":
        result_var.set(zwsinst.zerowidth())
    elif mode == "au":
        result_var.set(zwsinst.convert())
    else:
        exit(1)
    infovar.set("加/解密完成，可以复制")


def cp_res():
    global infovar
    instr = result_var.get()
    system(f"echo {instr} | pbcopy")
    infovar.set("复制成功")


input_box = Entry(main_win, relief=GROOVE, textvariable=input_var)
input_box.place(x=10, y=10, width=100, height=225)

out_box = Entry(main_win, relief=GROOVE,
                state=DISABLED, textvariable=result_var)
out_box.place(x=320-10-100, y=10, width=90, height=225)

enc_btn = Button(main_win, text='加密', command=lambda: crypt("en"))
enc_btn.place(x=(320-80)/2, y=20, width=80)
dec_btn = Button(main_win, text='解密', command=lambda: crypt("de"))
dec_btn.place(x=(320-80)/2, y=20+30, width=80)
auto_btn = Button(main_win, text='自动', command=lambda: crypt("au"))
auto_btn.place(x=(320-80)/2, y=20+30*2, width=80)
cp_btn = Button(main_win, text='复制结果', command=cp_res)
cp_btn.place(x=(320-80)/2, y=20+30*3, width=80)
about_btn = Button(main_win, text='关于', command=about)
about_btn.place(x=(320-80)/2, y=20+30*4, width=80)
quit_btn = Button(main_win, text='退出', command=lambda: exit(0))
quit_btn.place(x=(320-80)/2, y=20+30*5, width=80)

info_label = Label(main_win, fg='red', textvariable=infovar)
info_label.place(x=(320-80)/2, y=20+30*6, width=80, height=30)

main_win.mainloop()
