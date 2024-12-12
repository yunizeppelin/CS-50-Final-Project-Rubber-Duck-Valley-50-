import pygame
import random
from timer import Timer
from score import Score
from ammo import Ammo
from duck import Duck
from special_duck import Special_duck
from weapon import Weapon
from scorex2 import Scorex2

# Game mode
mode = ""
# State
state = "menu"

# Define Button object
class Button:
    # Load images
    def __init__(self, image, image2, x, y):
        self.image = image
        self.image2 = image2
        self.area = self.image.get_rect()
        self.area.topleft = (x, y)
        self.index = self.image

    # Render on screen
    def draw(self, screen):
        screen.blit(self.index, self.area)

    # Hover animation
    def hover(self, mouseX, mouseY):
        if self.area.collidepoint(mouseX, mouseY):
            self.index = self.image2
        else:
            self.index = self.image

    # Click
    def click(self, mouseX, mouseY, type):
        if self.area.collidepoint(mouseX, mouseY):
            global mode
            global state
            mode = type
            state = "game"

# Load pygame
pygame.init()

# Set resolution
screen = pygame.display.set_mode((640, 480))

# Set window name
pygame.display.set_caption("Rubber Duck Valley 50")

# Load background
background = pygame.image.load("background.png")
background_area = background.get_rect()
background_area.topleft = (0, 0)

# Load sprites
easyButton = Button(pygame.image.load("easy.png"), pygame.image.load("easy_hover.png"), 256, 120)
normalButton = Button(pygame.image.load("normal.png"), pygame.image.load("normal_hover.png"), 256, 170)
proButton = Button(pygame.image.load("pro.png"), pygame.image.load("pro_hover.png"), 256, 220)
insaneButton = Button(pygame.image.load("insane.png"), pygame.image.load("insane_hover.png"), 256, 270)

# Load crosshair
crosshair = pygame.image.load("crosshair.png")
crosshair_area = crosshair.get_rect()
crosshair_area.topleft = (64, 64)

# Initialize mixer
pygame.mixer.init()

# Load theme song
pygame.mixer.music.load("duck50_theme.mp3")

# Play theme song
pygame.mixer.music.play(loops=-1)

# Load weapon sound
fire = pygame.mixer.Sound("fire.mp3")

# Load timer
timer = Timer()

# Prepare score
score = None

# Prepare ammo
ammo = None

# Prepare ducks
duck = None

# Prepare weapn
weapon = None

# Prepare special duck
special_duck = None

# Prepare Score x2
scorex2 = None

quit = False
# Game loop
while not quit:

    # Get cursor position
    mouseX, mouseY = pygame.mouse.get_pos()

    # Menu state
    if state == "menu":
        # Hover mouse animation
        easyButton.hover(mouseX, mouseY)
        normalButton.hover(mouseX, mouseY)
        proButton.hover(mouseX, mouseY)
        insaneButton.hover(mouseX, mouseY)

        # Draw background
        screen.blit(background, background_area)

        # Draw text
        screen.blit(pygame.font.Font(None, 48).render(f"Rubber Duck Valley 50", True, (255, 0, 0)), (128, 48))
        screen.blit(pygame.font.Font(None, 24).render(f"Developed by Jirapas Unison Jipipob", True, (255, 255, 255)), (128, 92))

        # Draw buttons
        easyButton.draw(screen)
        normalButton.draw(screen)
        proButton.draw(screen)
        insaneButton.draw(screen)

        for event in pygame.event.get():
            # Check if the game is quiting
            if event.type == pygame.QUIT:
                quit = True
            # Check if user click on button
            if event.type == pygame.MOUSEBUTTONDOWN:
                easyButton.click(mouseX, mouseY, "Easy")
                normalButton.click(mouseX, mouseY, "Normal")
                proButton.click(mouseX, mouseY, "Pro")
                insaneButton.click(mouseX, mouseY, "Insane")
                print("Mode:",mode)
                # Set timer
                if mode == "Easy":
                    timer.set(60)
                elif mode == "Normal":
                    timer.set(50)
                elif mode == "Pro":
                    timer.set(40)
                elif mode == "Insane":
                    timer.set(30)
    # Game state
    elif state == "game":
        # Hide mouse
        pygame.mouse.set_visible(False)
        # Draw background
        screen.blit(background, background_area)
        # Spawn duck
        if duck == None:
            duck = Duck(random.randint(0, 576), random.randint(0, 256))
        duck.draw(screen)
        # Spawn special duck
        if special_duck == None:
            special_duck = Special_duck(random.randint(0, 576), random.randint(0, 256))
        special_duck.draw(screen)
        # Special duck delay respawn
        if special_duck.update():
            special_duck.start = None
        # Load weapon
        if weapon == None:
            weapon = Weapon()
        # Draw weapon
        weapon.draw(screen)
        # Update weapon
        weapon.update(mouseX, mouseY)
        # Load score
        if score == None:
            score = Score()
        # Draw score
        score.draw(screen)
        # Load ammo
        if ammo == None:
            ammo = Ammo()
        # Draw ammo
        ammo.draw(screen)
        # Update ammo
        ammo.update()
        # Draw timer
        timer.draw(screen)
        # Load Score x2
        if scorex2 == None:
            scorex2 = Scorex2()
        # Draw Score x2
        scorex2.draw(screen)
        # Draw crosshair
        crosshair_area.x = mouseX - 8
        crosshair_area.y = mouseY - 8
        screen.blit(crosshair, crosshair_area)
        # Time out
        if timer.time_out():
            state = "result"
        for event in pygame.event.get():
            # Check if the game is quiting
            if event.type == pygame.QUIT:
                quit = True
            # Chcke if user click on duck
            if event.type == pygame.MOUSEBUTTONDOWN:
                # decrease ammo
                if ammo.ammo > 0 and ammo.start == None:
                    fire.play()
                    ammo.ammo -= 1
                    if duck.click(mouseX, mouseY):
                        # Destroy duck
                        duck = None
                        if scorex2.multiplier == False:
                            # Update score by 1
                            score.update(1)
                        else:
                            # Update score by 2
                            score.update(2)
                    if special_duck.click(mouseX, mouseY) and special_duck.start == None:
                        # Destroy special duck
                        special_duck.start = pygame.time.get_ticks()
                        # Update score by 1
                        score.update(1)
                        # Activate multiplier
                        scorex2.multiplier = True
                        scorex2.start = pygame.time.get_ticks()
            # Check if user reload
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and ammo.start == None:
                    ammo.reload()
                    weapon.reload = True
        # Score x2 Time out
        if scorex2.time_out():
            scorex2 = None
    # Result state
    elif state == "result":
        # Show mouse
        pygame.mouse.set_visible(True)
        # Draw background
        screen.blit(background, background_area)
        # Draw score
        score.draw_result(screen, mode)
        for event in pygame.event.get():
            # Check if the game is quiting
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                # Press R to restart
                if event.key == pygame.K_r:
                    duck = None
                    special_duck = None
                    weapon = None
                    score = None
                    ammo = None
                    scorex2 = None
                    mode = ""
                    state = "menu"
                    # Press ESC to quit
                if event.key == pygame.K_ESCAPE:
                    quit = True
    
    # Update display
    pygame.display.flip()

    # Set 24 FPS
    pygame.time.Clock().tick(24)

# End of the program
pygame.quit()