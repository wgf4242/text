# 设置好evilPatcher路径

if [ -z "$1" ] || [ -z "$2" ] ; then
  echo "please input eval [file] [server_path]"
  exit
fi

rmdir -rf f1 f2 f3 fix 2>/dev/null
mkdir {f1,f2,f3,fix}
echo f1 f2 f3 | xargs -n 1 cp -v $*


for i in {1..3}; do
  python /home/kali/archive/evilPatcher-main/evilPatcher.py "f${i}/$1" /home/kali/archive/evilPatcher-main/sandboxs/sandbox${i}.asm
  cp "f${i}/$1.patch" fix/$1${i}
  rm -rf update 2>/dev/null
  mkdir update
  cp fix/$1${i} update/
  echo cp -f $1${i} $2 > update/update.sh
  tar zcvf $(basename $PWD)${i}.tar.gz update
done
