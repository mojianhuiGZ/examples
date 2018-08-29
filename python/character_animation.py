#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
视频转字符动画工具
参考:
    https://www.cnblogs.com/kirito-c/p/5971988.html
'''

import numpy as np
import cv2

# 用于生成字符画的像素
pixel_to_chars = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"

def video_to_images(video_path, image_size):
    """
    :param video_path: 字符串, 视频文件的路径
    :param size: 二元组, (宽, 高)，图像尺寸
    :return: 图像列表, numpy.ndarray
    """
    img_list = []
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read() # ret表示是否读取到图像. frame是图像矩阵, numpy.ndarry.
        if ret:
            # 转换成灰度图
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(gray, image_size, interpolation=cv2.INTER_LINEAR)
            img_list.append(img)
        else:
            break
    cap.release()
    return img_list


def image_to_characters(image):
    """
    :param img: numpy.ndarray, 图像矩阵
    :return: 字符串列表. 表示图像对应的字符画，每一行对应图像中的一行像素
    """
    result = []
    height, width = image.shape
    for row in range(height):
        line = ''
        for col in range(width):
            percent = image[row][col] / 255
            index = int(percent * (len(pixel_to_chars) - 1))
            # 添加字符像素
            #line += pixel_to_chars[index] + ' '
            line += pixel_to_chars[index]
        result.append(line)
    return result

def images_to_character_animation(images):
    video_chars = []
    for img in images:
        video_chars.append(image_to_characters(img))
    return video_chars

def save_character_animation(file_path, character_animation):
    with open(file_path, 'w') as f:
        f.write('%d %d %d\n' % (len(character_animation[0][0]),
                                len(character_animation[0]),
                                len(character_animation)))
        f.write('\n')

        for image in character_animation:
            for line in image:
                f.write(line)
                f.write('\n')
            f.write('\n')

if __name__ == "__main__":
    images = video_to_images('test.mp4', (320, 180))
    animation = images_to_character_animation(images[0:25])
    save_character_animation('test_ascii.txt', animation)

