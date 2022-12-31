# 문자열 포맷
# print('a'+'b')
# print('a','b')


#방법1
print('나는 7H똥벌2ㅔ') #일반적인 출력형식
print('나는 %dH똥벌2ㅔ'%7) #단,%d 정수형만 가능함 

print('나는 %s을 좋아합니다' %'개똥')
print('나는 %s을 좋아합니다' %'10')

#%s활용ㅇ
print('나는 %s색과 %s섹을 좋아합니다' %('파랑','빨강'))
print('Samsung은 %c로 시작해요' %'S')

#방법2
print('나는 {}H똥벌2ㅔ' .format(7))
print('나는 {}H똥벌{}ㅔ' .format('ㄱ','2'))
print('나는 {1}H똥벌{0}ㅔ' .format('ㄱ','2'))
#방법3
print('나는 {color} {age}H똥벌2ㅔ' .format(age=7, color='빨강'))
print('나는 {age} {color}H똥벌2ㅔ' .format(age=7, color='빨강'))
print('나는 {color} {age}H똥벌2ㅔ' .format(color='빨강',age=7))

#방법4 v3.6+
age=7
color='빨강'
print(f'나는{age}H똥벌레고 {color}섹을 좋아한다')