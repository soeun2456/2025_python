'''문제 3. 스페이스 슈터 (Shooting Game)
목표: 플레이어가 스페이스바를 누르면 미사일이 위로 발사되어 적을 맞추는 게임을 만드세요.

적은 위쪽에서 좌우로 왔다 갔다 움직입니다.

미사일은 플레이어 위치에서 생성되어 위(y 감소)로 이동합니다.

미사일과 적이 충돌하면 적의 위치를 재설정하고 점수를 얻습니다.

학습 포인트:

투사체(총알) 시스템 구현.

플레이어 위치를 기준으로 객체 생성 (bullet.center = player.center).

두 동적 객체(총알, 적) 간의 충돌 처리.'''

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("문제3 - 슈팅 게임")
clock = pygame.time.Clock()

player = pygame.Rect(280, 350, 40, 40)
enemy = pygame.Rect(280, 50, 40, 40)
enemy_speed = 3
bullets = []

running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 총알 생성 (플레이어 중앙에서 발사)
                b = pygame.Rect(0, 0, 5, 10)
                b.center = player.center
                bullets.append(b)

    # 플레이어 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 4
    if keys[pygame.K_RIGHT]: player.x += 4

    # 적 이동 (좌우 왕복)
    enemy.x += enemy_speed
    if enemy.right > 600 or enemy.left < 0:
        enemy_speed *= -1

    # 총알 이동 및 충돌
    for b in bullets[:]:
        b.y -= 7
        if b.colliderect(enemy):
            score += 1
            bullets.remove(b)
            # 적 리스폰 (위치 초기화)
            enemy.x = 280
            enemy.y = 50
        elif b.bottom < 0:
            bullets.remove(b)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    for b in bullets:
        pygame.draw.rect(screen, (255, 255, 0), b)

    pygame.display.set_caption(f"Score: {score}")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()