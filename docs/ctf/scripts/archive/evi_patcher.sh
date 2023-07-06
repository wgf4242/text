rmdir -rf f1 f2 f3 fix 2>/dev/null
mkdir {f1,f2,f3,fix}
echo f1 f2 f3 | xargs -n 1 cp -v $*


for i in {1..3}; do
  python /home/kali/archive/evilPatcher-main/evilPatcher.py "f${i}/$*" /home/kali/archive/evilPatcher-main/sandboxs/sandbox${i}.asm
  cp "f${i}/$*.patch" fix/$*${i}
done

# echo 'alias evil="/bin/bash /home/kali/archive/evilPatcher-main/p.sh $*"' >> ~/.zshrc
