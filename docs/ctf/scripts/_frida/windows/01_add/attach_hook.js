var baseaddr = Module.getBaseAddress("TestAdd.exe")
console.log("baseaddr:", Number(baseaddr).toString(16))

var add_offset = 0x1262

Interceptor.attach(ptr(baseaddr + add_offset), {
    onEnter: function (args) {
        console.log('Enter with args: ', args)
    },
    onLeave: function (retval) {
        console.log('Leave with return value: ', retval)
    }
})
