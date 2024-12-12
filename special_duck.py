import pygame

# Special Duck object
class Special_duck:
    def __init__(self, x, y):
        self.image = pygame.image.load("special_duck.png")
        self.area = self.image.get_rect()
        self.area.topleft = (x, y)
        self.start = None
        # 11 seconds respawn delay
        self.end = 11

    def update(self):
        # Delay respawn
        if self.start != None:
            if (self.end - ((pygame.time.get_ticks() - self.start)) // 1000) <= 0:
                return True
            else:
                return False

    def draw(self, screen):
        if self.start == None:
            screen.blit(self.image, self.area)

    def click(self, mouseX, mouseY):
        if self.area.collidepoint(mouseX, mouseY):
            return True
        else:
            return False