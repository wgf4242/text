var baseaddr = Module.getBaseAddress("fib_print.exe")
console.log("baseaddr:", Number(baseaddr).toString(16))

var func_fib_ptr = baseaddr.add(0x14c0)
console.log(Number(baseaddr).toString(16), Number(func_fib_ptr).toString(16))

var fib = function (n) {
  let cache = []
  for (let i = 0; i <= n; i++) {
    if (i == 1 || i == 0) {
      cache[i] = i
    } else {
      cache[i] = cache[i - 1] + cache[i - 2]
    }
  }
  return cache[n]
}

Interceptor.replace(
  func_fib_ptr,
  new NativeCallback(
    n => {
      const r = fib(n)
      console.log("args: ", r)
      return r
    },
    "uint64",
    ["int"]
  )
)
