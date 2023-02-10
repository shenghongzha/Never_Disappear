from game.gameinit import Game

# text = font.render("我的第一个游戏！", True, (255, 0, 0), (0, 0, 0))
# textRect = text.get_rect()
# textRect.center = (200, 200)
# window.blit(text, textRect)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    game = Game()
    game.init()