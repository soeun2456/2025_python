'''문제 5. 장애물 점프 게임 (Dino Run Style)
목표: 다가오는 장애물을 점프해서 피하는 게임입니다.

플레이어는 제자리에서 점프(SPACE 키)만 가능합니다.

장애물은 오른쪽에서 왼쪽으로 이동합니다.

점프 로직: 중력을 적용하여 올라갔다가 다시 내려와야 합니다. (예: y_velocity 사용)

학습 포인트:

중력(Gravity)과 점프 물리 구현 (vel_y 활용).

상태 관리 (점프 중인지 아닌지 is_jumping 플래그).

배경 스크롤링의 기초 원리(장애물 이동).'''

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("문제5 - 점프 게임 (스코어 기능 추가)")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

player = pygame.Rect(50, 300, 40, 40)
obstacle = pygame.Rect(600, 310, 30, 30)

vel_y = 0
is_jumping = False
gravity = 0.5

score = 0
obstacle_passed = False # 장애물을 넘었는지 확인하는 플래그

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # 점프는 바닥에 있을 때만 가능
            if event.key == pygame.K_SPACE and not is_jumping:
                vel_y = -10  
                is_jumping = True

    # 1. 중력 적용 (점프 로직)
    if is_jumping:
        player.y += vel_y
        vel_y += gravity
        # 땅에 닿으면 멈춤
        if player.y >= 300:
            player.y = 300
            is_jumping = False
            vel_y = 0

    # 2. 장애물 이동 (오른쪽 -> 왼쪽)
    obstacle.x -= 5

    # ------------------ 핵심 로직: 점수 계산 ------------------
    # 장애물의 오른쪽 끝(right)이 플레이어의 왼쪽 끝(left)보다 작아지면 
    # 즉, 장애물이 플레이어를 완전히 지나쳤다면?
    if obstacle.right < player.left:
        # 아직 점수 처리가 안 된 장애물이라면 점수 증가
        if not obstacle_passed:
            score += 1
            print(f"장애물 돌파! 현재 점수: {score}")
            obstacle_passed = True # '이미 넘은 장애물'로 표시
    # --------------------------------------------------------

    # 3. 장애물 리스폰 (화면 왼쪽 끝으로 사라지면)
    if obstacle.right < 0:
        obstacle.x = 600 # 오른쪽 끝으로 이동
        obstacle_passed = False # 새로운 장애물이므로 플래그 초기화

    # 4. 충돌 체크 (게임 종료)
    if player.colliderect(obstacle):
        print(f"충돌! 최종 점수: {score}")
        running = False

    # 화면 그리기
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0,0,0), (0, 340), (600, 340), 2) # 땅
    
    # 플레이어 (파란색)
    pygame.draw.rect(screen, (50, 50, 255), player)
    
    # 장애물 (빨간색)
    pygame.draw.rect(screen, (255, 50, 50), obstacle)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()