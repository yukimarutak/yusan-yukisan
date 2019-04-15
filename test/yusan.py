# -*- coding: utf8 -*-
import tkinter
import tkinter.messagebox


def DeleteEntryValue(event):
    entry_box.delete(0, tkinter.END)


def check(event):
    global val1
    global val2
    global val3

    text = ""

    if val1.get() is True:
        text += "項目1はチェックされています\n"
    else:
        text += "項目1はチェックされていません\n"

    if val2.get() is True:
        text += "項目2はチェックされています\n"
    else:
        text += "項目2はチェックされていません\n"

    if val3.get() is True:
        text += "項目3はチェックされています\n"
    else:
        text += "項目3はチェックされていません\n"

    tkinter.messagebox.showinfo('info', text)


root = tkinter.Tk()
root.title("タイトル")
root.geometry("400x300")

Static1 = tkinter.Label(text='test', background='#ffaacc')
Static1.pack()
Static1.place(x=100, y=200)

Static2 = tkinter.Label(text="test", background='#ffaacc')
Static2.pack()
Static2.place(x=0, y=0)

entry_box = tkinter.Entry(width=50)
entry_box.pack()
entry_box.place(x=0, y=20)

button = tkinter.Button(text='ボタン')
button.bind("<Button-1>", DeleteEntryValue)
button.pack()
button.place(x=0, y=50)

val1 = tkinter.BooleanVar()
val2 = tkinter.BooleanVar()
val3 = tkinter.BooleanVar()

val1.set(False)
val2.set(True)
val3.set(False)

check_box1 = tkinter.Checkbutton(text="項目1", variable=val1)
check_box1.pack()
check_box1.place(x=0, y=100)

check_box2 = tkinter.Checkbutton(text="項目2", variable=val2)
check_box2.pack()
check_box2.place(x=0, y=120)

check_box3 = tkinter.Checkbutton(text="項目3", variable=val3)
check_box3.pack()
check_box3.place(x=0, y=140)

check_button = tkinter.Button(root, text='チェックの取得', width=30)
check_button.bind("<Button-1>", check)
check_button.pack()

root.mainloop()






