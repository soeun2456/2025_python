'''문제 1. 마우스로 도망가는 공 잡기 (Clicker Game)
목표: 화면에 무작위로 나타나는 공을 마우스로 클릭해서 잡는 게임을 만드세요.

공은 일정 시간마다 새로운 위치로 순간이동합니다.

마우스 클릭 시 공 위에서 클릭했는지 판별(collidepoint)하여 점수를 올립니다.

제한 시간(예: 10초)이 지나면 게임이 종료됩니다.

학습 포인트:

pygame.mouse.get_pos()와 마우스 이벤트 처리.

rect.collidepoint(pos) 메서드 활용.

pygame.time.get_ticks()를 이용한 시간 제한 구현.'''

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("문제1 - 공 잡기")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# 공 설정
ball_rect = pygame.Rect(0, 0, 40, 40)
ball_rect.center = (300, 200)
move_timer = 0
score = 0
start_time = pygame.time.get_ticks()
game_duration = 10000  # 10초

running = True
while running:
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    remaining_time = max(0, (game_duration - elapsed_time) // 1000)

    if elapsed_time > game_duration:
        print(f"게임 종료! 최종 점수: {score}")
        running = False

    # 공 이동 타이머 (0.5초마다 이동)
    move_timer += 1
    if move_timer > 30:
        ball_rect.x = random.randint(0, 560)
        ball_rect.y = random.randint(0, 360)
        move_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 위치와 공의 충돌 확인
            if ball_rect.collidepoint(event.pos):
                score += 1
                # 잡으면 즉시 다른 곳으로 이동
                ball_rect.x = random.randint(0, 560)
                ball_rect.y = random.randint(0, 360)
                move_timer = 0

    screen.fill((255, 255, 255))
    pygame.draw.ellipse(screen, (255, 0, 0), ball_rect)
    
    score_text = font.render(f"Score: {score}  Time: {remaining_time}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()