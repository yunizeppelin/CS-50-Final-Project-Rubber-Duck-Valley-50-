import pygame

# Define Score x2 object
class Scorex2:
    def __init__(self):
        self.multiplier = False
        self.start = None
        # x2 for 5 seconds
        self.end = 5

    # Render text
    def draw(self, screen):
        if self.multiplier == True:
            screen.blit(pygame.font.Font(None, 24).render(f"Score X2", True, (255, 0, 0)), (320, 16))

    # Time out
    def time_out(self):
        if self.start != None:
            if (self.end - ((pygame.time.get_ticks() - self.start)) // 1000) <= 0:
                return True
            else:
                return False