#기본값
def profile(name,age,main_lang):
    print('이름:{0}\t나이:{1}\t사용 언어:{2}'.format(name,age,main_lang))


# profile('천문걸',15,'파이썬')
# profile('이성희',25,'자바')

def profile(name,age=14,main_lang='파2선'):
    print('이름:{0}\t나이:{1}\t사용 언어:{2}'.format(name,age,main_lang))

profile('천문걸')
profile('이성희')