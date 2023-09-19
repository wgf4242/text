import shutil
from pathlib import Path
import os

path = Path(__file__).parent
target = Path('D:/temp/ctf')
if not target.exists():
    target.mkdir()
shutil.copy(path / 'misc_blindWaterMark盲水印_bwmforpy3.py', target / 'bwm.py')
shutil.copy(path / 'misc_blindWaterMark盲水印_pinyubwm.py', target)
shutil.copy(path / 'misc_blindWaterMark_02_fourier.py', target)

runbat = target / 'bwm.bat'
with open(runbat, 'w', encoding='utf8') as f:
    f.write("python2 bwm.py decode 1.png 2.png out.png")

print('imageIN_Beta1.0.exe')
print('Misc_BlindWatermark_隐形水印工具.exe')

os.system("explorer " + str(target.absolute()))
