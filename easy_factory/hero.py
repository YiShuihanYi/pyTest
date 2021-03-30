# -*- encoding: utf-8 -*-

"""
2.使用简单工厂方法，实现TMO和police，两个英雄
1）一个回合制游戏，给两个英雄分别定义两个类，timo和PPolice。每个英雄都有hp和power
属性。hp代表血量，power代表攻击力
2）每个英雄都有fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量多的人获胜
3）每个英雄有一个speak_lines方法：打印以下内容
timo:提莫队长正在待命
police：见识一下法律的子弹
"""
from logging import exception


class Hero:
    name = ""
    hp = 0
    power = 0

    def fight(self, enemy):
        my_hp = self.hp - enemy.power
        enemy_hp = enemy.hp - self.power
        if my_hp > enemy_hp:
            print(f"{self.name} win")
        elif my_hp < enemy_hp:
            print(f"{enemy.name} win")
        else:
            print(f"go on!")

    def speak_lines(self):
        if self.name == "timo":
            print("提莫队长正在待命")
        elif self.name == "police":
            print("见识一下法律的子弹")