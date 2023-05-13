#오버라이드 형식
class C1:
    def m(self):
        return '석궁'
    
class C2(C1):
    def m(self):
        return super().m() + ' Autobow'
    
o = C2()
print(o.m())