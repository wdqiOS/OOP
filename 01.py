'''
    定义一个学生类，用来形容学生
'''

# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
lizhe = Student()

# 定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的变量（属性）赋值
    name = None
    age = 18
    course = "Python"



    # 需要注意
    # 1、def doHomework的缩进层级
    # 2、系统默认有一个self参数
    def doHomework(self):
        print(self.name,"在做作业")

        # 推荐在函数末尾使用return 语句
        return  None

# 实例化一个叫哲哲的学生，是一个具体的人
zhezhe = PythonStudent()
zhezhe.name = "李哲"
zhezhe.age = 16
print(zhezhe.name)
print(zhezhe.age)
# 注意成员函数的调用没有传递进入参数

zhezhe.doHomework()
print(zhezhe.__dict__)
print(zhezhe.__dict__)
print(PythonStudent.__dict__)


wdq = PythonStudent()
print(wdq)