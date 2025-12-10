'''문제 4. 공 튀기기 (Bounce Ball / Pong)
목표: 벽에 튕기는 공을 바닥에 떨어뜨리지 않고 받아내는 게임입니다.

공은 speed_x, speed_y를 가지며 벽에 닿으면 방향이 반전됩니다(* -1).

플레이어(패들)는 바닥에서 좌우로 움직입니다.

공이 바닥(HEIGHT)에 닿으면 게임 오버, 패들에 닿으면 위로 튕겨 나갑니다.

학습 포인트:

물리 기초: 속도 반전(반사) 구현.

화면 경계 처리 (rect.left < 0 등).

패들과 공의 충돌 시 Y축 속도 제어.'''

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("문제4 - 공 튀기기")
clock = pygame.time.Clock()

paddle = pygame.Rect(250, 370, 100, 10)
ball = pygame.Rect(300, 200, 15, 15)
ball_vx, ball_vy = 4, 4

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # 패들 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: paddle.x -= 6
        if keys[pygame.K_RIGHT]: paddle.x += 6
        paddle.clamp_ip(screen.get_rect()) # 화면 밖 방지

        # 공 이동
        ball.x += ball_vx
        ball.y += ball_vy

        # 벽 충돌 (좌, 우, 상단)
        if ball.left < 0 or ball.right > 600:
            ball_vx *= -1
        if ball.top < 0:
            ball_vy *= -1
        
        # 패들 충돌
        if ball.colliderect(paddle):
            ball_vy *= -1 # 튕겨내기
            ball.bottom = paddle.top # 겹침 방지

        # 바닥 충돌 (게임 오버)
        if ball.bottom > 400:
            game_over = True
            print("게임 오버")

    screen.fill((200, 255, 200))
    pygame.draw.rect(screen, (0, 0, 255), paddle)
    pygame.draw.ellipse(screen, (255, 100, 100), ball)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()