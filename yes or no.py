import PySimpleGUI as sg
from random import randint

theme_menu = ['menu',['LightGrey1','dark','DarkGray8','random']]


def create_window(theme):

    sg.theme(theme)
    sg.set_options(font = 'Calibri 20')
    button_size = (7,5)
    layout = [
        [sg.VPush()],
        [sg.Text('Mr.Cube', right_click_menu = theme_menu,  )],
        [sg.VPush()],
        [sg.Spin(['Am i crazy', 'Am i stupid', 'Am i smart', 'Am i a nerd', 'Am i strong'], expand_x = True),sg.Button('press to ask', key = '-Press-')],
        [sg.Text('Output', key = '-Output-', right_click_menu = theme_menu)],
        [sg.VPush()]

    ]
    return sg.Window('Yes or no',layout, size = (600,250), no_titlebar = False, element_justification = 'center')

    

window = create_window('dark', )

current_num = []
full_operation = []

while True:
    event, values = window.read ()
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event == '-Press-':
        nr = randint(1,2)
        if nr == 1:
            window['-Output-'].update('Mr.Cube says Yes')
        else:
            window['-Output-'].update('Mr.Cube says No')
            
    

window.close()