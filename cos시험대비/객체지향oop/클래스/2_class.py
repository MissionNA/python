# class Cal(object):
#     def __init__(self,v1,v2):  #__init__:함수 초기화
#         print(v1,v2)

# c1 = Cal(10,10)
# # print(c1.add())
# # print(c1.subtact())
# c2 = Cal(30,20)
꽓꿠똷뀋 = 1
print(꽓꿠똷뀋)
# class 활용:Instance변수와 method
class Celkulator(object):
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        if self.v1 - self.v2 < 0:
            return self.v2 - self.v1
        else: return self.v1 - self.v2
c1 = Celkulator(800,20)
print(c1.add())
print(c1.subtract())

c1 = Celkulator(20,800)
print(c1.add())
print(c1.subtract())