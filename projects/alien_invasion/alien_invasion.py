
import pygame
from pygame.sprite import Group
from scoreboard import Scoreboard

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #play button
    play_button = Button(ai_settings, screen,'Play')

    #bg_color = (230,230,230)
    ship = Ship(ai_settings,screen)

    #for alien

    aliens = Group()

    #for bullets
    bullets = Group()
    # for alien group 
    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # instance of the stats

    stats = GameStats(ai_settings)

    #instance of the score board
    sb = Scoreboard(ai_settings,screen, stats)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats,sb, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        

run_game()






