import pygame
import random

#기본설정
pygame.init()
GRID_SIZE = 4
CARD_SIZE = 100
PADDING = 10
screen_width = GRID_SIZE * (CARD_SIZE + PADDING) + PADDING
screen_height = GRID_SIZE * (CARD_SIZE + PADDING) + PADDING + 50 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("🂡숫자 카드 맞추기 게임!🂡")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

#색
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0) 

#초기화
def init_cards():
    """카드 값과 상태를 초기화합니다."""
    card_values = [i for i in range(1, (GRID_SIZE * GRID_SIZE) // 2 + 1)] * 2
    random.shuffle(card_values)
    
    cards = []
    for r in range(GRID_SIZE):
        row = []
        for c in range(GRID_SIZE):
            value = card_values.pop(0)
            row.append({'value': value, 'flipped': False, 'matched': False}) 
        cards.append(row)
        
    return cards


cards = init_cards()
pending_cards_pos = []
pairs_matched = 0
game_win = False
running = True

match_check_timer = 0
match_delay = 60
def draw_card(card, r, c):
    
    pos = (r, c)
    
    x = c * (CARD_SIZE + PADDING) + PADDING
    y = r * (CARD_SIZE + PADDING) + PADDING
    rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE)
    
    if card['matched']:

        pygame.draw.rect(screen, LIGHT_GRAY, rect) 
        text_color = BLACK
        border_color = BLACK
        
    elif card['flipped']:
        pygame.draw.rect(screen, WHITE, rect)
        text_color = BLUE
        border_color = RED if pos in pending_cards_pos else BLACK
        
    else:
        pygame.draw.rect(screen, BLUE, rect)
        
        if pos in pending_cards_pos:
            border_color = RED
        else:
            border_color = BLACK
        
        pygame.draw.rect(screen, border_color, rect, 3)
        return 

    text_surface = font.render(str(card['value']), True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
    
    pygame.draw.rect(screen, border_color, rect, 3) 

def handle_click(mouse_x, mouse_y):
    global pending_cards_pos, match_check_timer
    
    if match_check_timer > 0 or len(pending_cards_pos) == 2:
        return
    
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            x = c * (CARD_SIZE + PADDING) + PADDING
            y = r * (CARD_SIZE + PADDING) + PADDING
            rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE)
            
            if rect.collidepoint(mouse_x, mouse_y):
                card = cards[r][c]
                pos = (r, c)
                
                if card['matched'] or pos in pending_cards_pos:
                    return
                
                pending_cards_pos.append(pos)
                
                if len(pending_cards_pos) == 2:
                    r1, c1 = pending_cards_pos[0]
                    r2, c2 = pending_cards_pos[1]
                    cards[r1][c1]['flipped'] = True
                    cards[r2][c2]['flipped'] = True
                    
                    match_check_timer = match_delay 
                
                return 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_win:
            handle_click(event.pos[0], event.pos[1])

    if match_check_timer > 0:
        match_check_timer -= 1
        
        if match_check_timer == 0:
            r1, c1 = pending_cards_pos[0]
            r2, c2 = pending_cards_pos[1]
            card1 = cards[r1][c1]
            card2 = cards[r2][c2]
            
            if card1['value'] == card2['value']:
                card1['matched'] = True
                card2['matched'] = True

                pairs_matched += 1
                
                if pairs_matched == (GRID_SIZE * GRID_SIZE) // 2:
                    game_win = True
            else:
                card1['flipped'] = False
                card2['flipped'] = False

            pending_cards_pos = [] 

    screen.fill(LIGHT_GRAY)

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            draw_card(cards[r][c], r, c)

    if game_win:
        msg = "Congratulations! Press R to Restart"
        color = RED
    elif len(pending_cards_pos) == 1:
        msg = "Select the second card..."
        color = BLACK
    else:
        msg = f"Pairs: {pairs_matched} / 8"
        color = BLACK

    msg_surface = font.render(msg, True, color)
    screen.blit(msg_surface, (10, screen_height - 40))
    
    keys = pygame.key.get_pressed()
    if game_win and keys[pygame.K_r]:
        cards = init_cards()
        pending_cards_pos = []
        pairs_matched = 0
        game_win = False
        match_check_timer = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()