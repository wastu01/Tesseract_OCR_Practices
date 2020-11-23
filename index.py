# opencv 轉黑白
# pillow 套件

import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
# 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


# 用来正常显示负号


def get_bin_table(threshold=95):
    # 0表示黑色,1表示白色 binary
    # 闕值二值化

    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def main():
    # 轉灰度 level >>
    img = Image.open('img/DIY/healthpaper.jpg')
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

    # binary.save('output/DIY/1.tiff')

    # imgry.show() 基礎查看

    # matplotlib 進階顯示圖片設定
    # , figsize = (1.67, 1.04)
    plt.figure("img")
    plt.figure(num=1)
    plt.axis('off')  # 不顯示座標軸
    # plt.imshow(img)
    # plt.show()
    # plt.imshow(imgry, cmap='Greys_r')
    plt.title('GRAYMODE')
    # plt.show()
    text = pytesseract.image_to_string(binary, lang='chi_tra+eng')
    print(text)
    f = open('output/DIY/healthpaper.txt', 'w')
    f.write(text)
    f.close()
    plt.imshow(binary, cmap='Greys_r')
    plt.title('BINARY')
    plt.show()


if __name__ == '__main__':
    main()
