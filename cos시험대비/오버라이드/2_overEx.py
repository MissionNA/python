# 오버라이드의 활용

class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1 + self.v2
        Cal._history.append('더하기: %d+%d=%d' % (self.v1,self.v2,result))
        return result
    
    def subtract(self):
            result = self.v1 - self.v2
            Cal._history.append('빼기: %d-%d=%d' % (self.v1,self.v2,result))
            return result

    def setV1(self,v):
         if isinstance(v,int):
            self.v1 = v

    def getV1(self):
         return self.v1
    
    @classmethod
    def history(cls):
        for item in Cal._history:
             print(item)
    def info(self):
         return 'Cal에 입력되는 값 =>  v1 : %d, v2 : %d' % (self.v1,self.v2)

class CalMultiply(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append('곱하기기: %dx%d=%d' % (self.v1,self.v2,result))
        return result
    def info(self):
         return 'CalMultiply에 입력되는 값 =>  %s' % super().info()
    
class Caldivide(CalMultiply):
    def divide(self):
        result = self.v1 / self.v2
        Cal._history.append('나누기기기: %d/%d=%d' % (self.v1,self.v2,result))
        return result
    def info(self):
         return 'CalDivide에 입력되는 값 =>  %s' % super().info()


c0 = Cal(30,20)
print(c0.info())
c1= CalMultiply(10,10)
print(c1.info())
c2 = Caldivide(20,10)
print(c2.info())
