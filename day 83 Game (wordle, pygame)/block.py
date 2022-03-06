import pygame
from Colors import Color


class Block:
    x = 50
    y = 50
    # shift for letters to align them to center of block
    shift_x = 10
    shift_y = 7

    screen = None
    letter = None
    secret_word = None
    entered_letter = None
    font = None

    # colors that are using in wordle game.
    curent_color = Color.YELLOW.value

    def create_block(self):
        """method draws a block"""
        pygame.draw.rect(self.screen, Color.BORDER_GREY.value, pygame.Rect(self.x, self.y, 40, 40), 2)
        pygame.display.update()

    def set_screen(self, _screen):
        """method defines a surface which will be used for drawing block"""
        self.screen = _screen

    def set_position(self, _x, _y):
        """method set position of block"""
        self.x = _x
        self.y = _y

    def change_color(self, _color):
        """changing a color after compare in compare_letters() method"""
        pygame.draw.rect(self.screen, _color, pygame.Rect(self.x, self.y, 40, 40))
        pygame.display.update()

    def set_letter(self, _letter):
        """method set correct letter from word into this block"""
        self.letter = _letter

    def print_letter(self, _font, _key):
        """method shows the letter entered by user"""
        self.entered_letter = _key
        text_surface, rect = _font.render(_key, (0, 0, 0))
        self.screen.blit(text_surface, (self.x + self.shift_x, self.y + self.shift_y))

    def hide_letter(self):
        """method erase letter from cell"""
        print("hide letter for " + self.letter)
        # redraw part of screen into white color.
        self.screen.fill(pygame.Color(Color.WHITE.value), (self.x, self.y, 40, 40))
        self.create_block()

    def compare_letters(self):
        """method compare two letters and change the color of cell according rules of wordle"""
        # self.hide_letter()
        # if _hit true - user chose the right letter.
        _hit = False
        print(self.secret_word + " " + self.letter + " " + self.entered_letter)
        # 1 case. User correct chose letter and its position in word.
        if self.letter == self.entered_letter:
            self.change_color(Color.GREEN.value)
            print("change color to white for " + self.letter)
            _hit = True
        # 2 case. User chose correct letter but the position is incorrect.
        elif self.secret_word.upper().find(self.entered_letter) > 0:
            self.change_color(Color.YELLOW.value)
        else:
            # other cases
            self.change_color(Color.GREY.value)
        # print("redraw letter for " + self.letter)

        # after filling with color, it's necessary to draw the entered letter again.
        self.print_letter(self.font, self.entered_letter)
        # last thing - update display otherwise all changes will be not shown.
        pygame.display.update()
        return _hit
