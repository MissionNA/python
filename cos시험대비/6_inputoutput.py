
# in_str = input('입력해주세요.\n') #채팅만들기
# print(in_str.lower()+'hello') #upper - 대문자 vV - lower

# 입출력 활용
in_str = input('아이디를 입력해주세요.\n')
id_01 = '0349'
id_02 = 'sfjk'
if id_01 == in_str:
    print('안녕하세요,',id_01)
elif id_02 == in_str:
    print('안녕하세요,id_02')
else:
    print('접속이 차단되었습니다.')
    in_str = input('아이디를 확인해주세요.\n')