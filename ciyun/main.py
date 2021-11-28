import random
import math

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import jieba

from collections import Counter

maxout = 500  # 最大输出频次高的词数
width = 800
hight = 600


def find_position(img, size_x, size_y):  # size_x代表着当前词语所占矩形的宽度，size_y代表高度
    # 返回给定轴上的累积和numpy.cumsum（a，axis = None，dtype = None，out = None ）
    # 0为纵轴，1为横轴
    # assarray()创建ndarray数组对象,即先把image数据转为矩阵
    integral = np.cumsum(np.cumsum(np.asarray(img), axis=1), axis=0)
    for x in range(1, width - size_x):
        for y in range(1, hight - size_y):
            # 左上角小矩形+大矩形(矩阵行对应y，列对应x)
            area = integral[y - 1, x - 1] + integral[y + size_y - 1, x + size_x - 1]
            # 减去左侧矩形和上方矩形
            area -= integral[y - 1, x + size_x - 1] + integral[y + size_y - 1, x - 1]
            # area为0,返回（x,y)即该区域还没有词占据
            if not area:
                return x, y
    # 返回为空
    return None, None


def get_words(text):  # 词频统计
    seg_list = jieba.cut(text)
    c = Counter()
    # Counter 作为字典(dict)的一个子类用来进行hashtable计数，
    # 将元素进行数量统计、计数后返回一个字典,键值为元素：值为元素个数
    for i in seg_list:
        if len(i) > 1 and i != '\r\n':
            c[i] += 1
    ls = []
    print(c)
    # 选出词频前maxout个的词
    for (i, j) in c.most_common(maxout):
        ls.append(i)

    print(ls)
    # a = sorted(ls.items(), key=lambda x: x[1])#字典升序
    # a1 = sorted(ls.items(), key=lambda x: x[1], reverse=True)#降序排序
    return ls


def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) * children_list_len)  # iter声称迭代器，zip把迭代器里的对象作为相应大小的元祖，解压为列表
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list


# 循环将词语绘制到图像上
def main():
    words = open('1.Harry Potter and the Sorcerer\'s Stone.txt', 'r').read()  # 词语素材读取文件
    word_re = get_words(words)
    # 筛选排除一些可能不是那么有价值的单词
    stop_words = ['is', 'and', 'the', 'to', 'of', 'it', '--', '...', '....']

    for i in word_re:  # 此时的列表中元素是按照出现频数降序排列
        if i in stop_words:
            word_re.remove(i)
    print(word_re)
    sublist_length = 50  # 想要的子列表的长度
    word_list = list_of_groups(word_re, sublist_length)  # 原本的列表分成等长的maxout / sublist_length个子列表
    print(word_list[0])
    print(len(word_list))
    le = maxout / sublist_length

    # 新建画布对象，Image.new(mode,size,color=None)
    img = Image.new('L', (width,
                          hight))
    # img = Image.open('3.png')
    # 新建画布绘画对象
    draw = ImageDraw.Draw(img)
    for i in range(int(le)):
        print(i)
        if i == 0:
            for word in word_list[i]:

                font_size = 180
                font = ImageFont.truetype('timesbd.ttf', font_size)
                box_size = draw.textsize(word, font=font)
                x, y = find_position(img, box_size[0], box_size[1])
                if x:
                    draw.text((x, y), word, fill="white", font=font)
        else:
            for word in word_list[i]:
                # 字体大小随机
                font_size = random.randint(1, 150)
                # 字体为黑体
                font = ImageFont.truetype('times.TTF', font_size)

                # 计算文字矩形框的大小(宽x,高y)
                box_size = draw.textsize(word, font=font)

                # 图像上找出文字放置的位置
                x, y = find_position(img, box_size[0], box_size[1])

                # 存在x，则将词语放置在（x，y）处
                if x:
                    draw.text((x, y), word, fill="white", font=font)
    img.show()
    img.save('wordcloud1.png')


if __name__ == '__main__':
    main()
