# -*- coding:utf-8 -*-

# 现在请书写一个函数，该函数的输入为两个参数：
# - 需要处理的文本
# - 排版宽度。
# 该函数的返回值为预处理后的文本。预处理后的文本为每一节，及其所在的行号。中间以分号隔
# 开。若一个节跨越了多行，则行号用逗号隔开，并从小到大进行排列。
# 例如，假设输入为：The main theme of education in engineering school is learning
# to teach yourself，并且排版宽度指定为 30，则返回：
# The(1); (1);main(1); (1);theme(1); (1);of(1); (1);education(1); (1);in(1);
# (2);engineering(2); (2);school(2); (2);is(2); (2);learning(2,3); (3);to(3);
# (3);teach(3); (3);yourself(3);

content = 'The main theme of education in engineering school is learning to teach yourself'


def format_txt(txt, width):

    # 分割字符串
    word_list = []  # 分割后的单词list
    atsplit = True  # 是否在分割位置
    for char in txt:
        if char == ' ':
            atsplit = True
            word_list.append(' ')
        else:
            if atsplit:
                word_list.append(char)
                atsplit = False
            else:
                # 把字母加在最后一个单词上
                word_list[-1] = word_list[-1] + char

    start = 0  # 参考位置
    start_line = 1  # 开始的行数
    result = ''  # 最终结果
    for index, e in enumerate(word_list):
        start = start + len(e)  # 开始位置加上单词长度
        is_end = start % width  # 是否在行尾
        word_height = start / width  # 是否跨行
        # 如果单词不跨行，直接输出当前行数
        if word_height == 0 or is_end == 0:
            result = result + word_list[index] + '(' + str(start_line) + ');'
        else:  # 否则，输出单词跨的行遍历的递增列表
            i = 0
            lines = ''
            while i < word_height + 1:
                lines = lines + str(start_line + i) + ','
                i = i + 1
            lines = lines[:-1]
            result = result + word_list[index] + '(' + lines + ');'
        # 刷新参考位置
        start = start - width * word_height
        start_line = start_line + word_height
    return result


print format_txt(content, 24)
