# wechat-editorial-copy

把已经写好的 Markdown 长文排成可直接复制进微信公众号编辑器的富文本 HTML。

默认风格：用户指定的《人物》式克制编辑部长文。

## 固定工作流

`Markdown → 结构清理 → 全内联 HTML → 浏览器复制富文本 → 微信公众号粘贴 → 手机预览`

不依赖草稿箱 API。

## 关键文件

- `SKILL.md`：Agent 行为与排版规范
- `CODEX_HANDOFF.md`：Codex 下一步实现/验收任务
- `scripts/render.py`：当前 renderer
- `references/people-style.md`：从用户提供《人物》实文截图提取的版式规则
- `references/wechat-compat.md`：微信复制/inline CSS/滚动框兼容经验

## 样板

- 稿件：`wechat_draft/大连为何失落_公众号稿.md`
- 图片：`wechat_draft/assets/`

## 当前视觉规范

- 引言：浅灰框
- 标题：`「标题」` + 黑色粗体
- 正文：16px / 1.86 行高 / 20–26px 段距
- 自动合并 AI 式碎段
- 重点：`「重点」`，不用彩底
- 图片：全宽
- 图注：右对齐浅灰小字
- 参考资料：固定高度滚动框
- 无关注/星标/点赞尾巴

## 下一步

Codex 不要重写规范；先按 `CODEX_HANDOFF.md` audit + 运行 renderer，生成 HTML、长截图、测试结果后交审。