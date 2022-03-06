import string
import pygame
import pygame.freetype
import pygame_gui
import random_word as rw

# inner classes
from block import Block
from interface import Interface
from Colors import Color

pygame.init()

#
limiter = 5

# fonts, I'm not sure that they should be in interface class
GAME_FONT = pygame.freetype.Font("assets/Righteous-Regular.ttf", 36)
TITLE_FONT = pygame.freetype.Font("assets/Righteous-Regular.ttf", 69)

# in-game title
title = "wordle-like game"

# window's title
pygame.display.set_caption("Wordley example")

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# if_won = true mean that game will not continue, and user can't for example continue to input letters
if_won = False
# shift for main table of blocks
shift_x = 300
shift_y = 100

# variables for game mechanic
gameround = 0  # one round contains 5 letters. There are five rounds in game
cur_position = 0  # which block should be used from 0 to 4
correct_letters = 0  # how many correct letters in correct position in word entered user
block_list = [[], [], [], [], []]  # list of game rounds
alphabet_list = list(string.ascii_lowercase)  # alphabet list to check if entered character is letter
secret_word = "peace"  # this is word, which user must guess. in get_word() this word will be redefined

interface = Interface()


def get_word():
    """method return random english word of lenght 5 characters"""
    r = rw.RandomWords()
    word = r.get_random_word(minLength=5, maxLength=5)
    print(word)
    return word


def main():
    global gameround, cur_position, secret_word, if_won

    secret_word = get_word()
    run = True
    WIN.fill(Color.WHITE.value)

    # interface settings
    interface.set_font_title(TITLE_FONT)
    interface.set_font_main(GAME_FONT)
    interface.set_screen(WIN)
    interface.draw_title(title)
    interface.set_dimension(WIDTH, HEIGHT)
    interface.draw_stats(correct_letters)

    # display window to show interface
    pygame.display.update()

    # draw game pole
    draw_rectangles()

    # create button "New Game"
    new_game_button = interface.draw_button()

    # clock is necessary to show interface button
    clock = pygame.time.Clock()
    while run:
        # necessary to show interface button
        time_delta = clock.tick(60) / 1000.0

        # keys = pygame.key.get_pressed()

        interface.manager.draw_ui(WIN)
        pygame.display.update()

        # event manager in pygame
        for event in pygame.event.get():
            # event for "New Game" button
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == new_game_button:
                    print("new game")
                    repeat_game()
            interface.manager.process_events(event)
            # event for x button of window
            if event.type == pygame.QUIT:
                run = False
            # event for pressing keyboard buttons
            if event.type == pygame.KEYDOWN:
                # print("current position is " + str(cur_position))
                if event.key == pygame.K_BACKSPACE:
                    # cur_position is responsible for active block of letter and it shouldn't be -1. only from 0 to 4
                    if cur_position > 0:
                        cur_position -= 1
                        # erase letter from active block and active previous block
                        block_list[gameround][cur_position].hide_letter()

                        pygame.display.update()
                # enter button event
                elif event.key == pygame.K_RETURN:
                    # it should work only when user entered all five letters
                    if cur_position == 5:
                        next_round()
                else:
                    # show entered letter
                    _cur_key = event.unicode

                    # position should be 0 to 4, key should be one of letter and user is not a winner
                    if cur_position < limiter and _cur_key in alphabet_list and if_won == False:
                        print(block_list)
                        # print( " " + str(gameround) + " " + str(cur_position))
                        block_list[gameround][cur_position].print_letter(GAME_FONT, _cur_key.upper())

                        cur_position += 1
                        pygame.display.update()

        interface.manager.update(time_delta)
    pygame.quit()


def draw_rectangles():
    """method draw table of free blocks of white color """
    global secret_word
    for _y in range(5):
        for _x in range(5):
            block_letter = Block()
            block_letter.secret_word = secret_word
            block_letter.set_position(shift_x + 50 * _x, shift_y + 50 * _y)
            block_letter.set_screen(WIN)
            block_letter.font = GAME_FONT
            # every letter will shown and check only in uppercase
            block_letter.set_letter(secret_word[_x].upper())
            block_letter.create_block()
            block_list[_y].append(block_letter)


def next_round():
    """after user press enter and it's not the last round, new round begins"""
    global gameround, cur_position, correct_letters, if_won
    if gameround == 4:
        # end of game
        interface.draw_answer(secret_word)
        return 0
    for x in range(5):
        # compare 2 letters and if compare_letters return true than +1 to correctly chosen letters in this round
        # correct_letters counts again every round because user can change letters every round even if they are correct
        r = block_list[gameround][x].compare_letters()
        if r:
            correct_letters += 1
    # print(correct_letters)
    if correct_letters == 5:
        # user won
        if_won = True
        interface.draw_answer(secret_word)
    gameround += 1
    cur_position = 0  # cur position should be 0 to begin new letters entering from beginning of row
    interface.draw_stats(correct_letters)  # update stats 0/5 - 5/5
    correct_letters = 0  # as I wrote before every round correct_letters resets to zero


def repeat_game():
    """new game mechanic"""
    global secret_word, gameround, cur_position, correct_letters, title
    WIN.fill(Color.WHITE.value)
    secret_word = get_word()
    interface.draw_title(title)
    interface.draw_stats(correct_letters)
    pygame.display.update()
    for _y in range(5):
        block_list[_y].clear()

    draw_rectangles()
    gameround = 0
    cur_position = 0
    correct_letters = 0

    print(block_list)


if __name__ == '__main__':
    main()
