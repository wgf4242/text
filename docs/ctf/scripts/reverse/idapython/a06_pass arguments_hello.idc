// 在控制台会显示 argv 信息
// D:\CTF\IDA_Pro_v8.3_Portable\ida64.exe -S"hello.idc arg1 arg2 arg3" wizmo32.exe.idb
// 手动再次显示
// IDC>ARGV

#include <idc.idc>

static main()
{
  auto i;
  msg("'%s' was passed %d argument(s)\n", ARGV[0], ARGV.count);
  for (i=1;i<ARGV.count;i++)
  {
    msg("  ARGV[%d]=%s\n", i, ARGV[i]);
  }
  return 0;
}