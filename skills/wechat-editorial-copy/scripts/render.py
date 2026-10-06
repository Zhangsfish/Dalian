#!/usr/bin/env python3
"""Render a Markdown article into a WeChat copy/paste HTML preview.

Dependencies:
  pip install mistune beautifulsoup4
"""
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import mistune
from bs4 import BeautifulSoup

P_STYLE = "margin:0 0 1.15em 0;font-size:16px;line-height:1.95;letter-spacing:0.02em;text-align:justify;word-break:break-word;"
H2_STYLE = "margin:3.2em 0 1.35em 0;font-size:22px;line-height:1.45;font-weight:700;letter-spacing:0.01em;"
H3_STYLE = "margin:2.4em 0 1em 0;font-size:18px;line-height:1.55;font-weight:700;"
BQ_STYLE = "margin:1.8em 0 1.9em 0;padding:0 0 0 1em;border-left:2px solid #b8b8b8;font-size:17px;line-height:1.9;font-weight:600;"
IMG_STYLE = "display:block;width:100%;max-width:100%;height:auto;margin:2.1em auto 0.65em auto;"
CAP_STYLE = "margin:0.45em 0 2.1em 0;font-size:12px;line-height:1.65;color:#8a8a8a;text-align:center;"


def split_frontmatter(raw: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw, flags=re.S)
    if not m:
        return {}, raw
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data, raw[m.end():]


def render(markdown_path: Path, asset_base: str) -> str:
    raw = markdown_path.read_text(encoding="utf-8")
    front, body_md = split_frontmatter(raw)
    title = front.get("title", markdown_path.stem)

    md = mistune.create_markdown(
        escape=False, plugins=["strikethrough", "table", "url"]
    )
    soup = BeautifulSoup(md(body_md), "html.parser")

    for tag in soup.find_all(True):
        name = tag.name.lower()
        if name == "p":
            tag["style"] = P_STYLE
        elif name == "h2":
            tag["style"] = H2_STYLE
        elif name == "h3":
            tag["style"] = H3_STYLE
        elif name == "blockquote":
            tag["style"] = BQ_STYLE
            for p in tag.find_all("p"):
                p["style"] = "margin:0;font-size:17px;line-height:1.9;font-weight:600;"
        elif name == "strong":
            tag["style"] = "font-weight:700;"
        elif name == "em":
            tag["style"] = "font-style:normal;"
        elif name == "hr":
            tag["style"] = "border:0;border-top:1px solid #e5e5e5;margin:3em auto;width:42px;"
        elif name in ("ul", "ol"):
            tag["style"] = "margin:1em 0 1.4em 1.3em;padding:0;"
        elif name == "li":
            tag["style"] = "margin:0.3em 0;font-size:16px;line-height:1.9;"
        elif name == "a":
            tag["style"] = "text-decoration:none;border-bottom:1px solid #c9c9c9;"
        elif name == "img":
            src = tag.get("src", "")
            if src.startswith("./assets/"):
                tag["src"] = asset_base.rstrip("/") + "/" + src.split("/")[-1]
            tag["style"] = IMG_STYLE

    for p in soup.find_all("p"):
        if p.find("img"):
            p["style"] = "margin:0;padding:0;"
            continue
        prev = p.find_previous_sibling()
        text = p.get_text(" ", strip=True)
        if prev and prev.name == "p" and prev.find("img") and text.startswith("图"):
            p["style"] = CAP_STYLE

    for h2 in soup.find_all("h2"):
        if "资料来源" in h2.get_text():
            h2["style"] = "margin:3.2em 0 1.2em 0;padding-top:1.5em;border-top:1px solid #e8e8e8;font-size:17px;line-height:1.5;font-weight:700;"
            node = h2.find_next_sibling()
            while node and getattr(node, "name", None) != "h2":
                if getattr(node, "name", None) == "ol":
                    node["style"] = "margin:0.8em 0 1em 1.3em;padding:0;"
                    for li in node.find_all("li"):
                        li["style"] = "margin:0.55em 0;font-size:12.5px;line-height:1.7;color:#777;word-break:break-all;"
                node = node.find_next_sibling()
            break

    deck = (
        '<section style="margin:0 0 2.6em 0;padding:0 0 1.6em 0;border-bottom:1px solid #ececec;">'
        '<p style="margin:0 0 0.55em 0;font-size:12px;line-height:1.5;letter-spacing:0.18em;color:#9a9a9a;">城市 · 产业 · 组织</p>'
        '<p style="margin:0;font-size:17px;line-height:1.85;font-weight:600;letter-spacing:0.01em;">'
        '这篇文章试图解释的，不是大连为什么曾经成功，而是为什么成功没有继续复利。'
        '</p></section>'
    )
    article = deck + str(soup)

    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · 微信复制版</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#f3f3f3;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:#222}}
.toolbar{{position:sticky;top:0;z-index:99;background:#fff;border-bottom:1px solid #e8e8e8;padding:12px 16px;text-align:center}}
.toolbar button{{border:1px solid #222;background:#222;color:#fff;border-radius:2px;padding:8px 16px;font-size:14px;cursor:pointer;margin:0 4px}}
.toolbar button.secondary{{background:#fff;color:#222}}
.canvas{{max-width:680px;margin:24px auto 60px;background:#fff;padding:40px 28px 56px;box-shadow:0 2px 18px rgba(0,0,0,.06)}}
.preview-title{{max-width:680px;margin:28px auto 0}}
.preview-title h1{{margin:0;font-size:28px;line-height:1.35}}
.hint{{font-size:12px;color:#999;margin-top:8px;line-height:1.6}}
</style></head><body>
<div class="toolbar">人物式克制排版 <button onclick="copyRich()">复制正文（富文本）</button><button class="secondary" onclick="selectArticle()">手动选中</button> <span id="status"></span></div>
<div class="preview-title"><h1>{html.escape(title)}</h1><div class="hint">标题不在复制区内；先填公众号标题，再复制正文。</div></div>
<main id="article" class="canvas">{article}</main>
<script>
function selectArticle(){{const r=document.createRange();r.selectNodeContents(document.getElementById('article'));const s=window.getSelection();s.removeAllRanges();s.addRange(r)}}
async function copyRich(){{const n=document.getElementById('article'),h=n.innerHTML,t=n.innerText,st=document.getElementById('status');try{{if(navigator.clipboard&&window.ClipboardItem){{await navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([h],{{type:'text/html'}}),'text/plain':new Blob([t],{{type:'text/plain'}})}})]);st.textContent='已复制'}}else throw Error()}}catch(e){{selectArticle();let ok=false;try{{ok=document.execCommand('copy')}}catch(_e){{}}st.textContent=ok?'已复制':'请手动 Ctrl/Cmd+C'}}setTimeout(()=>st.textContent='',3000)}}
</script></body></html>'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--asset-base", required=True)
    args = ap.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(args.input, args.asset_base), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()