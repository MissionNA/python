#반복문
#형식:for 변수 in [변수에 들어갈 내용]

# print('대기번호:1')

# for waiting_no in [1,2,3,4,5] :
#     print('대기번호 : {}'.format(waiting_no))

# for waiting_no in range(1,101) :
#     print('대기번호 : {}'.format(waiting_no))


starbucks=['철아저씨','토르','나는 나무']
for customer in starbucks :
    print('{}님,커피가 준비되었습니다.'.format(customer))
