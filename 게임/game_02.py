# 멀티미디어를 지원하는 라이브러리 설치
import pygame # 무료 오픈소스
from pygame.rect import *
import random 
# 함수선언
def restart():
    global isGameOver,score
    isGameOver=False
    score=0
    for i in range(len(star)):
       recStar[i].y= -1
# 키보드(키값) 정의

def eventProcess():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # 키보드의 키가 눌러졌을 때 이벤트 발생

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.key == pygame.K_LEFT:
                move.x = -1
            if event.key == pygame.K_RIGHT:
                move.x = 1
            if event.key == pygame.K_UP:
                move.y = -1
            if event.key == pygame.K_DOWN:
                move.y =1
            if event.key == pygame.K_r:
                restart()


def movePlayer():
    if not isGameOver:
        recPlayer.x +=move.x
        recPlayer.y +=move.y

    #화면에 출력되는 비행기의 범위 제한
    if recPlayer.x < 0:
        recPlayer.x = 0
    if recPlayer.x > SCREEN_WIDHT-recPlayer.width:
        recPlayer.x = SCREEN_WIDHT-recPlayer.width
    if recPlayer.y < 0:
        recPlayer.y = 0
    if recPlayer.y > SCREEN_HEIGHT-recPlayer.height:
        recPlayer.y = SCREEN_HEIGHT-recPlayer.height
    SCREEN.blit(player,recPlayer)

def timeDelay500ms():
    global time_delay_500ms
    if time_delay_500ms>5:
        time_delay_500ms = 0
        return True
    time_delay_500ms +=1
    return False
    #유성생성

def makeStar():
    if isGameOver:
        return
    if timeDelay500ms():
        
        idex=random.randint(0,len(star)-1)
        if recStar[idex].y == -1:
            recStar[idex].x =random.randint(0,SCREEN_WIDHT)
            recStar[idex].y = 0


def moveStar():
    
    makeStar()
    for i in range(len(star)):
        

    #유성 움직이고 화면제한
        if recStar[i].y == -1:
            continue

        if not isGameOver:
            recStar[i].y += 1
        if recStar[i].y > SCREEN_HEIGHT:
            recStar[i].y = 0

        SCREEN.blit(star[i],recStar[i])
        
#충돌
def checkCollision():
    global score,isGameOver

    if isGameOver:
        return

    for rec in recStar:
        if rec.y == -1:
            continue
        if rec.top < recPlayer.bottom \
            and recPlayer.top < rec.bottom \
            and rec.left < recPlayer.right \
            and recPlayer.left < rec.right: 
            print('충돌')
            isGameOver=True
            break
    score +=1

#게임오버시 출력 문자 동작넣기(깜빡깜빡)
def blinking():
    global time_delay_4sec,toggle
    time_delay_4sec +=1
    if time_delay_4sec > 40:
        time_delay_4sec = 0
        toggle = ~toggle

    return toggle
    


#점수 및 게임상태 화면에 출력
def setText():
    mfont=pygame.font.SysFont('bold',20,True,False)
    SCREEN.blit(mfont.render(
        f'score : {score}',True,'orange'),(10,10,0,0))
    if isGameOver and blinking():
        SCREEN.blit(mfont.render(
            f'Game Over',True,'#610B0B'),(150,300,0,0))
        SCREEN.blit(mfont.render(
            f'press R-Restart',True,'#0B4C5F'),(130,320,0,0))


# 변수선언
isActive = True
SCREEN_WIDHT = 400 # 스크린 가로 변수
SCREEN_HEIGHT = 600 # 스크린 세로 변수

move = Rect(0,0,0,0) # pygame에서 지원하는 Rect : x, y, 가로, 세로

time_delay_500ms=0
time_delay_4sec=0
toggle=False
score=3500
isGameOver=False # 충돌 안된상태부터 시작하므로 값은 False
# 스크린 생성
pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))
pygame.display.set_caption("날아오는 유성 피하기") # 창 이름


# player 넣기(생성)
player = pygame.image.load("D:\pythonWorkspace\게임\player.png") # 파일 위치
player = pygame.transform.scale(player,(20,30)) # 플레이어 가로 세로 비율(50과 80이 비율임)
recPlayer = player.get_rect() #좌표생성

# player 위치 조절
recPlayer.centerx =(SCREEN_WIDHT-10)
recPlayer.centery =(SCREEN_HEIGHT-10)



# 유성 넣기(생성)
star = [pygame.image.load("D:\pythonWorkspace\게임\star.png") for i in range(100)]
recStar=[None for i in range(len(star))]
for i in range(len(star)):
    star[i] = pygame.transform.scale(star[i],(20,20)) # 스타(유성의) 가로 세로 비율(50과 80이 비율임)
    recStar[i] = star[i].get_rect() #좌표생성
    recStar[i].y = -1



clock = pygame.time.Clock()

while isActive:
    SCREEN.fill((0,0,0))
    eventProcess()
    movePlayer()
    moveStar()
    checkCollision()
    setText()
    blinking()

    pygame.display.flip()
    clock.tick(10)