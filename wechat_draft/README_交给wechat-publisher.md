# 交给 wechat-publisher：生成微信公众号草稿

## 任务

把本目录中的成稿：

`wechat_draft/大连为何失落_公众号稿.md`

排版并上传到微信公众号**草稿箱**。

**只生成草稿，不执行正式发布。**

---

## 输入文件

- 稿件：`./大连为何失落_公众号稿.md`
- 封面：`./assets/cover_dalian.jpg`
- 正文图片：`./assets/` 下 7 张编号图片

稿件已经满足以下条件：

- frontmatter 含非空 `title`
- frontmatter 含真实存在的 `cover`
- 正文图片全部使用相对路径
- 无 Mermaid
- 无数学公式
- 文件为 Markdown

---

## 推荐排版参数

- 主题：`lapis`
- 代码高亮：`solarized-light`
- 不需要重新改写正文
- 不需要额外生成配图
- 外链按 wechat-publisher / wenyan-cli 默认策略转脚注即可

---

## 上传前必须检查

1. `./assets/cover_dalian.jpg` 存在且可读取。
2. 以下正文图片均存在：
   - `01_dalian_location.jpg`
   - `02_tech_org_paradigm.jpg`
   - `03_growth_stages.jpg`
   - `04_axis_vs_network.jpg`
   - `05_population_province.jpg`
   - `06_population_city.jpg`
   - `07_population_index.jpg`
3. 所有图片成功上传到微信图床后，再创建公众号草稿。
4. 如任何图片上传失败，不要静默跳过；停止并报告具体文件。
5. 成功后回传：草稿创建结果、标题、封面是否成功、正文图片数量、任何 warning。

---

## 内容边界

这是一篇已经完成论证和 review 的成稿。

接力阶段只负责：
- Markdown 排版
- 图片上传
- 链接/脚注转换
- 推送到草稿箱

不要：
- 重写核心观点
- 压缩章节
- 改变图表数据
- 自行增加新的事实判断
- 正式发布

