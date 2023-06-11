"""
ffmpeg -i noise.mp4 -map 0:a:0 -c:a copy output0.wav
ffmpeg -i noise.mp4 -map 0:a:1 -c:a copy output1.wav
ffmpeg -i noise.mp4 -map 0:a:2 -c:a copy output2.wav

ffmpeg -i noise.mp4 -map 0:a:0 output1.wav
ffmpeg -i noise.mp4 -map 0:a:1 output2.wav
ffmpeg -i noise.mp4 -map 0:a:2 output3.wav

音频相减一半
"""

from scipy.io import wavfile
import numpy as np

# 加载两个音频文件
rate1, audio1 = wavfile.read('output1.wav')
rate2, audio2 = wavfile.read('output2.wav')

# 确保两个音频的采样率相同，如果不同，进行重新采样
if rate1 != rate2:
    # 重新采样audio2为与audio1相同的采样率
    audio2 = np.interp(np.linspace(0, len(audio2), len(audio1)), np.arange(len(audio2)), audio2).astype(audio1.dtype)

# 确保两个音频的长度相同，如果不同，进行裁剪或填充
length = min(len(audio1), len(audio2))
audio1 = audio1[:length]
audio2 = audio2[:length]

# 音频相减
result = audio1 - audio2 // 2

# 保存为新的音频文件
wavfile.write('output_diff.wav', rate1, result)
