# https://github.com/ghostmaze/Android-Reverse/raw/master/WhyShouldIPay/WhyShouldIPay.apk
# https://bbs.pediy.com/thread-227233.htm
# frida -U -l aaa.js "Not Premium App"
import frida,sys
 
 
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)
 
 
js_code = '''
    Java.perform(function(){
        var hook_Activity = Java.use('de.fraunhofer.sit.premiumapp.LauncherActivity');
        hook_Activity.showPremium.implementation = function(v){
            var Key = this.getKey();
            var Mac = this.getMac();
            send(Key);
            send(Mac);
 
        }
    });
'''
 
 
session = frida.get_usb_device().attach("Not Premium App")
script = session.create_script(js_code)
script.on('message',on_message)
script.load()
sys.stdin.read()