/* NewStarCTF 2022 艾克体悟题
* public class FlagActivity{
     private int cnt = 0; // instance.cnt.value 来访问
  }
* */
Java.perform(function () {
    let FlagActivity = Java.use("com.droidlearn.activity_travel.FlagActivity");
    FlagActivity["access$004"].implementation = function (instance) {
        instance.cnt.value = 100001;
        let ret = this.access$004(instance);
        return ret;
    };
});

// Objection 方式 - 堆上查找实例, 修改cnt值。
/*
objection -g com.droidlearn.activity_travel explore
android intent launch_activity com.droidlearn.activity_travel.FlagActivity

android heap search instances com.droidlearn.activity_travel.FlagActivity --dump-args --dump-backtrace --dump-return

Hashcode  Class                                        toString()
---------  -------------------------------------------  ---------------------------------------------------
112045134  com.droidlearn.activity_travel.FlagActivity  com.droidlearn.activity_travel.FlagActivity@6adac4e

android heap evaluate 112045134
clazz.cnt.value = 100001;
// Esc Enter 返回
*/