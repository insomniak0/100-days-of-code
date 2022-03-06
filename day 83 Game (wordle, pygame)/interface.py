import pygame
import pygame_gui
from Colors import Color


class Interface:
    screen = None
    fontTitle = None
    fontMain = None
    WIDTH = None
    HEIGHT = None
    manager = None

    def set_dimension(self, _width, _height):
        """set dimension for interface"""
        self.WIDTH = _width
        self.HEIGHT = _height

    def set_font_title(self, _fontTitle):
        """set font for title"""
        self.fontTitle = _fontTitle

    def set_font_main(self, _fontMain):
        """set main font for supporting information"""
        self.fontMain = _fontMain

    def set_screen(self, _screen):
        """set surface for interface"""
        self.screen = _screen

    def draw_title(self, title):
        """draw title"""
        self.update_data(self.fontTitle, title, 150, 17)

    def update_data(self, _font, _string, _x, _y):
        """update data of supporting information"""
        text_surface, rect = _font.render(_string, (0, 0, 0))
        self.screen.blit(text_surface, (_x, _y))
        pygame.display.update()

    def draw_stats(self, correct_letters):
        """draw statistics of correct letter in correct position for round"""
        _string = str(correct_letters) + "/5"
        print("redraw stats " + _string)
        # erase old data
        self.screen.fill(pygame.Color(Color.WHITE.value), (680, 90, 80, 40))
        self.update_data(self.fontMain, _string, 680, 90)

    def draw_answer(self, answer):
        """answer will drown in the end of the game"""
        answer_y_shift = 40
        self.update_data(self.fontMain, "Correct answer is:", 560, 130 + answer_y_shift)
        self.update_data(self.fontMain, answer.upper(), 660, 180 + answer_y_shift)

    def draw_button(self):
        """define New game button"""
        self.manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))
        new_game_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((self.WIDTH / 2 - 80, self.HEIGHT - 120), (100, 50)),
            text='New Game',
            manager=self.manager)

        return new_game_button
