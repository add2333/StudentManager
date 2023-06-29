# 导入tkinter
import tkinter as tk
from tkinter import messagebox

# 导入数据模型里的db对象
from DataBase import db

# 导入主界面
from MainPage import MainPage


class LoginPage:

    def __init__(self, master):
        self.root = master
        self.root.geometry('600x360')
        self.root.title('Login Page')

        self.userName = tk.StringVar()
        self.userPassword = tk.StringVar()

        self.page = tk.Frame(root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='用户名：').grid(row=1, column=1)
        tk.Entry(self.page, textvariable=self.userName).grid(row=1, column=2)
        tk.Label(self.page, text='密码').grid(row=2, column=1, pady=50)
        tk.Entry(self.page, textvariable=self.userPassword).grid(row=2, column=2)

        tk.Button(self.page, text='登陆', command=self.login).grid(row=3, column=1)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2)

    def login(self):
        name = self.userName.get()
        pwd = self.userPassword.get()
        islogin, errmessage = db.check_login(name, pwd)
        if islogin:
            # 销毁登陆界面
            self.page.destroy()
            MainPage(self.root)
        else:
            messagebox.showwarning(title='Warning', message=errmessage)


if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)
    root.mainloop()
