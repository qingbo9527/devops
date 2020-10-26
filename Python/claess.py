# class
'''面向对象编程'''
class Students:
    school = 'HomeTwon'
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('*' * 50)
    def choice_course(self):
        print('is choice course')
try:
    stu1 = Students()
except Exception as e:
    print(e)

stu1 = Students('Bob', 18, 'male')
print(stu1.__dict__)
'''
通过上述现象可以发现，调用类时发生两件事：
    创造一个空对象
    自动触发类中__init__功能的执行，将stu1以及调用类括号内的参数一同传入
'''
class Foo:
    pass
obj = Foo()
print(type(obj))
class Students:
    school = 'HomeTwon'
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('*' * 50)
    def choice_course(self,name):
        print(f'{name} choice course')
stu1 = Students('Mike',19,'male')
stu1.choice_course(1)
Students.choice_course(stu1, 1)
lis = [1, 2, 3]
print(type(lis))
lis.append(4)
print(lis)
list.append(lis, 5)
print(lis)
'''无对象'''
'''
import pymysql
def exc1(host,port,db,charset,sql):
    conn = pymysql.connect(host,port,db,charset)
    conn.execute(sql)
    return xxx
def exc2(proc_name):
    conn = pymysql.connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx
exc1('172.16.179.172',3306,'db1','utf-8','select * from t1')

def exc1(sql,host='172.16.179.172',port=3306,db='db1',charset='utf-8'):
    conn = pymysql.connect(host,port,db,charset)
    conn.execute(sql)
    return xxx
exc1('select * from t1')
'''
'''有对象'''
'''
import pymysql
class Foo:
    def __init__(self,host,port,db,charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset
    def exc1(self,sql):
        conn = pymysql.connect(self.host,self.port,self.db,self.charset)
        conn.execute(sql)
        return xxx
    def exc2(self,proc_name):
        conn = pymysql.connect(self.host,self.port,self.db,self.charset)
        conn.call_proc(sql)
        return xxx
obj1 = Foo('172.16.179.172',3306,'db1','utf-8')
obj1.exc1('select * from t1')
obj1.exc1('select * from t2')
obj2 = Foo('172.16.179.173',33.6,'db1','utf-8')
obj2.exc1('select * from t1')
'''
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
bart.score = 90
print(bart.score)
lisa.print_score()
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart', 59)
lisa = Student('Lisa', 87)
print(bart.name, bart.get_grade())
print(lisa.name, lisa.get_grade())
# 私有变量'__private'
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print(f'{0}:{1}',self.name,self.score)
    def get_name(self):
        return self.__name
bart = Student('Bob.Dilun',91)
print(bart.get_name())
bart.__name = 'New name'
print(bart.__name)
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender
# 测试
bob = Student('Bob','male')
if bob.get_gender() != 'male':
    print('测试失败')
else:
    bob.set_gender('female')
    if bob.get_gender() != 'female':
        print('测试失败')
    else:
        print('测试成功')
# 判断对象类型
# type()函数
# isinstance()函数
# 实例属性和类属性
class Student(object):
    name = 'Student'
# 创建实例s
s = Student()
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)
# 打印类的name属性
print(Student.name)
# 给实例绑定name属性
s.name = 'Michael'
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name)
# 但是类属性并未消失，用Student.name仍然可以访问
print(Student.name)
# 删除实例的name属性
del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name)
# 给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
        # self.count = self.count + 1，为何不能这么写？因为self.count为实例属性，每次都会初始化为0，类属性为所有实例属性共享，可以加
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')