#형식 :사전 ={}
cabinet ={3:'필로소피', 100:'파이썬'}
print(cabinet[3])
print(cabinet[100])

#이런 형식으로도 출력 가능
print(cabinet.get(3))

print(cabinet.get(5)) #None 하고 프로그램 계속 실행
# print(cabinet[5]) #에러뜨고 멈춤

#사전자료안에 값을 확인(키값을 넣어서 확인)
print(3 in cabinet) #있냐 없냐 묻는거(True)
print(5 in cabinet) #있냐 없냐 묻는거 (False)

cabinet = {'A-3':'유석재','B-100':'김테호'}
print(cabinet['A-3']) #대괄호 넣으면 Dictionary Key 나옴
print(cabinet['B-100']) #대괄호 넣으면 Dictionary Key 나옴

#키추가
cabinet['C-20']='조세호'
print(cabinet) 
print(cabinet['C-20']) #대괄호 넣으면 Dictionary Key 나옴

#키삭제
del cabinet['A-3']
print(cabinet)

#키들만 출력
print(cabinet.keys())

#키값 확인
print(cabinet.values())

#사전전부삭제
cabinet.clear()
print(cabinet) #{}을 출력

print(cabinet.clear()) #None을 출력
