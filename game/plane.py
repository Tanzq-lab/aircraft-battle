"""
飞机的封装
"""
import random
import pygame
import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """
    飞机的基础类
    """
    # 飞机的图片
    plane_images = []
    # 飞机爆炸的图片
    destroy_images = []
    # 坠毁的音乐地址
    down_sound_src = None
    # 飞机的状态 活的，死的
    active = True
    # 该飞机发射的子弹精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        # 初始化精灵组类
        super().__init__()
        self.screen = screen

        # 加载静态资源
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()

        # 飞机的速度
        self.speed = speed or 10
        # 获取飞机的位置
        self.rect = self.img_list[0].get_rect()

        # 飞机的宽度和高度
        self.plane_w, self.plane_h = self.img_list[0].get_size()

        # 游戏窗口的宽度和高度
        self.width, self.height = self.screen.get_size()

        # 改变飞机的初始化位置
        self.rect.left = int((self.width - self.plane_w) / 2)
        self.rect.top = int(self.height / 2)

    def load_src(self):
        """
        加载静态资源
        :return:
        """

        # 飞机图像
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))

        # 飞机坠毁的图像
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))

        # 飞机坠毁的音乐
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """ 飞机向上移动 """
        self.rect.top -= self.speed

    def move_down(self):
        """ 飞机向下移动 """
        self.rect.top += self.speed

    def move_left(self):
        """ 飞机向左移动 """
        self.rect.left -= self.speed

    def move_right(self):
        """ 飞机向左移动 """
        self.rect.right += self.speed

    def broken_down(self):
        """飞机坠毁特效"""
        # 1. 播放坠毁音乐
        if self.down_sound:
            self.down_sound.play()
        # 2. 播放坠毁的动画
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        # 3. 坠毁后
        self.active = False

    def shoot(self):
        """ 飞机放射子弹 """
        bullet = Bullet(self.screen, self, 15)
        self.bullets.add(bullet)


class OurPlane(Plane):
    """ 我方的飞机 """
    # 飞机的图片
    plane_images = constants.OUR_PLANE_IMG_LIST
    # 飞机爆炸的图片
    destroy_images = constants.OUR_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = None

    def update(self, war):
        """ 更新飞机的动画效果 """
        #  切换飞机的动画效果，喷气式效果
        self.move(war.key_down)

        if war.frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)

        # 飞机撞击检测
        rest = pygame.sprite.spritecollide(self, war.enemies, False)
        if rest:
            # 游戏结束
            war.status = war.OVER
            # 销毁所有敌方飞机
            war.enemies.empty()
            war.small_enemies.empty()
            # 飞机坠毁效果
            self.broken_down()

    def move(self, key):
        """  飞机移动自动控制 """
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    # 越界处理
    def move_up(self):
        super().move_up()
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        super().move_down()
        if self.rect.bottom > self.height:
            self.rect.bottom = self.height

    def move_left(self):
        super().move_left()
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.right > self.width:
            self.rect.right = self.width


class SmallEnemyPlane(Plane):
    """ 敌方小型飞机 """
    # 飞机的图片
    plane_images = constants.SMALL_ENEMY_PLANE_ING_LIST
    # 飞机爆炸的图片
    destroy_images = constants.SMALL_ENEMY_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = constants.SMALL_ENEMY_PLANE_SOUND

    def __init__(self, screen, speed):
        super().__init__(screen, speed)
        self.init_pos()

    def init_pos(self):
        """ 改变飞机的随机位置 """
        self.rect.left = random.randint(0, self.width - self.plane_w)
        self.rect.top = random.randint(-5 * self.plane_h, -self.plane_h)

    def update(self, *args):
        """
        更新飞机的移动
        :param args:
        :return:
        """
        super().move_down()
        # 画在屏幕上
        self.blit_me()

        # 超出范围的处理
        if self.rect.top >= self.height:
            self.active = False
            self.reset()

    def reset(self):
        """ 重置飞机的状态， 达到复用的效果 """
        self.active = True
        self.init_pos()

    def broken_down(self):
        """ 飞机爆炸 """
        super().broken_down()
        self.reset()
