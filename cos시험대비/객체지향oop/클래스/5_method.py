#클래스 메소드
class Cs:
    @staticmethod
    def static_method():
        print('Static method')
    @classmethod
    def class_method(cls):
        print('Class method')
    
    def instance_method(self):
        print('Instance method')

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()

class Cs():
    count = 0 
    def __init__(self):
        Cs.count +=1
    @classmethod
    def getCount(cls):
        return Cs.count
    

i1 =Cs()
i2 =Cs()
i3 =Cs()
i4 =Cs()
print(Cs.getCount())
