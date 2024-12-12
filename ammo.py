import pygame

# Define ammo object
class Ammo:
    def __init__(self):
        self.ammo = 12
        self.start = None
        self.end = 1 # Reload duration

    # Render ammo
    def draw(self, screen):
        if self.ammo > 0:
            screen.blit(pygame.font.Font(None, 24).render(f"Ammo: {self.ammo}", True, (255, 255, 255)), (16, 448))
        else:
            screen.blit(pygame.font.Font(None, 24).render(f"Press R to reload", True, (255, 255, 255)), (16, 448))

    # Reload function
    def reload(self):
        self.start = pygame.time.get_ticks()

    # Update function
    def update(self):
        if self.start != None:
            if (self.end - ((pygame.time.get_ticks() - self.start) // 1000)) <= 0:
                self.ammo = 12
                self.start = None