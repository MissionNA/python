#오버라이드 형식
class C1:
    def m(self):
        return '활과 화살'
    
class C2(C1):
    def m(self):
        return super().m() + ' Autobow'
    
o = C2()
print(o.m())