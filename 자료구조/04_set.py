#집합 = set
#중복안됨,순서(숫자:오름차순 / 문자:순서X)

my_set={1,2,3,3,3}
print(my_set)

python ={'오주완','오현수','김규인','천문걸','김도형','이성희'}
java ={'이성희','이미진'}

#교집합=(intersection)-python과 java를 모두 할 수 있는 개발자
print(python & java) #방법 1
print(python.intersection(java)) #방법 2

#합집합:python을 할 수 있거나 java를 할 수 있는 개발자
print(python|java) #방법1
print(python.union(java)) #방법2

#차집합:python을 할수 있지만 java를 할 수 없는 사람
print(python-java)
print(python.difference(java))

#java를 할 수 있는 개발자가 늘어남
java.add('김규인')
print(java)

#python을 잊어버린 개발자
python.remove('김규인')
print(python)
