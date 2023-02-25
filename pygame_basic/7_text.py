import pygame
pygame.init() #반드시 초기화해주기 

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
character=pygame.image.load('D:\python\pygame_basic\\enemy.png')
character_size=character.get_rect().size #이미지크기 구하기
character_width=character_size[0] #캐릭터 가로크기
character_heigth=character_size[1] #캐릭터 세로크기

character_x_pos= (screen_width/2)-(character_width/2) #캐릭터포지션
character_y_pos= screen_heigth-character_heigth




# 이동할 좌표
to_x = 0
to_y = 0
#이속
character_speed = 1
to_WHY = 1
#적캐릭터
enemy=pygame.image.load('D:\python\pygame_basic\\enemy.png')
enemy_size=enemy.get_rect().size #이미지크기 구하기
enemy_width=enemy_size[0] #캐릭터 가로크기
enemy_heigth=enemy_size[1] #캐릭터 세로크기

enemy_x_pos= (screen_width/2)-(enemy_width/2) #캐릭터포지션
enemy_y_pos= (screen_heigth/2)-(enemy_heigth/2) #적포지션

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트,크기)

#총 시간
total_time = 10

#시작 시간정보 
start_ticks = pygame.time.get_ticks() # 시작tick을받아옴


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


    #충돌처리 좌표 정보 업뎃
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos


    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    #충돌 체크 
    if character_rect.colliderect(enemy_rect):
         print('충돌')
         running = False
    
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #배경 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기

    #타이머 집어넣고 경과시간계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000
    #경과시간을 1000으로 나누어서 초(s) 단위로 표시
                                                              #형식   #글자색상
    time = game_font.render(str((total_time - elapsed_time)), True , (255,0,0))
    screen.blit(time,(10,10))
    #만약 시간 <0이면 종료
    if total_time - elapsed_time <= 0:
        print('타임아웃')
        running = False
    pygame.display.update()
pygame.time.delay(2000)#2초 대기 후 종료

#pygame 종료
pygame.quit()