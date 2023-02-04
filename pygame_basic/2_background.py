import pygame

pygame.init #반드시 초기화해주기 

#화면크기 설정
screen_width =480 #가로크기
screen_heigth =640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_heigth)) #튜플로 고정함 

#화면 타이틀 설정
pygame.display.set_caption('천문걸 게임') #게임이름

#배경이미지 불러오기
background=pygame.image.load('D:\python\pygame_basic\\background.png')

#이벤트 루프
running = True #게임이 진행중인가?
while running: #반복문
    for event in pygame.event.get(): #어떤 이벤트(동작)가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running=False #게임이 진행중이 아님

    # screen.fill((0,0,255)) #색상으로 배경채울시
    screen.blit(background,(0,0)) #배경 그리기

    pygame.display.update()

#pygame 종료
pygame.quit()