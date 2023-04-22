id = input('아이디를 입력해 주세요.\n')
def login(_id):
    members = ['뚊','돌돔','문걸']
    for member in members:
        if member == _id:
            return True
    return False
if login(id):
    print('안녕..'+id)
else:
    print('누구세요?')