import pygame
import time
pygame.init()

import game.layout.componentFormat as componentFormat

keyboard = [
    pygame.K_a,
    pygame.K_b,
    pygame.K_c,
    pygame.K_d,
    pygame.K_e,
    pygame.K_f,
    pygame.K_g,
    pygame.K_h,
    pygame.K_i,
    pygame.K_j,
    pygame.K_k,
    pygame.K_l,
    pygame.K_m,
    pygame.K_n,
    pygame.K_o,
    pygame.K_p,
    pygame.K_q,
    pygame.K_r,
    pygame.K_s,
    pygame.K_t,
    pygame.K_u,
    pygame.K_v,
    pygame.K_w,
    pygame.K_x,
    pygame.K_y,
    pygame.K_z,
    pygame.K_0,
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
    pygame.K_SPACE,
    pygame.K_PERIOD
]


class InputBox(componentFormat.ComponentFormat):
    
    def __init__(self, x: int, y: int, w: int, h: int, text: str="", color_: str | tuple= "white", bgcolor_: str | tuple= "black", fontSize: int = 32, timeDiff: float=.2, backspaceTimeDiff: float=.1, width: int=2) -> None:
        
        super().__init__(x, y)
        
        self.fontSize = fontSize 
        self.font = pygame.font.Font(None, self.fontSize)
        
        self.color = color_
        self.bgcolor = bgcolor_
        
        self.size = (w, h)
        self.text = text
        self.selectLine = False
        self.width = width
        
        
        self.lineTime = round(time.time())
        self.nowTime = time.time()
        self.timeDiff = timeDiff
        self.backspaceDiff = backspaceTimeDiff
        self.lastTime = {}
        self.backspaceLastTime = self.nowTime
        
        for key in keyboard:
            self.lastTime.update({pygame.key.name(key): self.nowTime})
        
        self.refresh()
        
    def get_drawinfo(self):
        self.lineTime = round(time.time())
        self.visualRefresh()
        return self.surface, self.coords
    
    
    def visualRefresh(self):
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        
        self.textSurface = self.font.render(self.text, True, self.color, self.bgcolor)
        textRect = self.textSurface.get_rect()
        
        if self.selectLine:
            if self.lineTime % 2 == 0:
                pygame.draw.line(self.surface, self.color, (textRect.x + textRect.w + (self.width * 2), textRect.y + self.width), (textRect.x + textRect.w + (self.width * 2), textRect.x + textRect.h - self.width))
            
        self.surface.blit(self.textSurface, (self.width, self.width))
        pygame.draw.rect(self.surface, self.color, self.rect, width=self.width)
    
    
    def refresh(self):
        self.nowTime = time.time()
        
        if self.text:
            while not self.size[1] - ((self.width + 1) * 2) >= self.font.get_height():
                self.fontSize -= 1
                self.font = pygame.font.Font(None, self.fontSize)
        
        self.visualRefresh()
    
    
    def getText(self) -> str:
        return str(self.text)
    
    def changeText(self, newText: str):
        self.text = newText
        self.refresh()
    
    def action(self, **kwargs):
        self.nowTime = time.time()
        
        if kwargs["pressed"][pygame.K_BACKSPACE]:
            if (self.nowTime - self.backspaceLastTime > self.backspaceDiff):
                self.changeText(self.text[:-1])
                self.backspaceLastTime = self.nowTime
        
        for key in keyboard:
            if kwargs["pressed"][key]:
                if (self.nowTime - self.lastTime[pygame.key.name(key)] > self.timeDiff):
                    if pygame.key.name(key) == "space":
                        self.changeText(self.text + " ")
                    else:
                        if kwargs["pressed"][pygame.K_LSHIFT] or kwargs["pressed"][pygame.K_RSHIFT]:
                            self.changeText(self.text + pygame.key.name(key).capitalize())
                        
                        else:
                            self.changeText(self.text + pygame.key.name(key))
                    self.lastTime[pygame.key.name(key)] = self.nowTime
                    
    def selected(self):
        self.width += 1
        self.selectLine = True
        
    def deselected(self):
        self.width -= 1
        self.selectLine = False
        
    def __str__(self) -> str:
        return str(self.text)
    