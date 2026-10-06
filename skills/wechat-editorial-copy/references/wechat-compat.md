# 微信复制与排版兼容经验

## 已确认的稳定原则

1. 微信公众号粘贴会过滤外部 CSS/class，因此正文样式应内联。
2. 使用复制按钮把 `text/html` + `text/plain` 一起写入剪贴板，比手工框选复制更稳定。
3. 网络图片粘贴后不一定自动转存，必须做发布前预览；正文结构不能依赖图片一定自动上传。
4. 普通正文优先使用 p/section/strong/img/ol/ul/li 等简单标签。
5. 复杂布局不要依赖 Grid/Flex；需要复杂结构时直接做成图片。

## 固定高度滚动框

微信公众号文章中可以实现固定区域滚动，社区实测常用：

- 明确 height / max-height；
- `overflow-y:auto` 或 `scroll`；
- `-webkit-overflow-scrolling:touch`；

但浏览器预览与手机实测可能略有差异，因此参考资料滚动框必须进入手机预览验收。

降级原则：

> 如果 overflow 被过滤，参考资料应该展开显示，而不是被截断或隐藏。

因此不要使用 `overflow:hidden` 作为关键逻辑。

## 移动端参数参考

多家公众号排版实践的常见舒适区间：

- 正文：15–16px；
- 小标题：17–18px；
- 注释：12–13px；
- 行高：1.75–1.9；
- 字间距：约 1px；
- 段间距：15–26px；
- 不首行缩进；
- 颜色尽量控制在 1–3 种。

本 skill 因用户指定《人物》风格，默认取：16px / 1.86 / 约24px段距。

## 参考

- 文颜：Markdown 转公众号富文本，一键复制；其核心同样依赖 inline style。
  https://github.com/caol64/wenyan
- W3CTool 微信排版器：按钮复制富文本 + 全内联样式。
  https://w3ctool.com/tools/wechat-format
- 腾讯云社区：样式内联化 + Clipboard HTML 富文本复制。
  https://developer.tencent.com/article/2436347
- V2EX：剪贴板同时保存 text/plain 与 text/html 的说明。
  https://global.v2ex.co/t/1136141
- 腾讯云社区：固定区域 overflow-y:auto 的公众号推文滚动实战。
  https://developer.tencent.com/article/1775684