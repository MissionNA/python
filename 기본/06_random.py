# random 함수 사용해서 로또번호 만들기
from random import *
from secrets import randbelow
print(random()) #0.0~1.0 미만 임의의 값
print(random()*10) #0.0~10.0 미만 임의의 값
#정수형 출력
print(int(random()*10)) #0.0~10 미만 임의의 값
print ('로또번호 출력')
print(int(random()*45)+1) #1~45 이하 임의의 값
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(randint(1,45))