# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1.캐릭터는 화면 가장 아래에 위치,좌우로만 이동 가능
# 2.똥은 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정
# 3.캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4.캐릭터가 똥과 충돌하면 게임 종료
# 5.FPS는 30으로 고정

# [게임 이미지]
# 1.배경 : 480 * 640(가로*세로) - background.png
# 2.캐릭터 : 70 * 70 - character.png
# 3.똥 : 70 * 70 - poo.png
import random
import pygame
##########################################################################
#기본초기화(반드시해야하는것들)
pygame.init() #반드시 초기화해주기 

#화면크기 설정
screen_width =480 #가로크기
screen_heigth =640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_heigth)) #튜플로 고정함 

#화면 타이틀 설정
pygame.display.set_caption('한문철 똥피하기')

#FPS
clock = pygame.time.Clock()
##########################################################################

#1.사용자 게임 초기화 (배경화면,게임 이미지,좌표,폰트 등등)
#배경이미지
background = pygame.image.load('D:/python/pygame_basic/background.png')
#캐릭터만들기
character = pygame.image.load('D:/python/pygame_basic/enemy.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_heigth = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_heigth - character_heigth)

#이동 위치
to_x = 0

character_speed = 15

#똥만들기
poo= pygame.image.load('D:/python/pygame_basic/poo.png')
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_heigth = poo_size[1]
poo_x_pos = random.randint(0,screen_width-poo_width)
poo_y_pos = 0
poo_speed = 15

running = True 
while running: 
    dt = clock.tick(60) 
    # 2.이벤트처리 (키보드 마우스 등등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running=False #게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    #3.게임캐릭터 위치정의
    character_x_pos +=to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    poo_y_pos += poo_speed

    if poo_y_pos > screen_heigth:
        poo_y_pos = 0
        poo_x_pos = random.randint(0,screen_width-poo_width)
    #4.충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poo_rect = poo.get_rect()
    poo_rect.left = poo_x_pos
    poo_rect.top = poo_y_pos

    if character_rect.colliderect(poo_rect):
        print('게임 오버')
        running = False
    #5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(poo,(poo_x_pos,poo_y_pos))
    pygame.display.update()

pygame.quit()
