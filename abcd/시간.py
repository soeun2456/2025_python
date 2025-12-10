import pygame

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("시간 타이머 예제")

# 프레임 설정
clock = pygame.time.Clock()

# 폰트 설정 (None은 기본 폰트, 50은 글자 크기)
font = pygame.font.SysFont(None, 50)

# 시작 시간 기록 (게임이 시작된 시점의 tick을 저장)
start_ticks = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ------------------ 시간 계산 로직 ------------------
    # 현재 시간(get_ticks)에서 시작 시간(start_ticks)을 빼면 경과 시간이 나옴 (ms 단위)
    # 이것을 1000으로 나누면 '초(second)' 단위가 됨
    elapsed_millis = pygame.time.get_ticks() - start_ticks
    elapsed_seconds = elapsed_millis / 1000
    
    # 정수로 표현하고 싶으면 int() 사용 (예: 0, 1, 2...)
    display_time = int(elapsed_seconds) 
    
    # 소수점까지 표현하고 싶으면 아래 주석 해제 (예: 1.23)
    # display_time = round(elapsed_seconds, 2)
    # ----------------------------------------------------

    # 화면 그리기
    screen.fill((255, 255, 255)) # 흰색 배경

    # 글자 렌더링 (내용, 안티앨리어싱, 색상)
    timer_text = font.render(f"Time: {display_time}", True, (0, 0, 0))
    
    # 화면 중앙 상단에 배치
    screen.blit(timer_text, (WIDTH // 2 - 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()