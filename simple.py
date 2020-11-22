# from PIL import Image
import pytesseract
import cv2

# img = Image.open('img/DIY/1.png')
#
# imgry = img.convert('L')
#
# imgry.save('output/gray.png')

# opencv 方式讀取圖檔
imgrycv = cv2.imread('img/DIY/1.png', cv2.IMREAD_GRAYSCALE)
print('-' * 30)
cv2.imshow('CaptchaImage', imgrycv)
cv2.imwrite('output/GRAY/0.tiff', imgrycv)

text = pytesseract.image_to_string(imgrycv, lang='eng', config='--psm 10 ')
print(text)
print('-' * 30)
print(imgrycv)
print('-' * 30)

f = open('output/captcha.txt', 'w')
f.write(text)
f.close()

cv2.waitKey(0)
cv2.destroyAllWindows()



# 侵蝕與膨脹 去除黑白點
# kernel = np.ones((5,5), np.uint8)
# binary = cv2.dilate(imgcv, kernel, iterations = 2)
# binary = cv2.erode(binary, kernel, iterations = 1)
# plot.imshow(binary,camp="gray")
# plot.show()
# cv2.imwrite('output/removeBW.tiff', imgcv)
