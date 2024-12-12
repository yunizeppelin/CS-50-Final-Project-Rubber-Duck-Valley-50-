import pygame

# Define score object
class Score:
    def __init__(self):
        self.score = 0

    # Update function
    def update(self, point):
        self.score += point

    # Render in-game score
    def draw(self, screen):
        screen.blit(pygame.font.Font(None, 24).render(f"Score: {self.score}", True, (255, 255, 255)), (528, 16))

    # Render result
    def draw_result(self, screen, mode):
        screen.blit(pygame.font.Font(None, 24).render(f"Mode: {mode}", True, (255, 255, 255)), (288, 160))
        screen.blit(pygame.font.Font(None, 24).render(f"Score: {self.score}", True, (255, 255, 255)), (288, 192))
        screen.blit(pygame.font.Font(None, 24).render(f"Well played!", True, (255, 255, 255)), (288, 224))
        screen.blit(pygame.font.Font(None, 24).render(f"Press R to restart", True, (255, 0, 0)), (288, 256))
        screen.blit(pygame.font.Font(None, 24).render(f"Press ESC to quit", True, (255, 0, 0)), (288, 288))