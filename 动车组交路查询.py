import requests
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *


def find_train(number):
    headers = {
        "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
    response = requests.get(f"https://api.rail.re/train/{number}", headers=headers)
    response.encoding = "utf-8"
    try:
        train_list = eval(response.text)
    except SyntaxError:
        return []
    return train_list


def find_emu(number):
    headers = {
        "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
    response = requests.get(f"https://api.rail.re/emu/{number}", headers=headers)
    response.encoding = "utf-8"
    try:
        train_list = eval(response.text)
    except SyntaxError:
        return []
    return train_list


def no():
    train_ = find_train(train_input.get())
    n = ""
    for i in train_:
        n += f'{i["date"]} {i["train_no"]}由{i["emu_no"]}担当\n'

    showinfo(f"{train_input.get()}的信息", str(n))


def tr():
    train_ = find_emu(emu_input.get())
    n = ""
    for i in train_:
        n += f'{i["date"]} {i["train_no"]}由{i["emu_no"]}担当\n'

    showinfo(f"{train_input.get()}的信息", str(n))


def love_train():
    s = askstring("询问", "请输入想收藏的车次")
    w = open("star.tzt", "a")
    w.write(f"{s}\n")


def love_emu_f():
    s = askstring("询问", "请输入想收藏的列车")
    w = open("star2.tzt", "a")
    w.write(f"{s}\n")



love_text = open("star.tzt").read()
love_list_no = love_text.split("\n")


love_emu = open("star2.tzt").read()
love_list_emu = love_emu.split("\n")


tk = Tk()
tk.title("动车组交路查询")
tk.resizable(False, False)

train = Label(tk, text="查询车次")
train.grid(column=0, row=0)

train_input = Entry(tk)
train_input.grid(column=1, row=0)

emu = Label(tk, text="查询车组号")
emu.grid(column=0, row=1)

emu_input = Entry(tk)
emu_input.grid(column=1, row=1)

train_button = Button(tk, text="查询车次", command=no)
train_button.grid(column=2, row=0)

emu_button = Button(tk, text="查询列车", command=tr)
emu_button.grid(column=2, row=1)

k_l = Label(tk, text="")
k_l.grid(row=3, column=0)

love_l = Label(tk, text="收藏的列车")
love_l.grid(row=4, column=0)


r = 5

for i in love_list_emu:
    try:
        train_love = Label(tk, text=i)
        train_love.grid(row=r, column=0)
        emu = find_emu(i)[0]
        train_go = Label(tk, text=f'{emu["date"]}担当{emu["train_no"]}')
        train_go.grid(row=r, column=1)
        r += 1
    except:
        continue

no = Label(tk, text="收藏的车次")
no.grid(row=r, column=0)

r += 1

for i in love_list_no:
    try:
        train_love = Label(tk, text=i)
        train_love.grid(row=r, column=0)
        emu = find_train(i)[0]
        train_go = Label(tk, text=f'{emu["date"]}由{emu["emu_no"]}担当')
        train_go.grid(row=r, column=1)
        r += 1
    except:
        continue

r += 1

button_a = Button(tk, text="添加收藏车次", command=love_train)
button_a.grid(row=r, column=0)

r += 1

button_a = Button(tk, text="添加收藏车号", command=love_emu_f)
button_a.grid(row=r, column=0)

tk.mainloop()
