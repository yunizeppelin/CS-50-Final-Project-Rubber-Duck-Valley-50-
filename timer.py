import pygame

# Define timer object
class Timer:
    def __init__(self):
        self.start = None
        self.end = None

    def set(self, time):
        self.start = pygame.time.get_ticks()
        self.end = time

    def time(self):
        return (pygame.time.get_ticks() - self.start) // 1000

    def draw(self, screen):
        screen.blit(pygame.font.Font(None, 24).render(f"Timer: {self.end - self.time()} seconds", True, (255, 255, 255)), (16, 16))

    def time_out(self):
        if (self.end - self.time()) <= 0:
            return True
        else:
            return False