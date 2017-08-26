class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# study drills
# 1.
find_friend = Song(["找呀找呀找朋友",
                    "找到一个好朋友",
                    "敬个礼握握手你是我的好朋友"])

find_friend.sing_me_a_song()

# 2.
lyr = ["两只老虎", "两只老虎", "跑得快"]
two_tigers = Song(lyr)
two_tigers.sing_me_a_song()

v = "只会唱儿歌？\n看样子是的！"
cs = Song(v)
cs.sing_me_a_song()
# 输出结果如下：
# 只
# 会
# 唱
# 儿
# 歌
# ？
#
#
# 看
# 样
# 子
# 是
# 的
# ！
