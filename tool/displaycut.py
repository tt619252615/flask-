import jieba
import jieba.posseg as pseg
from collections import Counter
import matplotlib.pyplot as plt
import os

def cut_and_tag(content):
    words_and_flags = [(x.word, x.flag) for x in pseg.cut(content)]
    seg_result = [word for word, flag in words_and_flags]  # 解构元组
    pos_img = create_pos_img(words_and_flags)
    return seg_result, pos_img

def create_pos_img(words_and_flags):
    flags = [flag for word, flag in words_and_flags]
    counter = Counter(flags)
    plt.figure(figsize=(20,10))
    plt.bar(counter.keys(), counter.values())
    img_path = os.path.join('static', 'pos_img.png')  # 将图像保存到 static 文件夹
    plt.savefig(img_path)  # 保存图像，而不是显示图像
    return img_path  # 返回图像的路径，以便在 HTML 中使用
