from game.war import PlaneWar
"""

                       在构造整个项目的时候要将整个思路想好，主函数写的东西要少且精确

"""


def main():
    """游戏入口， main方法"""
    # 引入类对象
    war = PlaneWar()  # 利用 CTRL 键加鼠标点击可快速访问到相应的函数上去。
    # 添加小型敌方飞机
    war.add_small_enemies(6)
    # 运行整个流程
    war.run_game()


if __name__ == '__main__':
    main()