/* NewStarCTF 2022 艾克体悟题
* public class FlagActivity{
     private int cnt = 0; // instance.cnt.value 来访问
  }
* frida -UF -l a02_simple.js
*/
Java.perform(function () {
    let MainActivity = Java.use("com.new_star_ctf.u_naive.MainActivity");
    MainActivity["encry"].implementation = function (str, i2, str2) {
        console.log('encry is called' + ', ' + 'str: ' + str + ', ' + 'i2: ' + i2 + ', ' + 'str2: ' + str2);
        let ret = this.encry(str, i2, str2);
        console.log('encry ret value is ' + ret);
        console.log('type ' + typeof (ret));

        var flag = '';
        for (var i = 0; i < ret.length; i++) {
            console.log('reti', ret[i] & 0xff)
            flag += String.fromCharCode(ret[i]);
        }

        return ret;
    };
});