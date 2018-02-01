# 这里介绍的类的写法
# __dict__ 类的属性
# __doc__ 类的文档字符串
# __name__ 类的名称
# __module__
# __bases__
# 类的继承 写法为class SubClassName(ParentClass1[,ParentClass2,...])
# 也就数说在相应的类名称之后加一个()里面放入父类,不是单继承
# 继承这里面的话,子类不会调用父类的init方法 但是可以在子类的构造方法中调用父类构造方法直接调用父类名 ItWorker()


class Worker:
    ''''
        工人类
    '''
    classStr = '这个是变量名称'

    # def __init__(self, name, pay):
    #     self.name = name
    #     self.pay = pay

    # 打印相应的方法 这个是实例化方法
    def hello(self):
        '''
        输出的相应的方法
        '''
        print(self.name)
        # 这里注意啊 字符串和数字的类型不能拼接的
        print('工人的名字是' + self.name + '工人的薪资是' + str(self.pay))

    # 类方法 使用@classmethod进行标识
    # @classmethod


class ItWorker(Worker):

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        print('子类的相应方法')

    def ItHello(self):
        print('It民工的工资是' + self.name)

    def hello(self):
        print('重新实现了父类的方法')
