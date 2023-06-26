# 导入tkinter
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('600x360')
root.title('Login Page')

userName = tk.StringVar()
userPassword = tk.StringVar()

page = tk.Frame(root)
page.pack()

tk.Label(page).grid(row=0, column=0)

tk.Label(page, text='用户名：').grid(row=1, column=1)
tk.Entry(page, textvariable=userName).grid(row=1, column=2)
tk.Label(page, text='密码').grid(row=2, column=1, pady=50)
tk.Entry(page, textvariable=userPassword).grid(row=2, column=2)


def login():
    name = userName.get()
    pwd = userPassword.get()
    if name == 'teacher' and pwd == '111':
        print('登陆成功')
    else:
        messagebox.showwarning(title='登陆失败', message='账号或密码错误')


tk.Button(page, text='登陆', command=login).grid(row=3, column=1)
tk.Button(page, text='退出', command=page.quit).grid(row=3, column=2)

root.mainloop()
