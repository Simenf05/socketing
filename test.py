from re import T
import pygame
import time
pygame.init()

import screen
import startScreen
import textBox
import layout

items = {
"txt": textBox.TextBox(10, 10, "hei", "red", pygame.font.Font(None, 20)),
"TXT2": textBox.TextBox(20, 20, "kuk", "blue"),
"TXT3": textBox.TextBox(100, 129, "afafa", (100, 100, 100))
}

lolist = []

for i in range(1, len(items) + 1):
    lolist.append((list(items)[i - 1], (i, 1)))

lo = layout.Layout((10,1), lolist)

start = startScreen.StartScreen(items, lo)


screenobj = screen.Screen((500, 500))


screenobj.addScreen(("start", start), True)

run = True

while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    
    pressed = pygame.key.get_pressed()

    screenobj.keypressReg(pressed)
    
    screenobj.updateScreen()
    
time.sleep(10)
