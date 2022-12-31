# #표준 입출력

# print('Python','Java') # 한칸 띄워서 출력
# print('Python'+'Java') #붙여서 출력

# #sep(separation):분리,구분
# print('Python','Java','JavaScript',sep=',') #쉼표를 출력하고 싶을떄
# print('Python','Java','JavaScript',sep=' vs ')

# print('Python','Java',sep=', ',end=' ')
# print('무엇이 더 재밌을까요?')

#시험성적
# score ={'수학':0,'영어':50,'코딩':100}
# for subject,score in score.items():
#     print(subject,score)


# score ={'수학':0,'영어':50,'코딩':100}
# for subject,score in score.items():
#     print(subject.ljust(4),str(score).rjust(4),sep=':')


#은행 기대 순번표 
#001, 002, 003

# for number in range(1,21):
#     print('대기번호: '+ str(number).zfill(3))

# print('2'.zfill(3)) #002
# print('123'.zfill(5)) #00123
# print('5'.rjust(5,'0')) #50000
# print('5'.ljust(5,'0')) #00005


answer=input('아무거나 입력해주세요 :')
print('입력하신 값은'+ answer +'입니다.')

print(type(answer))

answer=10
print(type(answer))
