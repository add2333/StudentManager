import tkinter as tk
from tkinter import ttk, messagebox

from DataBase import db


class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='By:add').pack()
        tk.Label(self, text='1395918522@qq.com').pack()
        tk.Label(self, text='https://github.com/add2333/StudentManager').pack()


class ChangeFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()
        self.id = tk.StringVar()
        self.GPA = tk.StringVar()
        self.classes = tk.StringVar()
        self.status = tk.StringVar()
        self.build_page()

    def build_page(self):
        tk.Label(self).grid(row=0, pady=20)

        tk.Label(self, text='姓  名:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='学  号:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=2, column=2, pady=10)

        tk.Label(self, text='学分绩:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.GPA).grid(row=3, column=2, pady=10)
        tk.Label(self, text='班  级:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.classes).grid(row=4, column=2, pady=10)

        tk.Button(self, text="查询", command=self.search_info).grid(row=5, column=1, pady=10)
        tk.Button(self, text="修改", command=self.change_info).grid(row=5, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10)

    def search_info(self):
        isexist, info = db.search_by_name(self.name.get())
        if isexist:
            self.name.set(info['name'])
            self.id.set(info['id'])
            self.GPA.set(info['GPA'])
            self.classes.set(info['class'])
            self.status.set('数据查询成功')
        else:
            self.status.set(info)

        pass

    def change_info(self):
        stu = {"name": self.name.get(), "id": self.id.get(), "GPA": self.GPA.get(), "class": self.classes.get()}
        self.name.set('')
        self.id.set('')
        self.GPA.set('')
        self.classes.set('')
        print(stu)
        db.update(stu)
        self.status.set('修改{%s}同学的信息成功！' %(stu["name"]))
        pass


class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()
        self.id = tk.StringVar()
        self.GPA = tk.StringVar()
        self.classes = tk.StringVar()
        self.status = tk.StringVar()
        self.build_page()

    def build_page(self):
        tk.Label(self).grid(row=0, pady=20)

        tk.Label(self, text='姓  名:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='学  号:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=2, column=2, pady=10)
        tk.Label(self, text='学分绩:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.GPA).grid(row=3, column=2, pady=10)
        tk.Label(self, text='班  级:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.classes).grid(row=4, column=2, pady=10)

        tk.Button(self, text="加入", command=self.record_info).grid(row=5, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=2, pady=10)

    def record_info(self):
        stu = {"name": self.name.get(), "id": self.id.get(), "GPA": self.GPA.get(), "class": self.classes.get()}
        self.name.set('')
        self.id.set('')
        self.GPA.set('')
        self.classes.set('')
        print(stu)
        db.insert(stu)
        self.status.set('成功插入！')


class SearchFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.table_view = tk.Frame()
        self.table_view.pack()

        self.build_page()

    def build_page(self):
        columns = ("name", "id", "GPA", "class")
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('name', width=200, anchor='center')
        self.tree_view.column('id', width=200, anchor='center')
        self.tree_view.column('GPA', width=200, anchor='center')
        self.tree_view.column('class', width=200, anchor='center')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('id', text='学号')
        self.tree_view.heading('GPA', text='学分绩')
        self.tree_view.heading('class', text='班级')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.display_data_frame()

        tk.Button(self, text='刷新', command=self.display_data_frame).pack()

    def display_data_frame(self):
        # 删除旧的信息
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        students = db.all_student()
        for index, stu in enumerate(students):
            print(stu)
            self.tree_view.insert('', index, values=(stu['name'], stu['id'], stu['GPA'], stu['class']))


class SearchByIdFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='ids').pack()


class SearchByNameFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text='idn').pack()


class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.username = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='根据名称删除数据').pack()
        tk.Entry(self, textvariable=self.username).pack()
        tk.Button(self, text='删除', command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        username = self.username.get()
        isdelete, message = db.delete_by_name(username)
        if isdelete:
            self.status.set(message)
        else:
            messagebox.showwarning(title='Warning', message=message)
        pass
