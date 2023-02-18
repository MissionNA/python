import pygame
pygame.init #반드시 초기화해주기 

#화면크기 설정
screen_width =480 #가로크기
screen_heigth =640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_heigth)) #튜플로 고정함 

#화면 타이틀 설정
pygame.display.set_caption('한문철 게임') #게임이름

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background=pygame.image.load('D:\python\pygame_basic\\background.png')


# 캐릭터 불러오기
character=pygame.image.load('D:\python\pygame_basic\\hharacter.png')
character_size=character.get_rect().size #이미지크기 구하기
character_width=character_size[0] #캐릭터 가로크기
character_heigth=character_size[1] #캐릭터 세로크기

character_x_pos= (screen_width/2)-(character_width/2) #캐릭터포지션
character_y_pos= screen_heigth-character_heigth




# 이동할 좌표
to_x = 0
to_y = 0
#이속
character_speed = 2
to_WHY = 0.054321

#이벤트 루프
running = True #게임이 진행중인가?
while running: #반복문
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): #어떤 이벤트(동작)가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running=False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += to_WHY

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x =0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y =0
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt



    if  character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos >screen_width - character_width:
        character_x_pos = screen_width - character_width

    if  character_y_pos <0:
        character_y_pos = 0
    elif character_y_pos >screen_heigth - character_heigth:
        character_y_pos = screen_heigth - character_heigth






    screen.blit(background,(0,0)) #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos)) #배경 그리기

    pygame.display.update()

#pygame 종료
pygame.quit()