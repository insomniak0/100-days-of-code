# -*- coding: utf-8 -*-
import PySimpleGUI as sg
# Day 81. Simple Morse code translater.
# It uses only latin characters

#dict of latin letters as keys and morse code as values.
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',
                    ' ':'.......'}

if __name__ == '__main__':

  layout_main=[[
    sg.Text("Text to encode", size=(20, 2), font=('Any 20'))],
    [sg.InputText(' ', key="textToEncode", text_color='#000000'),
    sg.Button('Encode')],
    [sg.Output(size=(50, 10))]
  ]
  window = sg.Window(title="Morse Code Encoder ", layout=layout_main, margins=(100, 50))
  while True:
      event, values = window.read()
      #close window if the X button clicked.
      if event == sg.WINDOW_CLOSED:
          break;

        #check if there are only latin symbols.
      try:
        # 1. make from string a list of characters
        # 2. strip string to remove not necessary spaces in the end of the string
        # 3. make them uppercase, because dictionary has only uppercase symbols as keys
        # 4. encode and decode string to check whether string has only latin characters
        # 5. and transrom string to list.
        textToEncode =  list(values['textToEncode'].strip().upper().encode(encoding='utf-8').decode('ascii'))
        # with list comprechencen put dict values to result string by using string characters as keys.
        # "".join transform list back to the string.
        resultString = "".join([MORSE_CODE_DICT.get(x)+'   ' for x in textToEncode])
        #erase input
        window['textToEncode'].Update('')
      # if there are non-latin characters, handle exception
      except UnicodeDecodeError:
          resultString = "There are non latin characters "


      print(resultString)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
  window.close()