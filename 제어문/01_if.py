#형식
# if 조건:
#   실행 명령문

weather = input('오늘 날씨가 어떄요?')
weather = ''

if weather == '비' or weather=='눈' :
    print('부산을 챙기세요') 
elif weather == '미세먼지' : #elseif
    print('마su크를 챙기세요')
else:
    print('날씨가 좋네요')
    
restart=input('게임을 다시 시작하겠습니까? Y/N')
restart=''
if restart=='Y':
    print('다시 시작하는 중...')
    isActive=True
elif restart=='N':
    print('게임을 종료합니다.')
    isActive=False