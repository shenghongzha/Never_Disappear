import pygame
from game.morse import ENCODE

class InputBox:
    def __init__(self, rect: pygame.Rect = pygame.Rect(100, 100, 140, 32)) -> None:
        """
        rect，传入矩形实体，传达输入框的位置和大小
        """

        self.boxBody: pygame.Rect = rect
        self.color_inactive = pygame.Color((255,255,0))  # 未被选中的颜色
        self.color_active = pygame.Color((255,0,0,))  # 被选中的颜色
        self.color = self.color_inactive  # 当前颜色，初始为未激活颜色
        self.active = False
        self.text = '' # 输入的内容
        self.done = False
        self.font = pygame.font.Font('./Fonts/SmileySans-Oblique.ttf',32)

    def dealEvent(self, event: pygame.event.Event):
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(self.boxBody.collidepoint(event.pos)):  # 若按下鼠标且位置在文本框
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if(
                self.active) else self.color_inactive
        if(event.type == pygame.KEYDOWN):  # 键盘输入响应
            if(self.active):
                if(event.key == pygame.K_RETURN):
                    '''在键盘输入的同时，self.text的值也在随之改变，其实并不需要通过按回车来记录值'''
                    self.translater = ENCODE(self.text)
                    self.translater.encode()
                    print(self.text)
                    self.text=''
                elif(event.key == pygame.K_BACKSPACE):
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen: pygame.surface.Surface):
        txtSurface = self.font.render(
            self.text, True, self.color)  # 文字转换为图片
# '''注意，输入框的宽度实际是由这里max函数里的第一个参数决定的，改这里才有用'''
        width = max(self.boxBody.width, txtSurface.get_width()+10)  # 当文字过长时，延长文本框
        self.boxBody.w = width
        screen.blit(txtSurface, (self.boxBody.x+5, self.boxBody.y+5))
        pygame.draw.rect(screen, self.color, self.boxBody, 2)




