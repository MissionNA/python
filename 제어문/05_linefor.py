student=[1,2,3,4,5,6]
print(student)

#학생번호 앞에 100을 붙여야 할때(101,102....)
student=[i+100 for i in student]
print(student)

#학생 이름을 길이로 변환하고 싶다
stydents=['Iron man','Thor','I am groot']
stydents=[len(i) for i in stydents]
print(stydents)

# 학생 이름을 대문자로 바꾸기
stydents=['Iron man','Thor','I am groot']
stydents=[i.upper() for i in stydents]
print(stydents)
