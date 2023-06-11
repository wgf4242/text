"""
ffmpeg -i noise.mp4 -map 0:a:0 -c:a copy output0.wav
ffmpeg -i noise.mp4 -map 0:a:1 -c:a copy output1.wav
ffmpeg -i noise.mp4 -map 0:a:2 -c:a copy output2.wav

ffmpeg -i noise.mp4 -map 0:a:0 output1.wav
ffmpeg -i noise.mp4 -map 0:a:1 output2.wav
ffmpeg -i noise.mp4 -map 0:a:2 output3.wav

音频相减一半
"""

import librosa
import soundfile as sf
import numpy as np

audio1, sr1 = librosa.load('output1.wav', sr=None)
audio2, sr2 = librosa.load('output2.wav', sr=None)

result = 2 * audio1 - audio2
sf.write('result.wav', result, sr1)
