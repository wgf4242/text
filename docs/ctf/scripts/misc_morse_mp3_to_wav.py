from pydub import AudioSegment

codefile_mp3 = "mooooooooooorse_02.mp3"
codefile_wav = "sampleMorseCode.wav"
# mcode = AudioSegment.from_mp3(codefile_mp3)
mcode = AudioSegment.from_mp3(codefile_mp3)
b = mcode.export(codefile_wav , format="wav")
print(b)