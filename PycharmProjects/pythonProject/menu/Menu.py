import pygame
from menu.Button import Button


class Menu:
    def __init__(self, game):
        self.game = game
        self.back_ground = Button(self.game, (0, 0), "wood.jpg", 0, 0)
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.offset = - 100
        self.mousex, self.mousey = pygame.mouse.get_pos()

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        self.back_ground.draw()
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Start"
        self.name = Button(game, (225, self.mid_h - 250), "name.png", 0, 0)
        self.btn_play = Button(game, (self.game.DISPLAY_W / 2 - 100, self.game.DISPLAY_H / 2 - 85), "btn_play.png", 0, 0)
        self.btn_options = Button(game, (self.game.DISPLAY_W / 2 - 100, self.game.DISPLAY_H / 2), "btn_options.png", 0, 0)
        self.btn_credits = Button(game, (self.game.DISPLAY_W / 2 - 100, self.game.DISPLAY_H / 2 + 85),
                                  "btn_credits.png", 0, 0)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.back_ground.draw()

            self.name.draw()

            self.btn_play.draw()
            self.btn_options.draw()
            self.btn_credits.draw()

            self.blit_screen()

    def check_input(self):
        if self.btn_play.check_collidepoint():
            if self.game.click:
                print("click_play")
                self.game.curr_menu = self.game.level_menu
                self.run_display = False
        elif self.btn_options.check_collidepoint():
            if self.game.click:
                print("click_op")
                self.game.curr_menu = self.game.options
                self.run_display = False
        elif self.btn_credits.check_collidepoint():
            if self.game.click:
                print("click_cre")
                self.game.curr_menu = self.game.credits
                self.run_display = False


class LevelMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.homex, self.homey = self.game.DISPLAY_W / 2, self.game.DISPLAY_H - 100
        self.levelx, self.levely = 100, 100
        self.btn_home = Button(self.game, (self.homex, self.homey), "btn_home.png", 0, 0)
        self.btn_level = Button(self.game, (self.levelx, self.levely), "level_lock.png", 0, 0)
        self.curr_level = 1

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.back_ground.draw()
            self.btn_home.draw()
            for xx in range(0, 8):
                for yy in range (0, 4):
                    if xx == 0 and yy == 0:
                        self.btn_level = Button(self.game, (self.levelx + xx * 90, self.levely + yy * 90), "btn_level.png", self.curr_level, 1)
                    else:
                        self.btn_level = Button(self.game, (self.levelx + xx * 90, self.levely + yy * 90), "level_lock.png", self.curr_level, 0)
                    self.btn_level.draw()
                    if self.btn_level.isDone == 1 and self.btn_level.check_collidepoint():
                        if self.game.click:
                            self.game.curr_menu = self.game.player_menu
                            self.run_display = False
            self.blit_screen()

    def check_input(self):
        if self.btn_home.check_collidepoint():
            if self.game.click:
                print("click home")
                self.game.curr_menu = self.game.main_menu
                self.run_display = False


class PlayerMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

        self.homex, self.homey = 75, 485

        self.btn_home = Button(self.game, (self.homex, self.homey), "btn_home.png", 0, 0)
        self.btn_reload = Button(self.game, (self.homex + 85, self.homey), "btn_reload.png", 0, 0)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.back_ground.draw()
            self.btn_home.draw()
            self.btn_reload.draw()
            self.blit_screen()

    def check_input(self):
        if self.btn_home.check_collidepoint():
            if self.game.click:
                print("click home")
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
        if self.btn_reload.check_collidepoint():
            if self.game.click:
                print("click reload")
                self.game.curr_menu = self.game.player_menu
                self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

        self.state = "Volume"
        self.soundx, self.soundy = self.mid_w - 150, self.mid_h - 30
        self.musicx, self.musicy = self.mid_w - 150, self.mid_h + 60

        self.btn_save = Button(game, (self.musicx + 35, self.musicy + 90), "btn_save.png", 0, 0)

        self.btn_txt_music = Button(game, (self.musicx, self.musicy), "btn_txt_music.png", 0, 0)
        self.btn_txt_sound = Button(game, (self.soundx, self.soundy), "btn_txt_sound.png", 0, 0)

        self.btn_sound = Button(game, (self.soundx + 220, self.soundy), "btn_unmute.png", 0, 0)
        self.btn_music = Button(game, (self.musicx + 220, self.musicy), "btn_music.png", 0, 0)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill((0, 0, 0))
            self.game.check_events()
            self.check_input()
            self.game.draw_text("Options", 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)

            self.back_ground.draw()

            self.btn_txt_sound.draw()
            self.btn_txt_music.draw()

            self.btn_save.draw()

            self.btn_sound.draw()
            self.btn_music.draw()
            self.blit_screen()

    def check_input(self):
        if self.btn_sound.check_collidepoint():
            if self.game.click:
                if self.btn_sound.btn_id == 0:
                    self.btn_sound = Button(self.game, (self.soundx + 220, self.soundy), "btn_mute.png", 1, 0)
                else:
                    self.btn_sound = Button(self.game, (self.soundx + 220, self.soundy), "btn_unmute.png", 0, 0)
                print("click sound")
        elif self.btn_music.check_collidepoint():
            if self.game.click:
                if self.btn_music.btn_id == 0:
                    self.btn_music = Button(self.game, (self.musicx + 220, self.musicy), "btn_unmusic.png", 1, 0)
                else:
                    self.btn_music = Button(self.game, (self.musicx + 220, self.musicy), "btn_music.png", 0, 0)
                print("click music")
        elif self.btn_save.check_collidepoint():
            if self.game.click:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.back_ground.draw()

            self.game.draw_text("Credits", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Made by Group 1", 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()


