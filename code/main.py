import pygame, sys
from settings import *
from fps import FPS
from level import Level


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        # screen resolution

        self.raw_w, self.raw_h = 640, 360
        # self.screen = pygame.display.set_mode(RES_LIST[RES_INDEX], pygame.RESIZABLE)
        self.screen = pygame.display.set_mode(RES_LIST[RES_INDEX])
        self.display = pygame.Surface((self.raw_w, self.raw_h)).convert_alpha()

        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        pygame.display.set_caption('Zelda')

        # self.clock = pygame.time.Clock()
        self.fps = FPS(self.font)
        self.level = Level(self.display)

    def draw_menu(self, text, offset, menu_offset=MENU_OFFSET):
        x, y = self.screen.get_size()
        MENU_LEFT = int(x / 2) - 10
        text_menu = self.font.render(text, False, TEXT_COLOR)
        btn_menu = pygame.draw.rect(self.screen, 'black',
                                    [MENU_LEFT, MENU_TOP + menu_offset * offset, MENU_WIDTH, MENU_HEIGHT], 3)
        text_rect = text_menu.get_rect(topleft=(MENU_LEFT, 100 + menu_offset * offset))
        self.screen.blit(text_menu, text_rect)
        return text_menu, btn_menu

    def draw_text(self, text, offset, menu_offset=MENU_OFFSET):
        x, y = self.screen.get_size()
        MENU_LEFT = int(x / 2) - 10
        text_menu = self.font.render(text, False, TEXT_COLOR)
        btn_menu = pygame.draw.rect(self.screen, 'black',
                                    [MENU_LEFT, MENU_TOP + menu_offset * offset, MENU_WIDTH, MENU_HEIGHT], 3)
        text_rect = text_menu.get_rect(topleft=(MENU_LEFT, 100 + menu_offset * offset))
        self.screen.blit(text_menu, text_rect)
        return text_menu, btn_menu

    def start_menu(self):
        text_start_game_menu, btn_start_game_menu = self.draw_menu("New Game", 0)
        text_continue_game_menu, btn_continue_game_menu = self.draw_menu("Continue", 1)
        text_options_menu, btn_options_menu = self.draw_menu("Options", 2)
        text_credit_menu, btn_credit_menu = self.draw_menu("Credit", 3)
        text_quit_menu, btn_quit_menu = self.draw_menu("Quit", 4)
        btn_dict = {
            "new_game": btn_start_game_menu,
            "continue_game": btn_continue_game_menu,
            "options": btn_options_menu,
            "credit": btn_credit_menu,
            "quit": btn_quit_menu,
        }
        return btn_dict

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.display.fill('grey')
            self.level.run()

            self.screen.blit(pygame.transform.scale(self.display, RES_LIST[RES_INDEX]), (0, 0))
            if IS_SHOW_FPS:
                self.fps.render(self.screen)
            pygame.display.update()

            self.fps.clock.tick(60)

    def options(self):
        self.screen.fill('black')
        while True:
            _, _ = self.draw_menu("Options", 0)
            _, btn_large_resolution = self.draw_menu("1920x1080", 1, menu_offset=50)
            _, btn_medium_resolution = self.draw_menu("1600x900", 2, menu_offset=50)
            _, btn_small_resolution = self.draw_menu("1280x720", 3, menu_offset=50)
            _, btn_back_resolution = self.draw_menu("BACK", 3)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_large_resolution.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        self.screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
                    if btn_medium_resolution.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        self.screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
                    if btn_small_resolution.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                    if btn_back_resolution.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        return

            pygame.display.flip()

    def credit(self):
        pass

    def run(self):
        game_over = False

        while not game_over:
            self.screen.fill('black')

            btn_dict = self.start_menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for btn_name, btn in btn_dict.items():
                        if btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                            if btn_name == "new_game":
                                self.play()
                                print("new game pressed")

                            if btn_name == "new_game":
                                self.play()
                                print("new game pressed")

                            if btn_name == "options":
                                self.options()
                                print("options pressed")

                            if btn_name == "credit":
                                self.credit()
                                print("credit pressed")

                            if btn_name == "quit":
                                print("quit pressed")
                                pygame.quit()
                                sys.exit()

            if IS_SHOW_FPS:
                self.fps.render(self.screen)

            pygame.display.flip()
            self.fps.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
