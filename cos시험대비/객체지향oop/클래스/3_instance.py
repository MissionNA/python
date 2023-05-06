# # instance 변수 읽고 쓰기
# class C(object):
#     def __init__(self,v):
#         self.value = v
#     def show(self):
#         print(self.value)


# c1 = C(10)
# print(c1.value)
# c1.value = 20
# print(c1.value)
# c1.show()

# # instance 변수 읽고 쓰기 확장(set/get 메소드)
# class C(object):
#     def __init__(self,v):
#         self.val = v
#     def show(self):
#         print(self.val)
#     def getValue(self):
#         return self.val
#     def setValue(self,v):
#         self.val = v

# c1 = C(10)
# print(c1.getValue())
# c1.setValue(20)
# print(c1.getValue())

# # instance 변수 읽고 쓰기 확장(set/get 메소드를 사용하는 이유)
class Cal(object):
    def __init__(self,v1,v2):
        if isinstance(v1,int):
            self.v1 = v1
        if isinstance(v2,int):
            self.v2 = v2
    def add(self):
        return self.v1 + self.v2
    def subtract(self):
        return self.v1 -self.v2
    def setV1(self,v):
        if isinstance(v,int):
            self.v1 = v
    def getV1(self):
        return self.v1
    
c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1(20)