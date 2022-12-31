#다양한 출력 폼

#빈 자리를 빈공간으로 두고,오른쪽 정렬을 하되,총 10자리 공간을 확보
print('{0: >10}'.format(500))
print('{0: <10}'.format(500))

#소수점 출력
print('{0:f}'.format(5/3)) #float(f) :실수형

print('{0:.2f}'.format(5/3))
