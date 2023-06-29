import tkinter as tk
from MenuViews import InsertFrame, SearchFrame, SearchByIdFrame, SearchByNameFrame, DeleteFrame, ChangeFrame, AboutFrame


class MainPage:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('学生信息管理系统 by add')
        self.root.geometry("1200x800")
        self.build_page()

    def build_page(self):
        self.insert_frame = InsertFrame(self.root)
        self.search_frame = SearchFrame(self.root)
        self.search_by_id_frame = SearchByIdFrame(self.root)
        self.search_by_name_frame = SearchByNameFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.change_frame = ChangeFrame(self.root)
        self.about_frame = AboutFrame(self.root)

        menubar = tk.Menu(self.root)
        menubar.add_command(label='增加', command=self.display_insert)
        menubar.add_command(label='查询所有', command=self.display_search)
        menubar.add_command(label='学号查询', command=self.display_search_by_id)
        menubar.add_command(label='姓名查询', command=self.display_search_by_name)
        menubar.add_command(label='删除', command=self.display_delete)
        menubar.add_command(label='修改', command=self.display_change)
        menubar.add_command(label='关于', command=self.display_about)
        self.root['menu'] = menubar

    def display_insert(self):
        self.insert_frame.pack()
        self.search_frame.pack_forget()
        self.search_by_id_frame.pack_forget()
        self.search_by_name_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()

    def display_search(self):
        self.search_frame.pack()
        self.insert_frame.pack_forget()
        self.search_by_id_frame.pack_forget()
        self.search_by_name_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()


    def display_search_by_id(self):
        self.search_by_id_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.search_by_name_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()

    def display_search_by_name(self):
        self.search_by_name_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.search_by_id_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()

    def display_delete(self):
        self.delete_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.search_by_id_frame.pack_forget()
        self.search_by_name_frame.pack_forget()
        self.change_frame.pack_forget()
        self.about_frame.pack_forget()

    def display_change(self):
        self.change_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.search_by_id_frame.pack_forget()
        self.search_by_name_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.about_frame.pack_forget()

    def display_about(self):
        self.about_frame.pack()
        self.insert_frame.pack_forget()
        self.search_frame.pack_forget()
        self.search_by_id_frame.pack_forget()
        self.search_by_name_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.change_frame.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
