import shutil
from pathlib import Path

path = Path(__file__).parent
target = Path('D:/temp/ctf')
if not target.exists():
    target.mkdir()
shutil.copy(path / 'misc_blindWaterMark盲水印_bwmforpy3.py', target)
shutil.copy(path / 'misc_blindWaterMark盲水印_pinyubwm.py', target)
shutil.copy(path / 'misc_blindWaterMark_02_fourier.py', target)
print('imageIN_Beta1.0.exe')
print('Misc_BlindWatermark_隐形水印工具.exe')
