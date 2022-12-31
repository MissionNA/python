# #반복문
# #형식:while 조건:
# #    위조건에 맞는 실행문

# customer = '토르'
# index=5

# while index >=1 :
#     print('{0}님,햄버거가 준비되었습니다. {1}번 남았습니다.'.format(customer,index))
#     index-=1 #index=index-1
#     if index == 0:
#         print('햄버거는 저희가 먹었습니다^^7')

# customer='토르'
# index=-2

# while True:
#     print('{0},커피가 준비되었다. {1}번 남았다.'.format(customer,index))
#     index +=1 #index=index+1
#     if index == 2:
#         print('end')
customer='토르'
person = 'undefined'

while person != customer :
    print('{0},커피가 준비 되었습니다.'.format(customer))
    person = input('이름이 어떻게 되세요?')
