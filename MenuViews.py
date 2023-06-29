import tkinter as tk
from tkinter import ttk, messagebox
from DataBase import db


class AboutFrame(tk.Frame):
    def __init__(self, root):
        # 初始化关于界面
        super().__init__(root)
        # 关于信息
        tk.Label(self, text='By:add(By:ymr)').pack()
        tk.Label(self, text='1395918522@qq.com').pack()
        tk.Label(self, text='https://github.com/add2333/StudentManager').pack()


class ChangeFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # 创建用于存储用户输入的变量
        self.name = tk.StringVar()
        self.id = tk.StringVar()
        self.GPA = tk.StringVar()
        self.classes = tk.StringVar()
        self.status = tk.StringVar()
        self.sex = tk.StringVar()
        self.email = tk.StringVar()

        # 构建页面
        self.build_page()

    def build_page(self):
        # 构建页面，创建并排列标签、输入字段和按钮

        # 创建一个空的标签作为占位符
        tk.Label(self).grid(row=0, pady=20)

        # 创建标签和输入框用于输入学生信息
        tk.Label(self, text="仅支持通过姓名修改").grid(row=0, column=2, pady=10)
        tk.Label(self, text='姓  名:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='学  号:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=2, column=2, pady=10)
        tk.Label(self, text='学分绩:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.GPA).grid(row=3, column=2, pady=10)
        tk.Label(self, text='性  别:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=4, column=2, pady=10)
        tk.Label(self, text='邮  箱:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.email).grid(row=5, column=2, pady=10)
        tk.Label(self, text='班  级:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.classes).grid(row=6, column=2, pady=10)

        # 创建按钮，用于触发查询信息和修改信息的方法
        tk.Button(self, text="查询", command=self.search_info).grid(row=7, column=1, pady=10)
        tk.Button(self, text="修改", command=self.change_info).grid(row=7, column=2, pady=10)

        # 创建标签，用于显示查询和修改操作的状态信息
        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10)

    def search_info(self):
        # 查询信息的方法

        # 调用数据库的方法，通过姓名查询学生信息
        isexist, info = db.search_by_name(self.name.get())

        if isexist:
            # 如果查询结果存在，则将查询到的学生信息显示在对应的输入框中
            self.name.set(info['name'])
            self.id.set(info['id'])
            self.GPA.set(info['GPA'])
            self.classes.set(info['class'])
            self.email.set(info['email'])
            self.sex.set(info['sex'])
            self.status.set('数据查询成功')
        else:
            # 如果查询结果不存在，则将状态信息设置为查询失败的原因
            self.status.set(info)

        pass

    def change_info(self):
        # 修改信息的方法

        # 创建一个字典，存储要修改的学生信息
        stu = {"name": self.name.get(), "id": self.id.get(), "GPA": self.GPA.get(),
               "class": self.classes.get(), "email": self.email.get(), "sex": self.sex.get()}

        # 清空输入框中的内容
        self.name.set('')
        self.id.set('')
        self.GPA.set('')
        self.classes.set('')
        self.sex.set('')
        self.email.set('')

        # 调用数据库的方法，更新学生信息
        isupdated, message = db.update(stu)

        if isupdated:
            # 设置状态信息为成功修改学生信息的消息
            self.status.set('修改{%s}同学的信息成功！' % (stu["name"]))
        else:
            # 如果更新失败，则弹出警告框显示更新失败的原因，并设置状态信息为更新失败的消息
            messagebox.showwarning(title='更新失败', message=message)
            self.status.set(message)

        pass



class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()
        self.id = tk.StringVar()
        self.GPA = tk.StringVar()
        self.classes = tk.StringVar()
        self.status = tk.StringVar()
        self.sex = tk.StringVar()
        self.email = tk.StringVar()
        self.build_page()

    def build_page(self):
        # 构建页面，创建并排列标签、输入字段和按钮
        tk.Label(self).grid(row=0, pady=20)
        tk.Label(self, text='姓  名:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='学  号:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=2, column=2, pady=10)
        tk.Label(self, text='学分绩:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.GPA).grid(row=3, column=2, pady=10)
        tk.Label(self, text='性  别:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=4, column=2, pady=10)
        tk.Label(self, text='邮  箱:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.email).grid(row=5, column=2, pady=10)
        tk.Label(self, text='班  级:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.classes).grid(row=6, column=2, pady=10)

        tk.Button(self, text="加入", command=self.record_info).grid(row=7, column=2, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10)

    def record_info(self):
        # 记录信息
        stu = {"name": self.name.get(), "id": self.id.get(), "GPA": self.GPA.get(), "class": self.classes.get(),
               "email": self.email.get(), "sex": self.sex.get()}
        self.name.set('')
        self.id.set('')
        self.GPA.set('')
        self.classes.set('')
        self.sex.set('')
        self.email.set('')
        self.status.set('')
        # print(stu)
        isinserted, message = db.insert(stu)
        if isinserted:
            self.status.set('成功插入！')
        else:
            messagebox.showwarning(title='插入失败', message=message)
            self.status.set(message)


class SearchFrame(tk.Frame):
    def __init__(self, root):
        # 初始化界面
        super().__init__(root)
        self.table_view = tk.Frame()
        self.table_view.pack()

        self.build_page()

    def build_page(self):
        # 构建页面，创建并排列表格和刷新按钮

        # 定义表格的列名
        columns = ("name", "id", "GPA", "class", "sex", "email")

        # 创建一个Treeview控件用于显示表格
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)

        # 设置每列的宽度和对齐方式
        self.tree_view.column('name', width=100, anchor='center')
        self.tree_view.column('id', width=200, anchor='center')
        self.tree_view.column('GPA', width=100, anchor='center')
        self.tree_view.column('class', width=200, anchor='center')
        self.tree_view.column('sex', width=100, anchor='center')
        self.tree_view.column('email', width=300, anchor='center')

        # 设置每列的标题
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('id', text='学号')
        self.tree_view.heading('GPA', text='学分绩')
        self.tree_view.heading('class', text='班级')
        self.tree_view.heading('sex', text='性别')
        self.tree_view.heading('email', text='邮箱')

        # 设置表格行的高度
        style = ttk.Style()
        style.configure("Treeview", rowheight=50)
        self.tree_view["style"] = "Treeview"

        # 将表格填充到父容器中
        self.tree_view.pack(fill=tk.BOTH, expand=True)

        # 显示数据库中的学生信息
        self.display_data_frame()

        # 创建刷新按钮，并绑定刷新数据的方法
        tk.Button(self, text='刷新', command=self.display_data_frame).pack()

    def display_data_frame(self):
        # 清空表格中的旧数据
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        # 从数据库中获取所有学生的信息
        students = db.all_student()

        # 将学生信息逐行插入表格中
        for index, stu in enumerate(students):
            self.tree_view.insert('', index, values=(stu['name'], stu['id'], stu['GPA'],
                                                     stu['class'], stu['sex'], stu['email']))


class SearchByIdFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # 创建用于存储用户输入的变量
        self.name = tk.StringVar()
        self.id = tk.StringVar()
        self.GPA = tk.StringVar()
        self.classes = tk.StringVar()
        self.status = tk.StringVar()
        self.sex = tk.StringVar()
        self.email = tk.StringVar()

        self.build_page()

    def build_page(self):
        # 构建页面，包括标签、输入框和按钮

        # 创建一个空的标签作为占位符
        tk.Label(self).grid(row=0, pady=10)

        # 创建标签和输入框用于输入学生信息
        tk.Label(self, text='姓  名:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='学  号:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=2, column=2, pady=10)
        tk.Label(self, text='学分绩:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.GPA).grid(row=3, column=2, pady=10)
        tk.Label(self, text='性  别:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=4, column=2, pady=10)
        tk.Label(self, text='邮  箱:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.email).grid(row=5, column=2, pady=10)
        tk.Label(self, text='班  级:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.classes).grid(row=6, column=2, pady=10)

        # 创建按钮，用于触发通过学号查询的方法
        tk.Button(self, text="通过学号查询", command=self.search_info_by_id).grid(row=7, column=2, pady=10)

        # 创建标签，用于显示查询结果的状态信息
        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10)

    def search_info_by_id(self):
        # 通过学号查询学生信息的方法

        # 调用数据库的方法，通过学号查询学生信息
        isexist, info = db.search_by_id(self.id.get())

        if isexist:
            # 如果查询结果存在，则将查询到的学生信息显示在对应的输入框中
            self.name.set(info['name'])
            self.id.set(info['id'])
            self.GPA.set(info['GPA'])
            self.classes.set(info['class'])
            self.sex.set(info['sex'])
            self.email.set(info['email'])
            self.status.set('数据查询成功')
        else:
            # 如果查询结果不存在，则显示查询失败的原因
            self.status.set(info)

        pass


class SearchByNameFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # 创建用于存储用户输入的变量
        self.name = tk.StringVar()
        self.id = tk.StringVar()
        self.GPA = tk.StringVar()
        self.classes = tk.StringVar()
        self.status = tk.StringVar()
        self.sex = tk.StringVar()
        self.email = tk.StringVar()

        self.build_page()

    def build_page(self):
        # 构建页面，包括标签、输入框和按钮

        # 创建一个空的标签作为占位符
        tk.Label(self).grid(row=0, pady=10)

        # 创建标签和输入框用于输入学生信息
        tk.Label(self, text='姓  名:').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='学  号:').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.id).grid(row=2, column=2, pady=10)
        tk.Label(self, text='学分绩:').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.GPA).grid(row=3, column=2, pady=10)
        tk.Label(self, text='性  别:').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=4, column=2, pady=10)
        tk.Label(self, text='邮  箱:').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.email).grid(row=5, column=2, pady=10)
        tk.Label(self, text='班  级:').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.classes).grid(row=6, column=2, pady=10)

        # 创建按钮，用于触发通过姓名查询的方法
        tk.Button(self, text="通过姓名查询", command=self.search_info_by_name).grid(row=7, column=2, pady=10)

        # 创建标签，用于显示查询结果的状态信息
        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10)

    def search_info_by_name(self):
        # 通过姓名查询学生信息的方法

        # 调用数据库的方法，通过姓名查询学生信息
        isexist, info = db.search_by_name(self.name.get())

        if isexist:
            # 如果查询结果存在，则将查询到的学生信息显示在对应的输入框中
            self.name.set(info['name'])
            self.id.set(info['id'])
            self.GPA.set(info['GPA'])
            self.classes.set(info['class'])
            self.sex.set(info['sex'])
            self.email.set(info['email'])
            self.status.set('数据查询成功')
        else:
            # 如果查询结果不存在，则将状态信息设置为查询失败的原因
            self.status.set(info)

        pass


class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # 创建用于存储用户输入的变量
        self.username = tk.StringVar()
        self.status = tk.StringVar()

        # 创建标签、输入框和按钮
        tk.Label(self, text='根据名称删除数据').pack()
        tk.Entry(self, textvariable=self.username).pack()
        tk.Button(self, text='删除', command=self.delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def delete(self):
        # 删除数据的方法

        # 获取用户输入的用户名
        username = self.username.get()

        # 调用数据库的方法，根据名称删除数据
        isdelete, message = db.delete_by_name(username)

        if isdelete:
            # 如果删除成功，则设置状态信息为删除成功的消息
            self.status.set(message)
        else:
            # 如果删除失败，则弹出警告框显示删除失败的原因
            messagebox.showwarning(title='删除失败', message=message)

        pass
