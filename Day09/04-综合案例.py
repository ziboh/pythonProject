class Game(object):
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod
    def show_help():
        print('游戏帮助')
    @classmethod
    def show_top_score(cls):
        print(f'最高分为{cls.top_score}')
    def start_game(self):
        print(f'{self.player_name}准备好了吗，即将开始游戏')

zhou = Game('周伯华')
zhou.start_game()
Game.show_top_score()
Game.show_help()
