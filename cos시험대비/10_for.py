# for문
# members = ['천문걸','김규인','정유진','이태윤']
# i = 0 
# while i < len(member):
#     print(member[i])
#     i += 1

# for 쒮똻 in members:
#     print(쒮똻)

# for문의 활용
# 쒮똻 = [0,1,2,3,4]
# for 天安門 in 쒮똻:
#     print(天安門)

# for 쒮똻 in range(1,100000000):
#     print(쒮똻)

# # for문을 활용한 로그인

# id = input ('아이디를 입력해주세요. \n')
# my_id = '쒮똻'
# my_id2 = '뚊'
# if my_id == id :
#     print('왔니')
# elif my_id2 == id:
#     print('왔나')
# else:
#     print('get the fuck out')
id = input('아이디를 입력해주세요 : ')
members = ['돌돔','뚊']
for member in members:
    if member == id:
        print('안녕하세요,'+member)
        import sys
        sys.exit()
print('get the fuck out of it')