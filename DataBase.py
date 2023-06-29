import json
import re

class MysqlDatabases:
    def __init__(self):
        self.users = json.loads(open('users.json', mode='r', encoding='utf-8').read())
        self.students = json.loads(open('students.json', mode='r', encoding='utf-8').read())

    def check_login(self, username, password):
        for user in self.users:
            if user['username'] == username:
                if password == user['password']:
                    return True, '登陆成功'
                else:
                    return False, '登陆失败，密码错误'
        return False, '登陆失败，用户名错误'

    def all_student(self):
        return self.students

    def is_valid_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, self.students['email']) is not None

    def insert(self, student):
        if not self.is_valid_email:
            return False, '邮箱格式不正确'
        else:
            self.students.append(student)
            with open('students.json', mode='w', encoding='utf-8') as f:
                json.dump(self.students, f, ensure_ascii=False)
            return True, '插入成功'

    def delete_by_name(self, name):
        for stu in self.students:
            print(stu)
            if stu['name'] == name:
                self.students.remove(stu)
                with open('students.json', mode='w', encoding='utf-8') as f:
                    json.dump(self.students, f, ensure_ascii=False)
                return True, f'{name} 删除成功'
        return False, f'{name} 不存在'

    def search_by_name(self, targetname):
        for stu in self.students:
            print(stu)
            if stu['name'] == targetname:
                return True, stu
        return False, f'{targetname} 不存在'

    def search_by_id(self, targetid):
        for stu in self.students:
            print(stu)
            if stu['id'] == targetid:
                return True, stu
        return False, f'学号为 {targetid} 的学生不存在'

    def update(self, targetstu):
        for stu in self.students:
            print(stu)
            if stu['name'] == targetstu['name']:
                stu.update(targetstu)
                with open('students.json', mode='w', encoding='utf-8') as f:
                    json.dump(self.students, f, ensure_ascii=False)
                return True, f'{targetstu["name"]} 学生信息修改成功'
        return False, f'{targetstu["name"]} 不存在'


db = MysqlDatabases()
if __name__ == '__main__':
    # print(db.check_login('teacher', '111111'))
    # print(db.all_student())
    print(db.search_by_name('2'))
