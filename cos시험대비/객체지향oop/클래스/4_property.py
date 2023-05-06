# 속성

class C(object):
    def __init__(self,v):
        self.__val = v
    def show(self):
        print(self.__val)

c1 = C(10)
# print(c1.val)
c1.show() #좀더 편하게 하는 방법