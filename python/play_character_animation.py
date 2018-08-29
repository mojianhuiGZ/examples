#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
播放字符动画的工具
参考:
    https://www.cnblogs.com/kirito-c/p/5971988.html
'''

import time
import curses
import sys

def load_character_animation(file_path):
    animation = []

    with open(file_path, 'r') as f:
        f.readline()
        f.readline()

        while True:
            image = []
            while True:
                line = f.readline()
                if line:
                    image.append(line.rstrip('\n'))
                else:
                    break
            if image:
                animation.append(image)
            else:
                break

    return animation


def play_character_animation(animation):
    """
    播放字符视频
    :param animation: 字符动画. 每个元素表示一帧
    :return: None
    """
    width, height = len(animation[0][0]), len(animation[0])

    # 初始化curses
    stdscr = curses.initscr()
    curses.start_color()
    try:
        # 调整窗口大小，宽度最好略大于字符画宽度。另外注意curses的height和width的顺序
        stdscr.resize(height, width * 2)

        for image in range(len(animation)):
            for line in range(height):
                stdscr.addstr(line, 0, animation[image][line], curses.COLOR_WHITE)
            stdscr.refresh()
            #time.sleep(1 / 24) # 粗略地控制播放速度
            time.sleep(1) # 粗略地控制播放速度
    finally:
        curses.endwin()
    return

if __name__ == "__main__":
    animation = load_character_animation(sys.argv[1])
    play_character_animation(animation)

