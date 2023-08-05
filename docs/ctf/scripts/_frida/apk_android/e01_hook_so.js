function hook() {
  // 1,拿到目标 so 的基址
  // https://frida.re/docs/javascript-api/
  var base  = Module.findBaseAddress("libwolf.so")

  console.log("base =", base);
}

setImmediate(hook);
// frida -UF -l hook.js -o out2.log