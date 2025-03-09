# This is classvariable and classmethod and staticmethod
# 类变量
# 类方法
# 静态方法

class Student(object):

    student_num = 0   # 类变量定义在类里面, 需要通过类名访问
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Student.student_num += 1   # 这里的类属性 student_num, 需要通过类名 Student 来访问, 即 Student.student_num


    # 类方法
    @classmethod   # 类方法需要装饰器 @classmethod 进行装饰; 使用类方法代替构造方法是一种常见的方法
    def add_students(cls, num):    # 参数 cls 代表类本身, num 则为方法的参数
        cls.student_num += num

    @classmethod
    def from_string(cls, info):
        name, sex = info.split(' ')
        return cls(name, sex)

    
    # 静态方法需要用 staticmethod 装饰器进行装饰, 静态方法与类方法不同, 静态方法不需要传入 cls或者self
    # 静态方法不能访问类和实例对象里面的私有属性 
    # 静态方法的适用场景是 虽然静态方法不需要类里面的内容, 但是从结构上来说, 静态方法需要在类的里面, 同样也适用将一系列功能相关的函数封装在一起
    @staticmethod 
    def name_len(name):
        return len(name)


s1 = Student('Qiqi', 'woman')
s2 = Student.from_string('Qiqi woman')
Student.add_students(5)


print(f'Student.student_num:{Student.student_num}')
print(f'name:{s2.name}, len:{s2.name_len(s2.name)}')