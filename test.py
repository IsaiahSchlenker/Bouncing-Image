# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:07:16 2024

@author: bluet
"""
import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Charlie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # set up the image
        self.image = pygame.image.load("elephant.png")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        #create the corresponding rect
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 240
        
        #create the ability to move
        self.dx = 5
        self.dy = 3
        
    def update(self):
        self.rect.right += self.dx
        if self.rect.centerx >= screen.get_width():
            self.dx = -self.dx
        elif self.rect.centerx <= 0:
            self.dx = -self.dx
        self.rect.top += self.dy
        if self.rect.centery >= screen.get_height():
            self.dy = -self.dy
        elif self.rect.centery <= 0:
            self.dy = -self.dy
        
        
        # check bounds
        
        if self.rect.bottom > screen.get_height():
            self.rect.top = 0
            
def main():
    
    #set up screen
    pygame.display.set_caption("Basic sprite demo")
    background = pygame.Surface(screen.get_size())
    background.fill("blue")
    screen.blit(background, (0, 0))
    
    # instantiate charlie
    charlie = Charlie()
    allSprites = pygame.sprite.Group(charlie)
    
    # set up timing
    clock = pygame.time.Clock()
    keepGoing = True
    while(keepGoing):
        clock.tick(30)
        
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        # clear and redraw sprites
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
    pygame.quit()   

