import pygame

# Weapon object
class Weapon():
    # Load images
    def __init__(self):
        self.sequence = []
        for i in range(24):
            self.sequence.append(pygame.image.load(f"weapon/{i}.png"))
        self.index = 0
        self.area = self.sequence[0].get_rect()
        self.area.topleft = (0, 0)
        self.reload = False

    # Update
    def update(self, x, y):
        if self.reload == True:
            self.index += 1
        if self.index == 23:
            self.index = 0
            self.reload = False
        self.area.x = x / 4
        self.area.y = y / 4

    # Render on screen
    def draw(self, screen):
        screen.blit(self.sequence[self.index], self.area)