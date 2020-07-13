import constants


class PlayRest(object):
    __score = 0  # 总分
    __life = 3  # 生命数量
    __blood = 1000  # 生命值

    @property
    def score(self):
        """ 单次游戏分数 """
        return self.__score

    @score.setter
    def score(self, value):
        """ 设置游戏分数 """
        if value < 0:
            return None
        self.__score = int(value)

    def set_history(self):
        """ 记录最高分  """
        # 读取文件中的分数
        # 比较 + 更新分数
        if int(self.get_max_sore()) < self.__score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w') as f:
                f.write(('{0}'.format(self.__score)))

    def get_max_sore(self):
        """ 读取文件中的历史最高分 """
        with open(constants.PLAY_RESULT_STORE_FILE, 'r') as f:
            r = f.read()
            if r:
                rest = r
            return r
