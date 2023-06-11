#include <idc.idc>

// 循环获取指定地址一个字节大小数据，然后异或1在写回去
static main(void){
    auto i = 0;
    auto m = 0;
    for(i = 0x401060; i < 0x401075; i=i+1){
        m = byte(i);
        patch_byte(i,m ^ 1);
    }
}