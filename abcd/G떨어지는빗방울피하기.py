'''문제 2. 하늘에서 떨어지는 빗방울 피하기 (Rain Drop)
목표: 플레이어는 바닥에서 좌우로만 움직일 수 있고, 위에서 끊임없이 떨어지는 사각형(비)을 피해야 합니다.

빗방울은 리스트로 관리하며 계속 생성됩니다.

빗방울이 바닥에 닿으면 리스트에서 제거합니다(메모리 관리).

플레이어와 빗방울이 충돌하면 게임 오버.

학습 포인트:

리스트를 활용한 다중 객체 생성 및 삭제.

객체의 Y축 이동 구현 (중력 효과 흉내).

화면 밖으로 나간 객체 처리(remove).



핵심 변경 사항:

버튼 영역(Rect) 정의: 재시작 버튼과 종료 버튼의 위치와 크기를 미리 변수로 만들어둡니다.

마우스 클릭 감지: game_over 상태일 때 마우스를 클릭하면, 클릭한 위치가 버튼 위인지 확인(collidepoint)합니다.

게임 초기화 함수: 재시작 버튼을 누르면 점수, 시간, 플레이어 위치, 빗방울 리스트를 모두 초기 상태로 되돌립니다.'''


import pygame
import random
import sys

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("빗방울 피하기 (버튼 추가 버전)")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)       # 일반 글꼴
btn_font = pygame.font.SysFont(None, 40)   # 버튼용 큰 글꼴

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# ------------------ 버튼 정의 (위치와 크기) ------------------
# 화면 중앙 하단에 배치
restart_btn = pygame.Rect(WIDTH//2 - 110, HEIGHT//2 + 50, 100, 50) # 왼쪽 버튼
quit_btn = pygame.Rect(WIDTH//2 + 10, HEIGHT//2 + 50, 100, 50)    # 오른쪽 버튼

# 게임 변수 초기화 함수 (재시작 시 사용)
def reset_game():
    global player, rains, spawn_timer, start_ticks, elapsed_time, game_over
    player = pygame.Rect(280, 350, 40, 40)  # 플레이어 위치 복구
    rains = []                              # 빗방울 비우기
    spawn_timer = 0
    start_ticks = pygame.time.get_ticks()   # 시간 초기화 (현재 시간으로 재설정)
    elapsed_time = 0
    game_over = False

# 초기 변수 설정
player = None
rains = []
spawn_timer = 0
start_ticks = 0
elapsed_time = 0
game_over = False

# 게임 시작 전 초기화 한 번 실행
reset_game()

running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 마우스 클릭 이벤트 (게임 오버 상태일 때만 체크)
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            mouse_pos = event.pos # 클릭한 위치 (x, y)
            
            # 1. 재시작 버튼 클릭 시
            if restart_btn.collidepoint(mouse_pos):
                reset_game()
            
            # 2. 종료 버튼 클릭 시
            if quit_btn.collidepoint(mouse_pos):
                running = False

    # ------------------ 게임 로직 (살아있을 때만) ------------------
    if not game_over:
        # 시간 계산
        millis = pygame.time.get_ticks() - start_ticks
        elapsed_time = int(millis / 1000)

        # 플레이어 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5

        # 빗방울 생성
        spawn_timer += 1
        if spawn_timer > 10:
            rain_x = random.randint(0, WIDTH - 10)
            rains.append(pygame.Rect(rain_x, 0, 10, 20))
            spawn_timer = 0

        # 빗방울 이동 및 충돌
        for rain in rains[:]:
            rain.y += 5
            if rain.colliderect(player):
                game_over = True # 게임 오버 상태로 변경
            if rain.y > HEIGHT:
                rains.remove(rain)

    # ------------------ 화면 그리기 ------------------
    screen.fill((0, 0, 30)) # 배경

    # 게임 요소 그리기
    pygame.draw.rect(screen, GREEN, player)
    for rain in rains:
        pygame.draw.rect(screen, (100, 200, 255), rain)

    # UI 표시
    if not game_over:
        # 게임 중: 시간 표시
        time_text = font.render(f"Time: {elapsed_time}s", True, WHITE)
        screen.blit(time_text, (10, 10))
    else:
        # ------------------ 게임 오버 화면 ------------------
        # 1. 메시지 표시
        msg_text = font.render("GAME OVER", True, RED)
        score_text = font.render(f"Survival Time: {elapsed_time} sec", True, WHITE)
        
        screen.blit(msg_text, (WIDTH//2 - msg_text.get_width()//2, HEIGHT//2 - 50))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 20))

        # 2. 버튼 그리기 (사각형)
        pygame.draw.rect(screen, GRAY, restart_btn) # 재시작 배경
        pygame.draw.rect(screen, GRAY, quit_btn)    # 종료 배경

        # 3. 버튼 텍스트 올리기
        restart_text = btn_font.render("Restart", True, BLACK)
        quit_text = btn_font.render("Quit", True, BLACK)

        # 텍스트를 버튼 사각형의 중앙에 배치
        screen.blit(restart_text, (restart_btn.centerx - restart_text.get_width()//2, restart_btn.centery - restart_text.get_height()//2))
        screen.blit(quit_text, (quit_btn.centerx - quit_text.get_width()//2, quit_btn.centery - quit_text.get_height()//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()