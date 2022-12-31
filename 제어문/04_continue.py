#for문이나 while문 중간에 넣어 조건을 실행하는 문

#형식
#for 조건
#    실행문
#    continue

# absent = [2,5] #결석
# for student in range(1,11): #1~10까지 학번이 있다
#     if student in absent:
#         continue
#     print('{0},책을 읽어보세요'.format(student))

absent=[2,5] #결석
no_book=[7] #책을 가지고 오지 않았다.

for student in range(1,11): #1~10까지 학번이 있다.
    if student in absent:
        continue
    elif student in no_book:
        print('오늘 수업 여기까지....{0}는 교무실로 따라와'.format(student))
        break
    print('{0},책 읽어'.format(student))
    