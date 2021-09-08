# -*- coding: utf-8 -*-

import pygame
import random as rnd
import time
from bullet import Bullet
from player import Player, Background

# 충돌 감지 함수
def collision(obj1, obj2):
    dist = ((obj1.pos[0] - obj2.pos[0]) ** 2 + (obj1.pos[1] - obj2.pos[1]) ** 2) ** 0.5
    return dist < 20

# 텍스트 출력 함수
def draw_text(txt, size, pos, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)

pygame.init()
WIDTH, HEIGHT = 1000, 800

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("총알 피하기")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 객체 생성
player = Player(WIDTH/2, HEIGHT/2)
bg = Background(0, 0)

# 배경 음악 재생
pygame.mixer.music.load('../resource/bgm.wav')
pygame.mixer.music.play(-1)

# 효과음 불러오기
effect_sound = pygame.mixer.Sound('../resource/sound effect.wav')

# 폭발 이미지 불러오기 및 이미지 크기 조정
explosion = []
explosion.append(pygame.image.load("../resource/1.png"))
explosion.append(pygame.image.load("../resource/2.png"))
explosion.append(pygame.image.load("../resource/3.png"))
for i in range(3):
    explosion[i] = pygame.transform.scale(explosion[i], (130, 130))

# 총알 생성
bullets_red = [Bullet(5, (255,0,0)) for _ in range(4)]
bullets_green = [Bullet(8, (0,255,0)) for _ in range(3)]
bullets_magenta = [Bullet(11, (255,0,255)) for _ in range(3)]
bullets = bullets_red + bullets_green + bullets_magenta

# 변수 선언
running = True
gameover = False
loop = True
write_result = True
exp = False
exp_x, exp_y = 0, 0
collision_time = 0
time_for_adding_bullets = 0
playtime = 0
life = 100
score = []

time.sleep(0.5)

# 게임 실행
while running:
    
    dt = clock.tick(FPS)
    
    # 배경 화면 출력
    screen.fill((0,0,0))
    bg.update(dt, screen)
    bg.draw(screen)
    
    # 방향키 조정 및 그에 따른 배경 움직이기
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)
                bg.goto(-0.2, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1, 0)
                bg.goto(0.2, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, -1)
                bg.goto(0, -0.2)
            elif event.key == pygame.K_DOWN:
                player.goto(0, 1)
                bg.goto(0, 0.2)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1, 0)
                bg.goto(0.2, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1, 0)
                bg.goto(-0.2, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
                bg.goto(0, 0.2)
            elif event.key == pygame.K_DOWN:
                player.goto(0, -1)
                bg.goto(0, -0.2)
    
    # 게임 진행 시, 실행
    if gameover == False:
        playtime += dt
        time_for_adding_bullets += dt
        
        # 비행기 출력
        player.update(dt, screen)
        if loop:
            player.draw(screen)
            
        # 총알 추가
        if time_for_adding_bullets > 5000:
            bullets.append(Bullet(5, (255,0,0)))
            bullets.append(Bullet(8, (0,255,0)))
            bullets.append(Bullet(11, (255, 0, 255)))
            time_for_adding_bullets -= 5000
    
        # 충돌 감지 및 무적        
        if loop:
            for b in bullets:                
                if collision(player, b):
                    # 충돌 시, 총소리 효과음 실행
                    effect_sound.play()
                    
                    # 충돌 시, 생명력 차감
                    if b in bullets_red: life -= 20
                    elif b in bullets_green: life -= 30
                    else: life -= 40
                        
                    # 충돌 시, 충돌 위치와 시간, boolean 타입 변경
                    collision_time = time.time()    
                    loop = False
                    exp_x, exp_y = player.pos[0], player.pos[1]
                    exp = True if life > 0 else False
                        
        # 무적 기간 동안 비행기 반짝거리기
        if loop == False:
            if (playtime // 100 % 10) % 2 == 0 :
                player.draw(screen)
        
        # 생명력이 0이 되면, 잠시 멈췄다가 게임 오버
        if life <= 0:
            life = 0            
            time.sleep(1.5)
            gameover = True
            
        # 충돌 시, 폭발 이미지 출력
        if exp:
            screen.blit(explosion[(playtime // 50) % 3],(exp_x - 65, exp_y - 65))
        if time.time() >= collision_time + 1:
            exp = False
            
    # 총알 출력
    for b in bullets:
        b.update_and_draw(dt, screen)
        
    # 좌측 상단에 실시간 생존 시간과 현재 총알 개수 출력
    txt = f"Time: {playtime/1000:.1f} / Bullets: {len(bullets)}"
    draw_text(txt, 32, (10, 10), (255,255,255))
    
    # 생명력을 막대 그래프와 숫자로 나타내기
    pygame.draw.rect(screen, (255,0,0), [30,70,300,30]) # Red
    pygame.draw.rect(screen, (0,255,0), [30,70,life * 3,30]) # Green
    draw_text(str(life), 32, (350, 70), (255,255,255))
        
    # 무적 해제          
    if time.time() >= collision_time + 3:
        loop = True
        
    # 게임 종료 시 실행
    if gameover:
        # 게임 오버 문구를 출력
        txt1 = "GAME OVER"
        draw_text(txt1, 100, (WIDTH/2 - 300, HEIGHT/2 - 150), (255,255,255))
        
        # 결과 기록
        if write_result:
            try:
                with open('../resource/result.txt','r') as f:
                    score = list(map(int,f.read().split()))
            except FileNotFoundError: pass
                
            score.append(playtime)
            score.sort(reverse=True)
                
            if len(score) > 10:
                del score[-1]
                
            with open('../resource/result.txt','w') as f:
                for i in score:
                    f.write(f"{i} ")
                        
            write_result = False
        
        # 기록된 생존시간을 화면에 출력
        txt1 = f"Survival Time: {playtime/1000:.1f}s"
        draw_text(txt1, 40, (WIDTH/2 - 200, HEIGHT/2), (255,255,255))
        
        # 현재 기록이 순위권에 있을 경우, 순위를 빨간색으로 강조하여 출력
        if playtime in score:
            txt = f"Your Rank: {score.index(playtime) + 1}"
            draw_text(txt, 40, (WIDTH/2 - 130, HEIGHT/2 + 100), (255,0,0))            
        # 현재 기록이 순위권에 없을 경우, 기록이 순위권에 없다는 문구를 출력
        else:
            txt = f"Your record is not in the rankings."
            draw_text(txt, 25, (WIDTH/2 - 220, HEIGHT/2 + 100), (255,255,255))
    
    # 화면 업데이트
    pygame.display.update()
    

# 게임 종료
pygame.quit()