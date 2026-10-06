# CODEX HANDOFF｜wechat-editorial-copy v0.2

## 目标

把公众号排版流程固定成：

`Markdown → 人物式编辑部长文 → 全内联 HTML → 浏览器一键复制 → 微信公众号编辑器粘贴`

不再围绕草稿箱 API 做主流程。

## 先读

1. `skills/wechat-editorial-copy/SKILL.md`
2. `skills/wechat-editorial-copy/references/people-style.md`
3. `skills/wechat-editorial-copy/references/wechat-compat.md`
4. `wechat_draft/大连为何失落_公众号稿.md`
5. `wechat_draft/assets/`

## 用户已经确认的版式要求

### 开头

- 引言放浅灰框；
- 里面是 1–2 个完整自然段；
- 不要一句话一行；
- 如有 author/editor，右对齐显示在灰框后；
- 无信息则省略。

### 标题

- 不是彩色条；
- 18px 左右，黑色粗体；
- 自动变成 `「标题」`；
- 靠大留白形成章节感。

### 重点

- 不要彩底高亮；
- 优先用 `「重点」`；
- standalone key sentence 可以 17px 半粗体。

### 正文

- 16px；
- line-height 1.8–1.9；
- 段距约 20–26px；
- 一段 2–4 句；
- 自动合并 AI 式碎段；
- 只改换段，不改字句和逻辑。

### 图片

- 全宽；
- 不套卡片；
- 图注必须**右对齐**；
- 图注 12px 浅灰。

### 参考资料

- 最后做成固定高度滚动框；
- 浅蓝细边框；
- 12.5–13px 灰色文字；
- `overflow-y:auto` + `-webkit-overflow-scrolling:touch`；
- 如果微信过滤 overflow，必须能够自然展开，不能截断。

### 结尾

自动去掉明确的：星标、点赞、在看、关注、往期推荐、营销尾图。

## renderer

文件：`skills/wechat-editorial-copy/scripts/render.py`

CLI：

`python render.py --input <article.md> --output <copy.html> --asset-base <https-url-base>`

当前 renderer 已加入：

- lead 灰框；
- author/editor 元数据；
- 碎段合并；
- 「」标题；
- 「」重点句；
- 右对齐图注；
- 参考资料滚动框；
- promo tail 剥离；
- GitHub raw HTTPS 图片；
- Clipboard HTML + plain text。

## 当前样板

输入：`wechat_draft/大连为何失落_公众号稿.md`

asset base：

`https://raw.githubusercontent.com/Zhangsfish/Dalian/main/wechat_draft/assets`

目标输出：

`wechat_layout/output/大连为何失落_人物式复制版_v2.html`

## 你要做的第一件事

不要重写 skill。先 audit 当前 renderer 并跑起来。

步骤：

1. 建 Python venv 或使用现有环境；
2. 安装 `requirements.txt`；
3. 跑 renderer；
4. 用 Chromium/Playwright 截一张完整长图；
5. 把截图放 `wechat_layout/review/people-v2-full.png`；
6. 做一个本地 contenteditable 测试页，把富文本复制过去验证样式；
7. 人工检查以下点：
   - 引言灰框；
   - 标题是否为「」且不夸张；
   - 段落是否仍大量一句一段；
   - 图注是否右对齐；
   - 参考资料是否可滚动；
   - 是否还有彩色主题残留；
   - 是否存在 promo tail。

## 第二件事：补自动测试

至少覆盖：

- frontmatter title；
- author/editor 可选；
- lead 抽取；
- merge_short_paragraphs 不跨图片/标题；
- heading 自动加「」但不重复；
- 图片 URL 重写；
- 图注右对齐；
- sources scroll box；
- promo stripping；
- 输出 HTML 内复制区没有 class 依赖。

## 实机验收

浏览器通过不算完成。

用户会最终在微信公众号后台：

1. Ctrl+V；
2. 保存预览；
3. 手机端检查。

尤其要关注 `overflow-y:auto` 的参考资料框；社区经验表明这种结构可用，但浏览器与微信手机端可能有差异。

## 禁止事项

- 不再加入 API publish；
- 不用 lapis / orange / purple 等主题；
- 不做 PPT 卡片；
- 不改变大连文章的事实、数据或论证。

完成后提交 PR 或给出 READY_FOR_AUDIT，附：输出 HTML、长截图、测试结果和 commit SHA。