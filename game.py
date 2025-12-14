import pygame
import random
import sys
import os

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("빗방울 피하기 게임")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
SKY_BLUE = (100, 200, 255)
DARK_BLUE = (0, 0, 30)

clock = pygame.time.Clock()
font = pygame.font.SysFont('malgungothic', 30)
btn_font = pygame.font.SysFont('malgungothic', 40)

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40

try:
    player_image = pygame.image.load(os.path.join('.', 'kiiroitori.png')).convert_alpha()
    player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
    use_image = True
except pygame.error:
    print("경고: 'player.png' 이미지를 로드할 수 없습니다. 사각형 플레이어를 대신 사용합니다.")
    use_image = False


RESTART_BTN_WIDTH, RESTART_BTN_HEIGHT = 120, 50
QUIT_BTN_WIDTH, QUIT_BTN_HEIGHT = 100, 50

restart_btn = pygame.Rect(WIDTH//2 - RESTART_BTN_WIDTH - 10, HEIGHT//2 + 50, RESTART_BTN_WIDTH, RESTART_BTN_HEIGHT)

quit_btn = pygame.Rect(WIDTH//2 + 10, HEIGHT//2 + 50, QUIT_BTN_WIDTH, QUIT_BTN_HEIGHT)


def reset_game():
    global player_rect, rains, spawn_counter, start_ticks, elapsed_time, game_over
    
    player_rect = pygame.Rect(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
    rains = []
    spawn_counter = 0
    start_ticks = pygame.time.get_ticks()
    elapsed_time = 0
    game_over = False

player_rect = None
rains = []
spawn_counter = 0
start_ticks = 0
elapsed_time = 0
game_over = False

reset_game()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            mouse_pos = event.pos
            
            if restart_btn.collidepoint(mouse_pos):
                reset_game()
            
            if quit_btn.collidepoint(mouse_pos):
                running = False

    if not game_over:
        millis = pygame.time.get_ticks() - start_ticks
        elapsed_time = int(millis / 1000)

        keys = pygame.key.get_pressed()
        player_speed = 6
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_speed

        spawn_counter += 1

        if spawn_counter > 20 and len(rains) < 15: 
            rain_x = random.randint(0, WIDTH - 10)
            rains.append(pygame.Rect(rain_x, 0, 10, 20))
            spawn_counter = 0

        rain_speed = 5
        for rain in rains[:]:
            rain.y += rain_speed
            
            if rain.colliderect(player_rect):
                game_over = True
            
            if rain.y > HEIGHT:
                rains.remove(rain)

    screen.fill(DARK_BLUE)

    if use_image:
        screen.blit(player_image, player_rect)
    else:
        pygame.draw.rect(screen, GREEN, player_rect)
        
    for rain in rains:
        pygame.draw.rect(screen, SKY_BLUE, rain)

    if not game_over:
        time_text = font.render(f"생존 시간: {elapsed_time}s", True, WHITE)
        screen.blit(time_text, (10, 10))
    else:
        msg_text = font.render("GAME OVER,,", True, RED)
        score_text = font.render(f"최종 기록: {elapsed_time}s", True, WHITE)

        screen.blit(msg_text, (WIDTH//2 - msg_text.get_width()//2, HEIGHT//2 - 50))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 20))

        pygame.draw.rect(screen, GRAY, restart_btn)
        pygame.draw.rect(screen, GRAY, quit_btn)

        restart_text = btn_font.render("Restart", True, BLACK)
        quit_text = btn_font.render("Quit", True, BLACK)

        screen.blit(restart_text, (restart_btn.centerx - restart_text.get_width()//2, restart_btn.centery - restart_text.get_height()//2))
        screen.blit(quit_text, (quit_btn.centerx - quit_text.get_width()//2, quit_btn.centery - quit_text.get_height()//2))

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
sys.exit()