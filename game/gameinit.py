import pygame
import sys
from game import Button
from game import morse
from game import TextBox


class Game:
    def __init__(self):
        pygame.init()
        # 初始化窗口大小
        self.size = (self.width, self.height) = (1080, 800)
        # 初始化一些常用颜色
        self.color = Button.Color
        # 设置窗口、名称、logo、字体
        self.window = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption("永不消逝的电波")
        logo = pygame.image.load('./image/logo.jpg')
        pygame.display.set_icon(logo)
        self.font = './Fonts/SmileySans-Oblique.ttf'
        # 初始化时钟对象
        self.Clock = pygame.time.Clock()
        # 配置开始界面
        self.startPicture = pygame.image.load('./image/start.jpg')
        self.startPicture = pygame.transform.scale(self.startPicture, self.size)
        self.StartGame = Button.ButtonText("开始游戏", self.color.BLACK, self.font, 30)
        self.StartGameBackground = Button.Image('./image/link.png', 0.4)
        self.version = Button.ButtonText("Alpha 1.0", self.color.VERSION, self.font, 14)
        # 加载通用资源
        self.Background = pygame.image.load('./image/background.jpg')
        self.SettingIcon = Button.ButtonImage('./image/settingwhite.png', 0.03)
        self.backb = Button.ButtonImage('./image/backb.png', 0.4)
        self.telegraph = pygame.image.load('./image/telegraph.jpg')
        self.telegraph_button = pygame.image.load('./image/telegraph_button.jpg')
        # 加载音频文件
        pygame.mixer.init()
        pygame.mixer.music.load('./music/long.wav')
        # 加载编解码对象
        self.decode = morse.DECODE()

    def init(self):
        self.window.blit(self.startPicture, (0, 0))
        self.StartGameBackground.draw(self.window, self.width * 0.51, self.height * 0.8)
        self.StartGame.draw(self.window, self.width * 0.5, self.height * 0.8)
        self.version.draw(self.window, self.width * 0.97, self.height * 0.97)
        self.SettingIcon.draw(self.window, self.width * 0.98, self.height * 0.03)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                self.Clock.tick(60)
                if event.type == pygame.VIDEORESIZE:
                    self.size = (self.width, self.height) = event.size
                    self.startPicture = pygame.transform.scale(self.startPicture, self.size)
                    self.window.blit(self.startPicture, (0, 0))
                    self.StartGameBackground.draw(self.window, self.width * 0.51, self.height * 0.8)
                    self.StartGame.draw(self.window, self.width * 0.5, self.height * 0.8)
                    self.version.draw(self.window, self.width * 0.97, self.height * 0.97)
                    self.SettingIcon.draw(self.window, self.width * 0.98, self.height * 0.03)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.StartGame.handle_event(self.GameInterface)
                    self.version.handle_event(self.VersionLog)
                    self.SettingIcon.handle_event(self.SettingInterface)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def GameInterface(self):
        morse = []
        temp = 0
        self.telegraph = pygame.transform.scale(self.telegraph, self.size)
        self.window.blit(self.telegraph, (0, 0))
        self.backb.draw(self.window, self.width * 0.02, self.height * 0.03)
        button = pygame.image.load('./image/button.png')
        button = pygame.transform.scale(button, (self.width * 0.12, self.height * 0.084))
        self.window.blit(button, (self.width * 0.44, self.height * 0.8))
        move = 0
        site = [self.width * 0.44, self.height * 0.8]
        model = 0
        inputbox = TextBox.InputBox(pygame.Rect(self.width*0.2,self.height*0.1,self.width*0.6,self.height*0.1))
        while True:
            self.Clock.tick(60)
            for event in pygame.event.get():
                inputbox.dealEvent(event)
                if event.type == pygame.VIDEORESIZE:
                    self.size = (self.width, self.height) = event.size
                    self.telegraph = pygame.transform.scale(self.telegraph, self.size)
                    button = pygame.transform.scale(button, (self.width * 0.12, self.height * 0.084))
                    site = [self.width * 0.44, self.height * 0.8]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.backb.handle_event(self.init)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not inputbox.active:
                        morse.append(temp)
                        temp = 0
                        model = 1
                        pygame.mixer.music.rewind()
                        if site[1] == self.height * 0.8:
                            move = 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE and not inputbox.active:
                        morse.append(temp)
                        temp = 0
                        model = 2
                        pygame.mixer.stop()
                        if site[1] != self.height * 0.8:
                            move = -7
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if model == 1:
                temp += 1
            elif model == 2:
                temp -= 1
            self.window.blit(self.telegraph, (0, 0))
            self.backb.draw(self.window, self.width * 0.02, self.height * 0.03)
            inputbox.draw(self.window)
            if move > 0:
                move -= 1
                site[1] += self.height * 0.01
            elif move < 0:
                move += 1
                site[1] -= self.height * 0.01
            self.window.blit(button, site)
            BaseRect = ((self.width * 0.45, self.height * 0.85), (self.width * 0.42, self.height * 0.92),
                        (self.width * 0.58, self.height * 0.92), (self.width * 0.55, self.height * 0.85))
            buttonBase = pygame.draw.polygon(self.window, self.color.BLACK, BaseRect)
            if site[1] < self.height * 0.81:
                site[1] = self.height * 0.8
            if temp == 1:
                pygame.mixer.music.play()
            elif temp < -100:
                res = self.decode.process(*morse)
                print(res)
                inputbox.text = res
                temp = 0
                model = 0
            pygame.display.update()

    def VersionLog(self):
        while True:
            self.Clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.window.blit(self.Background, (0, 0))
            pygame.display.update()

    def SettingInterface(self):
        while True:
            self.Clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.window.blit(self.Background, (0, 0))
            pygame.display.update()
