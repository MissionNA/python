#문자열 처리 함수
from operator import index
from platform import python_branch


pie='piE iz Dlous'
print(pie.lower())
print(pie.upper())

print(pie[:10].lower())
print(pie[10].islower())

print(len(pie))
print(pie.replace('piE','hamburger'))


index = pie.index('i') 
print(index)

index=pie.index("i",index+1)
print(index)

print(pie.find('Java'))
print(pie.index("Java"))
print('hi')

#특정글자가 몇번이나 들어가는가
print(pie.count('i'))