import matplotlib.pyplot as plt

from wordcloud import WordCloud
import numpy as np
import jieba
from PIL import Image

if __name__ == '__main__':
    text = open('1.Harry Potter and the Sorcerer\'s Stone.txt', 'r').read()  # 不加编码方式就会报错

    wordlist = jieba.cut(text, cut_all=True)

    word_sp = " ".join(wordlist)  # 用jieba分词

    mask = np.array(Image.open("4.png"))
    my_wordcloud = WordCloud(relative_scaling=0.3,mask=mask, font_path='timesi.ttf', width=800, height=600, mode='RGBA',
                         background_color=None).generate(
    word_sp)  # 最原始的对分词后的文本生成词云

    plt.imshow(my_wordcloud)  # 显示词云

    plt.axis("off")#除去坐标
    plt.savefig('wordcloud2.png')
    plt.show()
