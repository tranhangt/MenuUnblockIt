import pygame

class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.mousex, self.mousey = pygame.mouse.get_pos()

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Start"
        self.btn_play = pygame.Rect(self.game.DISPLAY_W / 2 - 50, self.game.DISPLAY_H / 2 - 70, 150, 50)
        self.btn_options = pygame.Rect(self.game.DISPLAY_W / 2 - 50, self.game.DISPLAY_H / 2 + 20, 150, 50)
        self.btn_credits = pygame.Rect(self.game.DISPLAY_W / 2 - 50, self.game.DISPLAY_H / 2 + 110, 150, 50)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_rect((255, 0, 0), self.btn_play)
            self.game.draw_rect((255, 255, 0), self.btn_options)
            self.game.draw_rect((255, 0, 255), self.btn_credits)
            self.game.draw_text("Game name", 70, self.mid_w - 70, self.mid_h - 130)
            self.blit_screen()

    def check_input(self):
        if self.btn_play.collidepoint(pygame.mouse.get_pos()):
            if self.game.click:
                print("click_play")
                self.game.playing = True
                self.run_display = False
        elif self.btn_options.collidepoint(pygame.mouse.get_pos()):
            if self.game.click:
                print("click_op")
                self.game.curr_menu = self.game.options
                self.run_display = False
        elif self.btn_credits.collidepoint(pygame.mouse.get_pos()):
            if self.game.click:
                print("click_cre")
                self.game.curr_menu = self.game.credits
                self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

        self.state = "Volume"
        self.soundx, self.soundy = self.mid_w, self.mid_h
        self.musicx, self.musicy = self.mid_w, self.mid_h + 50

        self.btn_sound = pygame.Rect(self.soundx + 70, self.soundy - 20, 30, 30)
        self.btn_music = pygame.Rect(self.musicx + 70, self.musicy - 20, 30, 30)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill((0, 0, 0))
            self.game.check_events()
            self.check_input()
            self.game.draw_text("Options", 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Sound", 40, self.soundx, self.soundy)
            self.game.draw_text("Music", 40, self.musicx, self.musicy)

            self.game.draw_rect((230, 30, 30), self.btn_music)
            self.game.draw_rect((250, 50, 50), self.btn_sound)
            self.blit_screen()

    def check_input(self):
        if self.btn_sound.collidepoint(pygame.mouse.get_pos()):
            if self.game.click:
                self.game.draw_rect((255, 0, 50), self.btn_sound)
                print("click sound")
        elif self.btn_music.collidepoint(pygame.mouse.get_pos()):
            if self.game.click:
                self.game.draw_rect((255, 0, 50), self.btn_music)
                print("click music")

        # if self.game.BACK_KEY:
        #     self.game.curr_menu = self.game.main_menu
        #     self.run_display = False
        # elif self.game.UP_KEY or self.game.DOWN_KEY:
        #     if self.state == 'Volume':
        #         self.state = 'Controls'
        #         self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
        #     elif self.state == 'Controls':
        #         self.state = 'Volume'
        #         self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        # elif self.game.START_KEY:
        #     pass


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
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Credits", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Made by Group 1", 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()