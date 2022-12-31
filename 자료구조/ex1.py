# # Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다
# #참석률을 높이기 위해서 댓글 이벤트를 진행하기로 했습니다
# #댓글 작성자들 중에 추첨을 통해 1명을 치킨,3명은 커피 쿠폰을 받게 됩니다.

# #조건1:편의상 댓글은 20명이 작성하였고, 아이디는 1~20까지라고 가정한다.
# #조건2:댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# #조건3: random 모듈의 shuffle과 sample(번호추출)을 활용

# #출력형식
# #-- 당첨자 발표 --
# #   치킨당첨자 : 1
# #   커피당첨자 :[2,3,4]
# #-- 축하합니다.--

# #연습
# from random import randint, sample, shuffle
# list=[1,2,3,4,5]
# shuffle(list)
# print (list)
# print(sample(list,1)) #lst 안에 있는 값을 1일경우 하나 추출

from random import *
users = range(1,21) #1에서 20까지 숫자의 범위만듦
users=list(users)
shuffle(users) #숫자섞기

# 4명중 1명은 치킨,3명은 커피
winners = sample(users,4)

print('-- 당첨자 발표 --')
print('치킨당첨자:{}'.format(winners[0]))
print('커피당첨자:{}'.format(winners[1:]))
print('--축하합니다--')