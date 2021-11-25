import pygame


class MenuLoader:
    BTN_LOADER = {}

    def __init__(self):
        self.BTN_LOADER["spr_play"] = pygame.image.load("image/play.png")


class Button:
    def __init__(self, game, position, img, btn_id, isDone):
        self.pos = list(position)

        self.img = pygame.image.load("image/" + img)
        self.img_rect = self.img.get_rect()
        self.img_rect.topleft = position
        self.btn_id = btn_id
        self.game = game
        self.isDone = isDone

    def draw(self):
        self.game.display.blit(self.img, self.pos)

    def check_collidepoint(self):
        if self.img_rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

