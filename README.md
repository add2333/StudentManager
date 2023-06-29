## Python 实现的学生管理系统

### 依赖

- python 3.8
- 其他依赖包均为 python 3.8 自带（tkinter, re, json

### 主要使用的包
- tkinter--实现图形界面
- re--验证邮箱正则表达式
- json--读取 json 文件

### 运行

1. `clone` 项目
2. 控制台中输入`python LoginPage.py`运行

### 备注

- 用户名：111，密码：111
- 登陆用户名和密码可以通过修改`users.json`来更改
- 由于本 demo 在 Ubuntu 下编写， 所以在 windows 系统下的运行界面可能会出现过大或过小的情况
- students.json 示例
```json
[{"name": "张三", "id": "2022111111", "GPA": "4.1", 
  "class": "111", "email": "123456@gmail.com", "sex": "男"}]
```
- users.json 示例
```json
[{"username": "111", "password": "111"}, {"username": "add", "password": "123"}]
```