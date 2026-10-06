# CODEX HANDOFF｜wechat-editorial-copy

## 背景

用户的公众号是无法依赖草稿箱 API 的场景，所以停止把“自动 push 草稿箱”作为主流程。

新的主流程固定为：

`Markdown → 全内联富文本 HTML → 浏览器预览 → 一键复制 → 微信公众号编辑器粘贴`

视觉方向参考用户提供的「人物」公众号长文截图：克制、编辑部感、黑白灰、大留白、图片全宽，不使用 wenyan/lapis 的彩色标题条。

## 先读

1. `skills/wechat-editorial-copy/SKILL.md`
2. `wechat_draft/大连为何失落_公众号稿.md`
3. `wechat_draft/assets/`

## 第一阶段任务

实现一个通用 renderer：

`skills/wechat-editorial-copy/scripts/render.py`

CLI 目标：

`python render.py --input <article.md> --output <copy.html> --asset-base <https-url-base>`

### renderer 必须做

- 解析并移除 YAML frontmatter；
- 标题只显示在预览工具栏/标题提示区，不进入复制正文；
- Markdown 转 HTML；
- 将 p / h2 / h3 / blockquote / strong / ul / ol / li / img / table 等转换为微信公众号可接受的简单结构；
- 所有复制区域样式写成 inline style；
- 自动识别图片后的图注段落；
- 把 `./assets/foo.jpg` 重写为 `<asset-base>/foo.jpg`；
- 来源区自动缩小到 12–13px 灰色；
- 页面顶部提供「复制正文（富文本）」按钮；
- Clipboard API 写入 `text/html` + `text/plain`；
- fallback：Range + `execCommand('copy')`。

## 默认样式

- body paragraph: 16px / line-height 1.95 / 0 首行缩进；
- h2: 22px / 700 / margin-top 约 3.2em；
- h3: 18px / 700；
- quote: 17px / 600 / 2px 灰色左线；
- image: width 100%；
- caption: 12px / #8a8a8a / center；
- source section: 12.5px / gray；
- 禁止彩色标题块、渐变、胶囊、阴影卡片。

## 当前样板文章

用：`wechat_draft/大连为何失落_公众号稿.md`

asset base：

`https://raw.githubusercontent.com/Zhangsfish/Dalian/main/wechat_draft/assets`

目标输出：

`wechat_layout/output/大连为何失落_人物式复制版.html`

## 验收

1. 打开 HTML，无控制台错误；
2. 7 张正文图都能显示；
3. 点击复制后，可以粘贴到 contenteditable 页面并保留：标题层级、粗体、引用、图片、图注、段落留白；
4. 复制区不包含文章大标题；
5. 不存在 class 依赖；
6. 不存在外部 CSS 依赖；
7. 不存在 `file://` 图片；
8. 做一张 Chromium/Playwright 长截图放到 `wechat_layout/review/`；
9. 把截图与人物参考原则人工 review；
10. 不改文章正文逻辑和数据。

## 第二阶段

等用户确认样板后，再把 `skills/wechat-editorial-copy/` 做成可迁移 skill：

- README
- SKILL.md
- scripts/render.py
- tests/fixture.md
- tests/test_render.py
- references/style.md

不要重新加入微信公众号 API 发布能力。