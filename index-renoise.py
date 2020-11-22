# opencv 轉黑白
# pillow 套件

import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
# 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


# 用来正常显示负号


def get_bin_table(threshold=113):
    # 0表示黑色,1表示白色 binary
    # 闕值二值化

    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def sum_9_region_new(img, x, y):
    """确定噪点 """
    cur_pixel = img.getpixel((x, y))  # 当前像素点的值
    width = img.width
    height = img.height

    if cur_pixel == 1:  # 如果当前点为black色区域,则不统计邻域值
        return 0

    if y < 4:  # 本例中，前两行的黑点都可以去除
        return 1
    elif y > height - 6:  # 最下面两行
        return 1
    else:  # y不在边界
        if x < 3:  # 前两列
            return 1
        elif x == width - 1:  # 右边非顶点
            return 1
        else:  # 具备9领域条件的
            sumall = img.getpixel((x - 1, y - 1)) \
                     + img.getpixel((x - 1, y)) \
                     + img.getpixel((x - 1, y + 1)) \
                     + img.getpixel((x, y - 1)) \
                     + cur_pixel \
                     + img.getpixel((x, y + 1)) \
                     + img.getpixel((x + 1, y - 1)) \
                     + img.getpixel((x + 1, y)) \
                     + img.getpixel((x + 1, y + 1))
            return 9 - sumall


def collect_noise_point(img):
    """收集所有的噪点"""
    noise_point_list = []
    for x in range(img.width):
        for y in range(img.height):
            res_9 = sum_9_region_new(img, x, y)
            if (0 < res_9 < 3) and img.getpixel((x, y)) == 0:  # 找到孤立点
                pos = (x, y)
                noise_point_list.append(pos)
    return noise_point_list


def remove_noise_pixel(img, noise_point_list):
    """根据噪点的位置信息，消除二值图片的黑点噪声"""
    for item in noise_point_list:
        img.putpixel((item[0], item[1]), 1)


def main():
    # 轉灰度 level >>
    img = Image.open('img/colorcaptcha.jpg')
    # print('image mode : ', img.mode)
    # print(img.getpixel((0, 0)))
    # co = img.getcolors()
    # print(co)
    # print('-' * 30)
    imgry = img.convert('L')
    # print('imgry mode ： ', imgry.mode)
    # print(imgry.getpixel((0, 0)))
    # gry = imgry.getcolors()
    # print(gry)
    print('-' * 30)
    table = get_bin_table()
    binary = imgry.point(table, '1')
    noise_point_list = collect_noise_point(binary)
    remove_noise_pixel(binary, noise_point_list)
    print('binary mode ： ', binary.mode)
    print('-' * 30)
    # width, height = binary.size
    # lis = binary.getdata()
    # lis = list(lis)
    # start = 0
    # step = width
    # for i in range(height):
    #     for p in lis[start: start + step]:
    #         if p == 1:  # 将白色的点变成空格，方便人眼看
    #             p = ''
    #         print(p)
    #     print()
    #     start += step

    # imgry.show() 基礎查看

    # matplotlib 進階顯示圖片設定

    plt.figure("img")
    plt.figure(num=1, figsize=(1.08, 1.44))
    plt.title('GRAYMODE')
    plt.axis('off')  # 不顯示座標軸
    plt.imshow(img)
    # plt.show()
    plt.imshow(imgry, cmap='Greys_r')
    # plt.show()
    plt.imshow(binary, cmap='Greys_r')
    plt.title('REMOVING')

    binary.save('output/DIY/gray02-ok.png')
    text = pytesseract.image_to_string(binary, lang='chi_tra', config='--psm 6')
    print(text)
    plt.show()
    f = open('output/gray02.txt', 'w')
    f.write(text)
    f.close()


if __name__ == '__main__':
    main()
