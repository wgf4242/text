var baseaddr = Module.getBaseAddress("TestAdd.exe")

var ptr_func_addr = baseaddr.add(0x4f40)

Interceptor.replace(
  ptr_func_addr,
  new NativeCallback(
    (a, b) => {
      console.log("args: ", a, b)
      return a - b
    },
    "int",
    ["int", "int"]
    // "mscdecl" "fastcall" , 不指定就是默认的调用约定
  )
)
