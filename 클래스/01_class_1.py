# 클래스: 파이썬에서 제일 중요한 부분형식
# 형식: class 클래스 이름:

#마린:공격 유닛,군인,총을 쏠 수 있음
name ='마린'#유닛 이름
hp=40 #유닛의 체력
damage=5 #유닛의 공격력

print('{} 유닛이 생성되었습니다.'.format(name))
print('체력 {0},공격력 {1}\n'.format(hp,damage))

#탱크: 공격 유닛,포를 쏠 수 있는 유닛...일반모드/시즈 모드 有

tank_name ='탱크'#유닛 이름
tank_hp=150 #유닛의 체력
tank_damage='25,폭발' #유닛의 공격력

print('{} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {0},공격력 {1}\n'.format(tank_hp,tank_damage))

#공격
def attack(name,location,damage):
    print('{0} : {1} 방향으로 저그를 공격합니다.[공격력 {2}]'.format(name,location,damage))

attack(name,'1시',damage)
attack(tank_name,'1시',tank_damage)

