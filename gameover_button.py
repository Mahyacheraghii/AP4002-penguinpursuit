import pygame

class EndButton:
    def __init__(self, pp_game, msg):
        self.screen = pp_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 250
        self.height = 80
        self.button_color = (160, 50, 100)

        self.txt_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 50)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.txt_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)