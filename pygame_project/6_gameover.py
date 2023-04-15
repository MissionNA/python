# 1.모든 공을 없애면 게임 종료(성공)
# 2.캐릭터가 공에 닿으면 게임 종료(실패)
# 3.시간 제한 99초 초과 시 게임 종료(실패)



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
character_size =character.get_rect().size
character_width = character_size[0] #캐릭터 가로
character_height = character_size[1] #캐릭터 세로

character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_heigth - character_height - stage_height
 
#캐릭터 이동방향
character_to_x = 0

#캐릭터 이속
character_speed = 5

#무기만들기
weapon = pygame.image.load(os.path.join(image_path,'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한번에 여러 발 발사 가능
weapons = []

#무기 이동 속도 
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path,'balloon1.png')),
    pygame.image.load(os.path.join(image_path,'balloon2.png')),
    pygame.image.load(os.path.join(image_path,'balloon3.png')),
    pygame.image.load(os.path.join(image_path,'balloon4.png'))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18,-15,-12,-9] # 0,1,2,3

#공들 정보
balls= []

#최초로 발생하는 큰 공
balls.append({
    'pos_x':50, #공의 x좌표
    'pos_y':50,  #공의 y좌표
    'img_idx' :0, #공 1번 이미지
    'to_x':3, #x축이동방향, -3이면 왼쪽,3이면 오른쪽
    'to_y':-6, #y축 이동방향,
    'init_spd_y':ball_speed_y[0] #y의 최초속도
})
#사라질 무기,공 정보 저장 할 변수 
weapon_to_remove = -1
ball_to_remove = -1
#폰트 정의
game_font = pygame.font.Font(None,40)
total_time = 22
start_ticks = pygame.time.get_ticks() # 게임 시작시간 정의 

# 게임 종료 메시지(TimeOut,MissionComplete,GameOver)
game_result = 'GAME OVER'




running = True 
while running: 
    dt = clock.tick(30)  
                                              
    # 2.이벤트처리 (키보드 마우스 등등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running=False #게임이 진행중이 아님
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_z: #무기발사
                weapon_x_pos = character_x_pos + (character_width/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
            elif event.key == pygame.K_x: #무기발사
                weapon_x_pos = character_x_pos + (character_width/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
            elif event.key == pygame.K_c: #무기발사
                weapon_x_pos = character_x_pos + (character_width/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
            elif event.key == pygame.K_v: #무기발사
                weapon_x_pos = character_x_pos + (character_width/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
                                
# zxczxczc
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    #3.게임캐릭터 위치정의
    character_x_pos+=character_to_x
    if character_x_pos < 0 :
        character_to_x = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width-character_width
    #무기위치 조정
    weapons = [[w[0],w[1]- weapon_speed] for w in weapons] #무기 위치를 위로 올림
     #무기가 천장에 닿으면 무기 없애기
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0] 

    #공 위치 정의 
    for ball_idx,ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #가로벽에 닿았을 떄 공 이동 위치 변경(튕겨나오는 효과)
        if ball_pos_x<=0 or ball_pos_x> screen_width - ball_width:
            ball_val['to_x'] =  ball_val['to_x']*-1

        #세로위치   :스테이지 튕겨서 올라가는 공처리
        if  ball_pos_y >= screen_heigth - stage_height - ball_height:
            ball_val['to_y'] =  ball_val['init_spd_y']
        else: #그 외의 모든 경우에는 속도를 줄여나감(증가)
            ball_val['to_y'] += 0.5    

        ball_val['pos_x'] += ball_val['to_x']       
        ball_val['pos_y'] += ball_val['to_y']                                                                                           
    #4.충돌 처리

    #캐릭터rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
 
    for ball_idx,ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']
        #공 rect정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        #공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running = False
            break
            #공과 무기들 충돌 처리
        for weapon_idx,weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]
            #무기들 rect정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y 
        #충돌체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx #공없애기
                #가장 작은 공의 크기가 아니라면 다음단계의 공으로 나누기 
                if ball_img_idx < 3: 
                    #현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공 정보 
                    small_ball_rect = ball_images[ball_img_idx+1].get_rect()
                    small_ball_width = small_ball_rect[0]
                    small_ball_height = small_ball_rect[1] 
 
                    #왼쪽으로 팅겨나가는볼
                    balls.append({
                        'pos_x':ball_pos_x+ (ball_width /2) - (small_ball_width/2), #공의 x좌표
                        'pos_y':ball_pos_y + (ball_height/2)- (small_ball_height/2),  #공의 y좌표
                        'img_idx' :ball_img_idx + 1, #공 1번 이미지
                        'to_x':-3, #x축이동방향, -3이면 왼쪽,3이면 오른쪽
                        'to_y':-6, #y축 이동방향,
                        'init_spd_y':ball_speed_y[ball_img_idx+1] #y의 최초속도
                    })
                    #오른쪾으로 튕겨나가는볼
                    balls.append({
                        'pos_x':ball_pos_x+ (ball_width /2) - (small_ball_width/2), #공의 x좌표
                        'pos_y':ball_pos_y + (ball_height/2)- (small_ball_height/2),  #공의 y좌표
                        'img_idx' :ball_img_idx + 1 , #공 1번 이미지
                        'to_x':3, #x축이동방향, -3이면 왼쪽,3이면 오른쪽          
                        'to_y':-6, #y축 이동방향,
                        'init_spd_y':ball_speed_y[ball_img_idx+1] #y의 최초속도
                    })  

                break
            #충돌된 공 and 무기 없애기
        if ball_to_remove > -1:
            del balls[ball_to_remove]  
            ball_to_remove = -1
                
        if weapon_to_remove > -1:
            del weapons[weapon_to_remove]
            weapon_to_remove = -1
    # 모든 공을 없앤 경우 게임 종료(성공)
        if len(balls) == 0:
            game_result = 'Mission Complete'
            running = False

    #5. 화면에 그리기
    screen.blit(background,(0,0))
    for weapon_x_pos,weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx,v in enumerate(balls):
            ball_pos_x = v['pos_x']
            ball_pos_y = v['pos_y']
            ball_img_idx = v['img_idx']
            screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))    
    screen.blit(stage,(0,screen_heigth-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000  # ms -> 초환산    
    timer = game_font.render('Time : {}'.format(int(total_time-elapsed_time)),True,(45,45,45)) 
    screen.blit(timer,(10,10))

    # 시간이 초과했다면
    if total_time - elapsed_time <=0: 
        game_result = 'Time Over'
        running = False
    pygame.display.update()    

msg = game_font.render(game_result,True,(45,45,45))
msg_rect = msg.get_rect(center = (int(screen_width/2),(int(screen_heigth/2)))) 
screen.blit(msg,msg_rect)

pygame.display.update()
# 2초 대기
pygame.time.delay(200)
   
pygame.quit()
if len(balls) == 0 and elapsed_time <= 1.693:
    print(str(elapsed_time) +('초로 최고기록을 갱신하였습니다!'))
elif len(balls) == 0 and elapsed_time > 1.693:
    print(str(elapsed_time)+ ('초로 게임을 끝내셨습니다.'))
else: print('못합니다.')
