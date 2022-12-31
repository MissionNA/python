#멀티미디어 지원하는 라이브러리 설치
import pygame #무료오픈쏘오쓰으

#스크린 생성
pygame.init() #뭔가를 만들때 무조건 init쓰기
SCREEN = pygame.display.set_mode((400,600))
pygame.display.set_caption('날아오는 유성 피하기')

while True:
    pygame.display.flip()