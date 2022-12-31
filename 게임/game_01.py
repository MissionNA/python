from pynput import keyboard #키보드 사용을 위한 라이브러리 설치
import os
import time,random #너무 빠른 실행을 막기 귀해 시간 조절

isActive=True
position = {'x':6+7,'y':0+6}
guide ='     #              #'

air=[-1 for i in range(len(guide))] #비행기 움직임 초기화 및 범위설정
air_make_time = 0 #적군비행기 만드는 시간
air_update_time = 0 #적군비행기 움직이는 속도

missile=[-1 for i in range(len(guide))]
missile_update_time=0

score = 0

def key_press(key):
    # print(f'{key} press')
    global position
    global missile

    if key==key.space:         missile[position['x']]=position['y']
    if key == key.up:          position['y'] -=1
    if key == key.down:        position['y'] +=1
    if key == key.left:        position['x'] -=1
    if key == key.right:       position['x'] +=1

        #비행기 포지션 범위
    if position['x'] <6:       position['x'] =6
    if position['x'] >19:      position['x'] =19
    if position['y'] <0 :      position['y'] =0
    if position['y'] >9:       position['y'] =9
def key_release(key):
    # print(f'{key} release')
    if key == keyboard.Key.esc:
        global isActive
        isActive = False
        return False

# with keyboard.Listener(on_press=key_press,on_release=key_release) as keylistener:
#     keylistener.join()

listener=keyboard.Listener(on_press=key_press,on_release=key_release)
listener.start()


print('실행중입니다.')




while isActive:
    os.system('cls') #화면의 출력물을 지움


    if air_make_time>5:
        air_make_time=0
        idex = random.randint(6,19)
        if air[idex] == -1:
            air[idex] =0 #한라인에 적군비행기가 생성되어있으면 만들지 안만들지


    print('     ################')
    for i in range(10): #y
        for k in range(len(guide)): #x
            if position ['x'] == k and position ['y'] == i:     

                #적기 충돌
                if air[k]==position['y']:
                    print('※',end='')
                    isActive=False
                else:
                    print('♝',end='')
            elif air[k] > -1 or missile[k] >-1:
                if air[k] ==i:
                    
                    if air[k] == missile[k]:
                        print('※',end='')
                        score+=10
                        air[k] =-1
                        missile[k]=- 1
                    else:
                        print('▼',end='') 
                elif missile[k] == i:
                     print('△',end= '')
                else: 
                    print (guide[k], end='') 
            else:
                print(guide[k], end='') #end='' 옆으로 붙여서 출력하기 위해
        print()
    print('     ################') 
    
    print(f"x:{position['x']}, y:{position['y']}")
    print(f'당신의 점수는{score+2340}점 입니다.')
    time.sleep(0.1) 

#적군 내려오기
    if air_update_time > 2:
        air_update_time=0
        for i ,val in enumerate(air):
            if val > -1:
                air[i] += 1 #한칸씩 내려오기
                if air[i]>9: #만약 끝까지 내려오면
                    air[i]= -1 #클리어 시키고 올라가서 
    #미사일 생성/이동
    if missile_update_time>1:
       missile_update_time=0

    for i ,val in enumerate(missile):
        if val>-1:
            missile[i]-=1
    
    air_make_time+=1
    air_update_time+=1

    missile_update_time += 1

print('게임을 종료합니다.')
del listener  
