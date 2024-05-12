// https://bbs.kanxue.com/thread-278134.htm
Java.perform(function () {
    // write1();
    write_mes_2();

    readfile1_reflect();
    // readFile_2("/sdcard/test.txt");
});

function write1() {
    var file = new File("/sdcard/test.txt", "w");
    file.write("Hello Word!\n");
    file.flush();
    file.close();
}

function write_mes_2() {
    var addr_fopen = Module.findExportByName("libc.so", "fopen");
    var addr_fputs = Module.findExportByName("libc.so", "fputs");
    var addr_fclose = Module.findExportByName("libc.so", "fclose");

    var fopen = new NativeFunction(addr_fopen, "pointer", ["pointer", "pointer"]);
    var fputs = new NativeFunction(addr_fputs, "int", ["pointer", "pointer"]);
    var fclose = new NativeFunction(addr_fclose, "int", ["pointer"]);
    var filename = Memory.allocUtf8String("/sdcard/test.txt");
    var open_mode = Memory.allocUtf8String("w+");
    var file = fopen(filename, open_mode);
    console.log("fopen file:", file);

    var buffer = Memory.allocUtf8String("Hello Word!2\n");
    var ret = fputs(buffer, file);
    console.log("fputs ret:", ret);
    fclose(file);
}

function readfile1_reflect() {
    var fileName = "/sdcard/test.txt"
    console.log("> Reading file: ", fileName);
    var JString = Java.use("java.lang.String");
    var Files = Java.use("java.nio.file.Files");
    var Paths = Java.use("java.nio.file.Paths");
    var URI = Java.use("java.net.URI");
    var pathName = "file://" + fileName;
    var path = Paths.get(URI.create(pathName));
    var fileBytes = Files.readAllBytes(path);
    var ret = JString.$new(fileBytes);
    console.log(ret)
    return ret;
}

function readFile_2(fileName){
    var addr_fopen = Module.findExportByName("libc.so", "fopen");
    var addr_fread = Module.findExportByName("libc.so", "fread");
    var addr_fseek = Module.findExportByName("libc.so", "fseek");
    var addr_ftell = Module.findExportByName("libc.so", "ftell");
    var addr_fclose = Module.findExportByName("libc.so", "fclose");

    var fopenptr = new NativeFunction(addr_fopen, "pointer", ["pointer", "pointer"]);
    var freadptr = new NativeFunction(addr_fread, 'int', ['pointer', 'int','int','pointer']);
    var fseekptr = new NativeFunction(addr_fseek, 'int', ['pointer', 'int','int']);
    var ftellptr = new NativeFunction(addr_ftell, "int", ["pointer"]);
    var fcloseptr = new NativeFunction(addr_fclose, "int", ["pointer"]);

    var pf = fopenptr(Memory.allocUtf8String(fileName), Memory.allocUtf8String("rb"))
    fseekptr(pf, 0, 2);
    var size = fseekptr(fp);
    fseekptr(pf, 0, 0);
    console.log(size)
    var databuffer = Memory.alloc(size);
    freadptr(databuffer, 1, size, pf);
    console.log(databuffer.readCString())
    fcloseptr(file);
}
