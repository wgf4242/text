// .vuepress/config.js

module.exports = {
  theme: 'reco',
  title: "wgf4242's Blog",
  description: 'Just playing around',
  markdown: {
    lineNumbers: true,
  },
  themeConfig: {
    base: '/text_del/', // 比如你的仓库是text_del
    displayAllHeaders: true, // 默认值：false
    sidebar: 'auto',
    /**
     * 右侧导航条
     * text - 显示字段
     * link - 链接：注意前后带 / 符号
     */
    nav: [
      {
        text: '主页',
        link: '/home/',
      },
      /**
       * 多级菜单
       * 开头 text 为一级标题
       * 数组内 text 为二级标题
       * link 为链接，注意带 /
       */
      {
        text: '文章',
        items: [
          {
            text: '技术',
            link: '/article/technology/',
          },
          {
            text: '随笔',
            link: '/article/essay/',
          },
          {
            text: '其他',
            link: '/article/other/',
          },
        ],
      },
      {
        text: '关于',
        link: '/about/',
        // link: '/about/'
      },
      // 链接到网站
      {
        text: 'Github',
        link: 'https://www.github.com/wgf4242',
      },
    ],
  },
};
