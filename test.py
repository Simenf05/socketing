import pygame
pygame.init()

import game.window as window
import game.menu as menu
import game.map as map
import game.layout.text.textBox as textBox
import game.layout.text.inputBox as inputBox
import game.layout.button.nextScreenBtn as nextScreenBtn
import game.layout.layout as layout
from consts import *

SIZE = 600

screenobj = window.Window((SIZE, SIZE))

items = {
"overskrift": textBox.TextBox(SIZE / 2, 100, "HISTORIEN OM JON", RED, BIGFONT),
"ip": textBox.TextBox(SIZE / 2, 150, "skriv inn ip her", RED, NORMALFONT),
"ipInput": inputBox.InputBox(SIZE / 2 - 150, 200, 300, 40, fontSize=40),
"navn": textBox.TextBox(SIZE / 2, 300, "skriv inn navn her", RED, NORMALFONT),
"navnInput": inputBox.InputBox(SIZE / 2 - 150, 400, 300, 40, fontSize=40),
"button": nextScreenBtn.NextScreen(SIZE / 2 - 100, 500, 200, 40, screenobj, "sub", "press ENTER")
}

main1 = {
    "overskrift": textBox.TextBox(SIZE / 2, 100, "HISTORIEN OM JON", RED, BIGFONT)
}

main2 = {
    ("overskrift", main1["overskrift"], (1, 1))
}

sub = layout.Layout((2, 1), main2)
mianscreen = map.MainScreen(main1, sub)

lay1 = [
    ("ipInput", items["ipInput"], (1, 1)),
    ("navnInput", items["navnInput"], (2, 1))
    
]

lo = layout.Layout((3,1), lay1)

start = menu.StartScreen(items, lo)


start.layout.setValue(items["button"], (3, 1))
start.addDraw(("button", items["button"]))

screenobj.addScreen(("start", start), True)
screenobj.addScreen(("sub", mianscreen))

run = True

while run:
    
    pressed = pygame.key.get_pressed()

    screenobj.keypressReg(pressed)
    
    screenobj.updateScreen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    

