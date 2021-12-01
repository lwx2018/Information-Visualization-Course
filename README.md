# Information-Visualization-Course
Information-Visualization-Course

2021信息可视化与可视化分析平时作业

一、词云

1.1运行环境

·pycharm2020

·python3.7

·Windows10

1.2运行步骤

·首先使用pycharm打开main.py文件和harrypotter.py文件

·main.py文件是没有使用wordcloud库实现的词云，harrypotter.py文件使用了wordcloud库实现词云

·main.py文件和harrypotter.py文件中可以更改读取的文本，默认是读取1.Harry Potter and the Sorcerer's Stone.txt	文件，记得使用转义符

·harrypotter.py文件可以更改词云生成的背景，默认为4.png

1.3算法原理

·main.py文件中读取文本之后，通过jieba库进行分词，在针对每一个词出现的频数进行统计，结果为一个词典，由词和该次出现的次数组成，再根据选择想要出现的词的个数选出前多少个词，之后可以自选筛选掉不需要的词，为了展现出最大出现频数的一些词，把筛选过的词的列表分成想要个数的子列表。

·重叠检测方法，每个词语被框在一个矩形里（宽为w，高为h），只需要对图片每个位置 (x,y) 进行计算，如果 (x,y) 到 (x + w - 1, y + h - 1) 这个矩形区域内没有内容，就能够放置这个词语。即判断蓝色区域有无内容可以通过该区域像素点之和来判断，通过绿色区域像素值和加黄色区域像素和减去紫色区域和青色区域像素和来计算。

<img width="415" alt="image" src="https://user-images.githubusercontent.com/40064484/144163016-532ee45a-6ca6-4572-9be1-ba1cfe3e5254.png">

1.4算法效果

<img width="416" alt="image" src="https://user-images.githubusercontent.com/40064484/144163109-e12da7b2-e432-4399-b8dc-63c4de2d8691.png">

main.py的效果图

<img width="416" alt="image" src="https://user-images.githubusercontent.com/40064484/144163155-b6100e5c-1368-48a6-8729-afaa44386ae0.png">

harrypotter.py的效果图

二、node-link

2.1运行环境

·chrome浏览器

·http服务器

·d3.v3

·node-v16.13.0

2.2运行步骤

·安装Node后，使用npm安装，http-server-g

·在当前目录即包括.html的目录，进入cmd，执行http-server -c-1

·在chrome中输入localhost:8080/2.html，或者cmd中所有的available on：地址

2.3算法原理

·使用d3布局方法增加一个tree布局，并设定相应的数据

·使用d3的自带方法json读取cityname.json的数据，为了实现之后的节点展开与隐藏，根据数据生成的nodes集合，使用forEach方法记录当前位置

·鼠标点击响应事件nodeClick，修改节点子节点，调用函数update

·update函数，更新节点数据和链接数据，首先需要再加载一遍节点数据和链接数据，为了实现动态效果，需要在相应的节点和链接进行transition变化效果，要为变化后的node修改位置、circle标记、文字标记，再把不需要展示的node去除，链接是相同的操作。在最后需要记录当前位置，为下次动画做初始值。

2.4算法效果

<img width="334" alt="image" src="https://user-images.githubusercontent.com/40064484/144163257-6749d1eb-aca1-415f-a886-74cbcc877014.png">

初始展示收缩前

<img width="350" alt="image" src="https://user-images.githubusercontent.com/40064484/144163269-e1c1a37c-1102-4ca1-abb7-e743ca1ce70f.png">

收缩后
