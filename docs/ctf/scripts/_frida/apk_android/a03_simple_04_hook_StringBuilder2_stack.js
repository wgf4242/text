// frida -U com.richfit.qixin.partybuild.product -l l2.js
// frida -UF -l l3.js
Java.perform(function () {
    var threadef = Java.use('java.lang.Thread')
    var threadinstance = threadef.$new()

    function Where(stack){
        var at = ""
        for(var i = 0; i < stack.length; ++i){
            at += stack[i].toString() + "\n"
        }
        return at
    }

    var strCls = Java.use("java.lang.StringBuilder");
    strCls.toString.implementation = function(){
        var result = this.toString();
        // console.log(result.toString());
        if(result.toString().indexOf("AES/CBC/PKCS5Padding") >= 0 )
        // if(result.toString().indexOf("AES") >= 0 )
        {
            console.log('yes!!!!!!!!!!!!')
            console.log(result.toString());
            var stack = threadinstance.currentThread().getStackTrace();
            console.log("Rc Full call stack:" + Where(stack));
        }
        return result;
    }
});
