import tkinter as tko
from tkinter.ttk import *
import requests
import tkinter.ttk as ttk


def star(t):
    w = open("star", "a")
    w.write(t + "\n")
    v = find(t)
    l = []
    l.append([v[0]["date"], v[0]["emu_no"], v[0]["train_no"]])
    for data in l:
        # insert()方法插入数据
        table.insert('', 'end', value=data)


def find_b(t):
    a = find(t)
    l = []
    for i in a:
        l.append([i["date"], i["emu_no"], i["train_no"]])

    tk = tko.Tk()
    tk.title("查询结果")
    tableColumns = ['日期', '车号', '车次']
    tableValues = l
    # 设置滚动条
    xscroll = Scrollbar(tk, orient=tko.HORIZONTAL)
    yscroll = Scrollbar(tk, orient=tko.VERTICAL)
    xscroll.pack(side=tko.BOTTOM, fill=tko.X)
    yscroll.pack(side=tko.RIGHT, fill=tko.Y)
    table = ttk.Treeview(
        master=tk,  # 父容器
        columns=tableColumns,  # 列标识符列表
        height=30,  # 表格显示的行数
        show='tree headings',  # 隐藏首列
        style='Treeview',  # 样式
        xscrollcommand=xscroll.set,  # x轴滚动条
        yscrollcommand=yscroll.set  # y轴滚动条
    )
    xscroll.config(command=table.xview)
    yscroll.config(command=table.yview)
    table.pack()  # TreeView加入frame
    # 定义表头
    for i in range(len(tableColumns)):
        table.heading(column=tableColumns[i], text=tableColumns[i], anchor=tko.CENTER)  # 定义表头
        table.column(tableColumns[i], minwidth=100, anchor=tko.CENTER, stretch=True)  # 定义列
    # style = ttk.Style(tk)
    # style.configure('Treeview')
    for data in tableValues:
        # insert()方法插入数据
        table.insert('', 'end', value=data)
    tk.mainloop()


def find(o):
    try:
        if (o[0] == "c" or o[0] == "C") and (o[1] == "r" or o[1] == "R"):
            l = "emu"
        elif o[1].isdigit():
            l = "train"
        else:
            return []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}
        response = requests.get(f"https://api.rail.re/{l}/{o}", headers=headers)
        response.encoding = "utf-8"
        r = eval(response.text)
        return r
    except:
        return []


tk = tko.Tk()
tk.title("动车组交路查询V3.0.0")
e = Entry(tk)
e.pack()
b = Button(tk, text="查询", command=lambda: find_b(e.get()))
b.pack()
b = Button(tk, text="收藏", command=lambda: star(e.get()))
b.pack()

l = []
for i in open("star").read().split("\n"):
    try:
        l.append([find(i)[0]["date"], find(i)[0]["emu_no"], find(i)[0]["train_no"]])
    except:
        continue
tableColumns = ['日期', '车号', '车次']
tableValues = l
# 设置滚动条
xscroll = Scrollbar(tk, orient=tko.HORIZONTAL)
yscroll = Scrollbar(tk, orient=tko.VERTICAL)
xscroll.pack(side=tko.BOTTOM, fill=tko.X)
yscroll.pack(side=tko.RIGHT, fill=tko.Y)
table = ttk.Treeview(
    master=tk,  # 父容器
    columns=tableColumns,  # 列标识符列表
    height=30,  # 表格显示的行数
    show='tree headings',  # 隐藏首列
    style='Treeview',  # 样式
    xscrollcommand=xscroll.set,  # x轴滚动条
    yscrollcommand=yscroll.set  # y轴滚动条
)
xscroll.config(command=table.xview)
yscroll.config(command=table.yview)
table.pack()  # TreeView加入frame
# 定义表头
for i in range(len(tableColumns)):
    table.heading(column=tableColumns[i], text=tableColumns[i], anchor=tko.CENTER)  # 定义表头
    table.column(tableColumns[i], minwidth=100, anchor=tko.CENTER, stretch=True)  # 定义列
# style = ttk.Style(tk)
# style.configure('Treeview')
for data in tableValues:
    # insert()方法插入数据
    table.insert('', 'end', value=data)
tk.mainloop()
