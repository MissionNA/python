#리스트 []:내용의 변경과 추가 가능

#지하철 칸별로 10명,20명,30명
# subway1=10
# subway2=20
# subway3=30

subway=[10,20,30]
print(subway)

subway =['성민준','오현수','오주완','김규인','천문걸','김동형']
print(subway)

print(subway.index('오현수'))

# subway.append('성민준') #자료 추가시 맨뒤에 추가됨
# print(subway)

subway.insert(5,'성민준') #위치 지정해서 추가할때
print(subway)

#지하철에서 내림(한명씩 뒤에서)
# print(subway.pop(3))
# print(subway)

subway.append('김규인')
# subway.sort()
subway.reverse()
print(subway)
print(subway.count('김규인'))

#오름차순 정렬
num_list = [5,2,4,3,1]

num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료를 함께 사용도 가능
mix_list = ['이성희',20,True]
print(mix_list)
num_list = [5,2,4,3,1]
str(num_list)
print(num_list)


#혼합도 가능
# mix_list.extend(num_list)
# print(mix_list)
# mix_list.sort()
# mix_list.reverse() 아직 해결 못함
