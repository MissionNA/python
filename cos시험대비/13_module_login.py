from auth import login
id = input('아이디를 입력 ㄱ\n')
# 복잡하고 더럽게 많은 코드
if login(id):
    print(id)
else:
    print(False)
