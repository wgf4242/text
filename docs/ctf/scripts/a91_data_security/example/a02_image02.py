# 打开视频文件
video_capture = cv2.VideoCapture(video_path)

# 创建输出文件
with open(output_file, 'w') as f:
    frame_count = 0
    while video_capture.isOpened():
        # 逐帧读取视频
        ret, frame = video_capture.read()

        if not ret:
            break

        # 使用Tesseract进行OCR识别
        text = pytesseract.image_to_string(frame, lang='chi_sim+eng')

        # 写入结果到文件
        f.write(f"Frame: {frame_count}\n")
        f.write(f"Text: {text}\n")
        f.write("\n")

        frame_count += 1

# 释放视频对象
video_capture.release()