import pygame

# Duck object
class Duck:
    def __init__(self, x, y):
        self.image = pygame.image.load("duck.png")
        self.area = self.image.get_rect()
        self.area.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.area)

    def click(self, mouseX, mouseY):
        if self.area.collidepoint(mouseX, mouseY):
            return True
        else:
            return False