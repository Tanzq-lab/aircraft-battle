import os
import pygame

"""  

      这个包保存的是所有常量的地址，方便以后修改一些变量，避免硬代码，修改起来很麻烦
      一般对常量命名的时候名称全部都是大写，方便辨别

"""

# 项目的根目录    运用os模块，首先获取当前文件的全部地址，在用dirname模块获取到文件夹地址，相当于把文件名称地址那一块去掉了
# 这样就形成了最基础的地址常量
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 静态文件的目录    运用os模块里面自带的join将地址拼接起来，这样就避免了不同操作系统显示不同地址的问题
ASSET_DIR = os.path.join(BASE_DIR, 'asset')

"""   
                                后面就是用到什么资源添加什么资源地址常量名称到下面
"""


# 背景图片
BG_IMG = os.path.join(ASSET_DIR, 'images/background.png')
BG_IMG_OVER = os.path.join(ASSET_DIR, 'images/game_over.png')

# 游戏分数颜色
TEXT_SOCER_COLOR = pygame.Color(255, 255, 0)
# 游戏文字地址
TEXT_FONT = os.path.join(ASSET_DIR, 'font/SIMHEI.TTF')

# 背景音乐
BG_MUSIC = os.path.join(ASSET_DIR, 'music/game_bg_music.mp3')

# 开始标题
IMG_GAME_TITLE = os.path.join(ASSET_DIR, 'images/game_title.png')
# 开始游戏的按钮
IMG_GAME_START_BTN = os.path.join(ASSET_DIR, 'images/game_start.png')


# 我方飞机的静态资源

# 对于联系在一起用的图片可使用list将其储存到一起，方便调用
OUR_PLANE_IMG_LIST = [
    os.path.join(ASSET_DIR, 'images/hero1.png'),
    os.path.join(ASSET_DIR, 'images/hero2.png')
]
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSET_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSET_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSET_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSET_DIR, 'images/hero_broken_n4.png')
]


BULLET_IMG = os.path.join(ASSET_DIR, 'images/bullet2.png')
BULLET_SHOOT_SOUND = os.path.join(ASSET_DIR, 'music/bullet.wav')     # 添加音乐需要注意的是要用.wav作为后缀

# 敌方小型飞机及音效
SMALL_ENEMY_PLANE_ING_LIST = [os.path.join(ASSET_DIR, 'images/enemy1.png')]
SMALL_ENEMY_DESTROY_IMG_LIST = [
    os.path.join(ASSET_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSET_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSET_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSET_DIR, 'images/enemy1_down4.png')
]
# 小型飞机坠毁时的音乐
SMALL_ENEMY_PLANE_SOUND = os.path.join(ASSET_DIR, 'music/enemy1_down.wav')

# 击中小型敌机所获得的分数
SCORE_SHOOT_SMALL = 10

# 历史最高分数文件地址
PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR,  'store/rest.txt')
