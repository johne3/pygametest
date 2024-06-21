import pygame
import os

os.environ['SDL_VIDEODRIVER'] = 'fbcon'
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
	
#os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init();
screen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                running = False
    
    screen.fill("purple")
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()