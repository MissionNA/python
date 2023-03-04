import os
import pygame
##########################################################################
#기본초기화(반드시해야하는것들)
pygame.init() #반드시 초기화해주기 

#화면크기 설정
screen_width =640 #가로크기
screen_heigth =480 #세로크기
screen = pygame.display.set_mode((screen_width,screen_heigth)) #튜플로 고정함 

#화면 타이틀 설정
pygame.display.set_caption('팡문철 팡팡')

#FPS
clock = pygame.time.Clock()
##########################################################################

#1.사용자 게임 초기화 (배경화면,게임 이미지,좌표,폰트 등등)
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path,'images') #images 폴더 위치 반환

#배경만들기
background = pygame.image.load(os.path.join(image_path,'background.png'))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,'character.png'))
cs =character.get_rect().size
cw = cs[0] #캐릭터 가로
ch = cs[1] #캐릭터 세로

cx = (screen_width/2) - (cw/2)
cy = screen_heigth - ch - stage_height

#캐릭터 이동방향
character_to_x = 0
#캐릭터 이속
character_speed = 5


running = True 
while running: 
    dt = clock.tick(60) 

    # 2.이벤트처리 (키보드 마우스 등등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running=False #게임이 진행중이 아님
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기발사
                pass
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    #3.게임캐릭터 위치정의

    #4.충돌 처리
    
    #5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_heigth-stage_height))
    screen.blit(character,(cx,cy))
    pygame.display.update()

pygame.quit()