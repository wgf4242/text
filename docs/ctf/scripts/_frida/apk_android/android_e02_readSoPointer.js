// 2015阿里移动安全挑战赛第二题AliCrackme_2
Java.perform(function () {
  function readSoPointer() {
    var soAddr = Module.findBaseAddress("libcrackme.so")

    send(Memory.readUtf8String(Memory.readPointer(soAddr.add(0x628c))))
  }
  readSoPointer();
})
