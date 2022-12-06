// n 个字节的爆破
void bruteForce0(int n) {
    for (int i = 0; i < pow(123-41, n); ++i) {
        char src[n];
        int t = i;
        for (int j = 0; j < n; ++j) {
            src[j] = t % (123-41) + 41;
            t /= (123-41);
        }
        // 把 src 数组传递给要暴力破解的函数
        for (int j = 0; j < n; ++j) {
            printf("%d,", src[j]);
        }
        printf("\n");
        // enc(src, keys, out + offset);
        // int r = strncmp(out + offset, res + offset, 4);
        // if (r == 0) {
        //     printf("%s\n", src);
        //     return;
        // }

    }
    printf("error , not found\n");
}
