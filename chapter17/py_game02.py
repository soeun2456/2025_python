import pygame

pygame.init()

WIDTH, HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 2")

screen.fill((255,255,255))
pygame.display.flip()

pygame.time.delay(2000)

pygame.quit()
