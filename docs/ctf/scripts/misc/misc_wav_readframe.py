import wave				#调用wave模块
f = wave.open(r"00000000.wav", "rb")		#读取语音文件
params = f.getparams()			#返回音频参数
nchannels, sampwidth, framerate, nframes = params[:4] #赋值声道数，量化位数，采样频率，采样点数
print(nchannels,sampwidth,framerate,nframes)# 输出声道数，量化位数，采样频率，采样点数
f = f.getnframes()
print(f)