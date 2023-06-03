
import cv2
import pytesseract
import os

# 配置pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # 修改为你的tesseract安装路径

# 读取图片文件夹
image_folder = ''

# 获取文件列表
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# 处理图片并保存结果
with open('ocr_results.txt', 'w') as f:
    for file_name in image_files:
        file_path = os.path.join(image_folder, file_name)

        # 读取图片
        image = cv2.imread(file_path)

        # 使用Tesseract进行OCR识别
        text = pytesseract.image_to_string(image, lang='chi_sim+eng')

        # 写入结果到文件
        f.write(f"File: {file_name}\n")
        f.write(f"Text: {text}\n")
        f.write("\n")