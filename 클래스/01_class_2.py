class unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0},공격력 {1}'.format(self.hp,self.damage))

#클래스 사용
marine1=unit('마린',40,5)
marine2=unit('마린',40,5)
tank=unit('탱크',150,35)

# __init__ : 파이썬에서 쓰이는 생성자
#객체 : 마린이나 탱크 같이 클래스에서 생성되는 것들...이때 이 객체들을 unit class의 인스턴스라고 표현한다.
#주의: __init__함수에서 정의된 self를 제외한 것들은 인스턴트의 클래스 사용시 인스턴스의 갯수들과 일치해야함


#공격유닛
class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage=damage

    def attack(self,location):
        print('{0} : {1} 방향으로 저그를 공격합니다.[공격력 {2}]'\
            .format(self.name,location,self.damage))

    def damaged(self,damage):
        print('{0}: {1} 데미지를 입었습니다.'.format(self.name,damage))
        self.hp -=damage
        print('{0}:현재 체력은 {1}입니다.'.format(self.name,self.hp))
        if self.hp <=0:
            print('{0}이(가) 파괴되었습니다.'.format(self.name))

#파이어벳:공격유닛,화염방사기 사용
firebat1=AttackUnit('파이어뱃',50,16)
firebat1.attack('5시')

#공격을 2번 받았다고 가정한다
firebat1.damaged(25)
firebat1.damaged(25)