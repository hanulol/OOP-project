import pygame
import sys

from player import Player
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two-Player Shooting Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
BLUE = (50, 100, 220)
RED = (220, 50, 50)

# Fonts
title_font = pygame.font.SysFont(None, 64)
big_font = pygame.font.SysFont(None, 48)
normal_font = pygame.font.SysFont(None, 30)
small_font = pygame.font.SysFont(None, 24)


def draw_text(text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)

    screen.blit(text_surface, text_rect)


def create_players():
    player1_controls = {
        "up": pygame.K_w,
        "down": pygame.K_s,
        "left": pygame.K_a,
        "right": pygame.K_d,
        "shoot": pygame.K_f,
    }

    player2_controls = {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "shoot": pygame.K_SLASH,
    }

    player1 = Player(100, 260, BLUE, player1_controls, 1)
    player2 = Player(750, 260, RED, player2_controls, -1)

    return player1, player2


def draw_instruction_page():
    screen.fill(WHITE)

    draw_text("Two-Player Shooting Game", title_font, BLACK, SCREEN_WIDTH // 2, 90, True)

    draw_text("Goal:", big_font, BLACK, 100, 170)
    draw_text("Reduce the other player's HP to 0.", normal_font, BLACK, 100, 215)

    draw_text("Player 1", normal_font, BLUE, 100, 290)
    draw_text("Move: W, A, S, D", small_font, BLACK, 120, 330)
    draw_text("Shoot: F", small_font, BLACK, 120, 360)

    draw_text("Player 2", normal_font, RED, 520, 290)
    draw_text("Move: Arrow keys", small_font, BLACK, 540, 330)
    draw_text("Shoot: / key", small_font, BLACK, 540, 360)

    draw_text("Press SPACE to start", big_font, BLACK, SCREEN_WIDTH // 2, 500, True)


def draw_game_page(player1, player2, bullets):
    """Draw the main game page."""
    screen.fill(GRAY)

    pygame.draw.line(
        screen,
        BLACK,
        (SCREEN_WIDTH // 2, 0),
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT),
        3,
    )

    player1.draw(screen)
    player2.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    draw_text("Player 1 HP: " + str(player1.hp), normal_font, BLUE, 30, 20)
    draw_text("Player 2 HP: " + str(player2.hp), normal_font, RED, SCREEN_WIDTH - 200, 20)


def draw_game_over_page(winner):
    screen.fill(WHITE)

    draw_text("Game Over", title_font, BLACK, SCREEN_WIDTH // 2, 160, True)
    draw_text(winner + " wins!", big_font, BLACK, SCREEN_WIDTH // 2, 260, True)

    draw_text("Press R to restart", normal_font, BLACK, SCREEN_WIDTH // 2, 360, True)
    draw_text("Press ESC to quit", normal_font, BLACK, SCREEN_WIDTH // 2, 400, True)


def update_game(player1, player2, bullets):
    """Update players, bullets, collisions, and winner."""
    keys = pygame.key.get_pressed()

    player1.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
    player2.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)

    player1.update_cooldown()
    player2.update_cooldown()

    for bullet in bullets:
        bullet.move()

    for bullet in bullets[:]:
        if bullet.direction == 1 and bullet.get_rect().colliderect(player2.get_rect()):
            player2.take_damage(bullet.damage)
            bullets.remove(bullet)

        elif bullet.direction == -1 and bullet.get_rect().colliderect(player1.get_rect()):
            player1.take_damage(bullet.damage)
            bullets.remove(bullet)

        elif bullet.is_off_screen(SCREEN_WIDTH):
            bullets.remove(bullet)

    if player1.hp <= 0:
        return "Player 2"

    if player2.hp <= 0:
        return "Player 1"

    return None



player1, player2 = create_players()
bullets = []
winner = None

game_state = "instructions"
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_state == "instructions":
                if event.key == pygame.K_SPACE:
                    game_state = "playing"

            elif game_state == "playing":
                if event.key == player1.controls["shoot"] and player1.can_shoot():
                    bullets.append(player1.shoot())

                if event.key == player2.controls["shoot"] and player2.can_shoot():
                    bullets.append(player2.shoot())

            elif game_state == "game_over":
                if event.key == pygame.K_r:
                    player1, player2 = create_players()
                    bullets = []
                    winner = None
                    game_state = "instructions"

                if event.key == pygame.K_ESCAPE:
                    running = False

    if game_state == "playing":
        winner = update_game(player1, player2, bullets)

        if winner is not None:
            game_state = "game_over"

    if game_state == "instructions":
        draw_instruction_page()

    elif game_state == "playing":
        draw_game_page(player1, player2, bullets)

    elif game_state == "game_over":
        draw_game_over_page(winner)

    pygame.display.flip()

pygame.quit()
sys.exit()

