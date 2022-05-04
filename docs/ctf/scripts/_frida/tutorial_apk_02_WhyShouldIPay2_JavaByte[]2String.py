import frida,sys
 
def on_message(message,data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)
 
jscode = """
Java.perform(function(){
    function stringToBytes(str){
    var javaString = Java.use('java.lang.String');
    var bytes = [];
    bytes = javaString.$new(str).getBytes();
    return bytes;
    }
 
    function bytesToString(bytes){
      var javaString = Java.use('java.lang.String');
      return javaString.$new(bytes);
    }   
 
    var LauncherActivity = Java.use('de.fraunhofer.sit.premiumapp.LauncherActivity');
    var activeKey_str="";
    LauncherActivity.getKey.implementation = function(v){
      return activeKey_str;
    }
    LauncherActivity.showPremium.implementation = function(v){
      send("Hook start...");
      var key  = this.getKey();
      var mac = this.getMac();
      send("key:"+key);
      send("mac:"+mac);
      var MainActivity = Java.use('de.fraunhofer.sit.premiumapp.MainActivity');
      var activeKey = MainActivity.xor(stringToBytes(mac),stringToBytes("LICENSEKEYOK"));
      activeKey_str = bytesToString(activeKey);   
      send("activeKey:" + activeKey_str);
      this.showPremium(v);
    }
}
);
"""
 
dev = frida.get_usb_device()
session = dev.attach('Not Premium App')
script = session.create_script(jscode)
script.on('message',on_message)
script.load()
sys.stdin.read()