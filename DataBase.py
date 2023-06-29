import json
import re

class MysqlDatabases:
    def __init__(self):
        # 初始化数据库对象
        # 从文件中加载用户数据和学生数据
        self.users = json.loads(open('users.json', mode='r', encoding='utf-8').read())
        self.students = json.loads(open('students.json', mode='r', encoding='utf-8').read())

    def check_login(self, username, password):
        # 检查用户登录
        # 根据提供的用户名和密码进行验证
        # 如果用户名和密码匹配，则返回登录成功
        # 否则返回登录失败的相应消息
        for user in self.users:
            if user['username'] == username:
                if password == user['password']:
                    return True, '登陆成功'
                else:
                    return False, '登陆失败，密码错误'
        return False, '登陆失败，用户名错误'

    def all_student(self):
        # 获取所有学生信息
        # 返回存储的学生数据
        return self.students

    def is_valid_email(self, email):
        # 验证邮箱格式是否正确
        # 使用正则表达式检查提供的邮箱是否符合指定的格式要求
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            # print('='*10, "ok", '='*10)
            return True
        else:
            # print('='*10, "err", '='*10)
            return False

    def insert(self, student:dict):
        # 插入学生信息
        # 首先验证学生的邮箱格式是否正确
        # 如果邮箱格式正确，将学生信息添加到学生数据中，并将学生数据写入到文件中，然后返回插入成功的消息
        # 如果邮箱格式不正确，返回插入失败的消息
        if not self.is_valid_email(student['email']):
            return False, '邮箱格式不正确'
        else:
            self.students.append(student)
            with open('students.json', mode='w', encoding='utf-8') as f:
                json.dump(self.students, f, ensure_ascii=False)
            return True, '插入成功'

    def delete_by_name(self, name):
        # 根据姓名删除学生信息
        # 遍历学生数据，找到姓名匹配的学生并删除
        # 如果成功删除，将更新后的学生数据写入文件，并返回删除成功的消息
        # 如果找不到匹配的学生，返回学生不存在的消息
        for stu in self.students:
            print(stu)
            if stu['name'] == name:
                self.students.remove(stu)
                with open('students.json', mode='w', encoding='utf-8') as f:
                    json.dump(self.students, f, ensure_ascii=False)
                return True, f'{name} 删除成功'
        return False, f'{name} 不存在'

    def search_by_name(self, targetname):
        # 根据姓名搜索学生信息
        # 遍历学生数据，找到姓名匹配的学生并返回学生信息
        # 如果找到匹配的学生，返回成功和学生信息
        # 如果找不到匹配的学生，返回学生不存在的消息
        for stu in self.students:
            print(stu)
            if stu['name'] == targetname:
                return True, stu
        return False, f'{targetname} 不存在'

    def search_by_id(self, targetid):
        # 根据学号搜索学生信息
        # 遍历学生数据，找到学号匹配的学生并返回学生信息
        # 如果找到匹配的学生，返回成功和学生信息
        # 如果找不到匹配的学生，返回学生不存在的消息
        for stu in self.students:
            print(stu)
            if stu['id'] == targetid:
                return True, stu
        return False, f'学号为 {targetid} 的学生不存在'

    def update(self, targetstu:dict):
        # 更新学生信息
        # 首先验证学生的邮箱格式是否正确
        # 如果邮箱格式正确，遍历学生数据，找到姓名匹配的学生并更新信息
        # 如果成功更新，将更新后的学生数据写入文件，并返回更新成功的消息
        # 如果找不到匹配的学生，返回学生不存在的消息
        # 如果邮箱格式不正确，返回插入失败的消息
        if not self.is_valid_email(targetstu['email']):
            return False, '邮箱格式不正确'
        else:
            for stu in self.students:
                print(stu)
                if stu['name'] == targetstu['name']:
                    stu.update(targetstu)
                    with open('students.json', mode='w', encoding='utf-8') as f:
                        json.dump(self.students, f, ensure_ascii=False)
                    return True, f'{targetstu["name"]} 学生信息修改成功'
            return False, f'{targetstu["name"]} 不存在'

db = MysqlDatabases()
# 可以通过该实例调用数据库操作的方法

