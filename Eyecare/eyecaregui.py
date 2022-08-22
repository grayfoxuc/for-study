import PySimpleGUI as sg
from eyecare import *

sg.theme('DarkAmber')

layout = [[sg.Text('Timer will show here')],
          [sg.Button('Start', key='-START-'), sg.Button('Stop', key='-STOP-')]
         ]

window = sg.Window('Eye Care', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-START-':
        start_eyecare()
    if event == '-STOP-':
        print('I clicked stop')

window.close()
