#지역변수 : 함수내에서만 쓸수 있는 변수 like 동백전
#전역변수: 상관없이 프로그램 전체에 다 쓸 수 있는 변수 like 현대카드

gun=10 #전역변수

#지역변수 사용
# def checkpoint(soldiers): #경계근무 하는 군인
#     gun = 20 #지역변수를 만듦
#     gun = gun - soldiers
#     print('[함수 내] 남은 총:{0}'.format(gun))

# print('전체 총 : {0}'.format(gun))
# checkpoint(2) #2명이 경계근무 나감
# print('남은 총: {0}'.format(gun))

# 전역변수
# def checkpoint(soldiers):
#     global gun #global:전역변수 불러오는거
#     gun=gun-soldiers
#     print('[함수 내] 남은 총:{0}'.format(gun))

# print('전체 총 : {0}'.format(gun))
# checkpoint(2) #2명이 경계근무 나감
# print('남은 총: {0}'.format(gun))


def checkpoint(gun,soldiers):
    gun=gun-soldiers
    print('[함수 내] 남은 총:{0}'.format(gun))
    return gun

print('전체 총 : {0}'.format(gun))
gun = checkpoint(gun,2)
print('남은 총: {0}'.format(gun))