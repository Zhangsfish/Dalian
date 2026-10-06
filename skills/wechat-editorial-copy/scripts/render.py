#!/usr/bin/env python3
"""Render a Markdown article into a People-style WeChat copy/paste HTML preview.

Dependencies:
  pip install mistune beautifulsoup4
"""
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import mistune
from bs4 import BeautifulSoup, NavigableString, Tag

BODY_STYLE = (
    "margin:0 0 24px 0;font-size:16px;line-height:1.86;"
    "letter-spacing:0.025em;text-align:justify;word-break:break-word;color:#262626;"
)
HEADING_STYLE = (
    "margin:58px 0 30px 0;font-size:18px;line-height:1.55;"
    "font-weight:700;letter-spacing:0.01em;color:#151515;"
)
SUBHEADING_STYLE = (
    "margin:46px 0 24px 0;font-size:17px;line-height:1.55;"
    "font-weight:700;color:#1d1d1d;"
)
KEY_STYLE = (
    "margin:30px 0 32px 0;font-size:17px;line-height:1.85;"
    "font-weight:650;color:#202020;"
)
IMG_STYLE = "display:block;width:100%;max-width:100%;height:auto;margin:32px auto 0 auto;"
CAP_STYLE = (
    "margin:5px 0 32px 0;font-size:12px;line-height:1.55;"
    "color:#929292;text-align:right;"
)
LEAD_STYLE = (
    "margin:0 0 54px 0;padding:24px 24px 22px 24px;"
    "background:#f3f3f3;border:0;"
)
LEAD_P_STYLE = (
    "margin:0 0 18px 0;font-size:16px;line-height:1.95;"
    "letter-spacing:0.02em;text-align:justify;color:#343434;"
)
BYLINE_STYLE = (
    "margin:0 0 64px 0;text-align:right;font-size:14px;"
    "line-height:1.85;color:#262626;"
)
SOURCE_BOX_STYLE = (
    "height:300px;overflow-y:auto;-webkit-overflow-scrolling:touch;"
    "margin:58px 0 16px 0;padding:12px 14px 14px 14px;"
    "border:1px solid #a9d6ea;background:#fff;"
)
SOURCE_TITLE_STYLE = (
    "margin:0 0 12px 0;font-size:14px;line-height:1.6;"
    "font-weight:700;color:#858585;"
)
SOURCE_LI_STYLE = (
    "margin:0 0 9px 0;font-size:12.5px;line-height:1.72;"
    "color:#888;word-break:break-all;"
)

PROMO_MARKERS = (
    "亲爱的读者", "星标", "点赞", "在看", "关注我们", "关注公众号",
    "往期推荐", "欢迎关注", "转发"
)


def split_frontmatter(raw: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw, flags=re.S)
    if not m:
        return {}, raw
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data, raw[m.end():]


def bracket(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    if text.startswith("「") and text.endswith("」"):
        return text
    return f"「{text}」"


def plain_len(tag: Tag) -> int:
    return len(re.sub(r"\s+", "", tag.get_text("", strip=True)))


def is_plain_paragraph(tag: Tag | None) -> bool:
    if not tag or tag.name != "p":
        return False
    if tag.find("img"):
        return False
    text = tag.get_text("", strip=True)
    if not text:
        return False
    if text.startswith("图") and len(text) < 120:
        return False
    return True


def strip_promo_tail(soup: BeautifulSoup) -> None:
    nodes = [n for n in soup.children if isinstance(n, Tag)]
    if not nodes:
        return
    threshold = int(len(nodes) * 0.70)
    for i, node in enumerate(nodes):
        if i < threshold:
            continue
        text = node.get_text(" ", strip=True)
        if len(text) <= 240 and any(m in text for m in PROMO_MARKERS):
            for doomed in nodes[i:]:
                doomed.decompose()
            return


def extract_lead(soup: BeautifulSoup) -> Tag | None:
    lead = soup.new_tag("section")
    lead["style"] = LEAD_STYLE
    count = 0

    # First top-level blockquote is treated as the article deck.
    first_bq = soup.find("blockquote", recursive=False)
    first_h = soup.find(["h2", "h3"], recursive=False)
    if first_bq and (not first_h or list(soup.children).index(first_bq) < list(soup.children).index(first_h)):
        text = first_bq.get_text(" ", strip=True)
        if text:
            p = soup.new_tag("p")
            p["style"] = LEAD_P_STYLE
            p.string = text
            lead.append(p)
            count += 1
        first_bq.decompose()

    # Hide the literal "引子" heading and bring the first two prose blocks into the deck.
    intro = None
    for h in soup.find_all(["h2", "h3"], recursive=False):
        if "引子" in h.get_text():
            intro = h
            break
    if intro:
        node = intro.find_next_sibling()
        grabbed = 0
        while node and grabbed < 2:
            nxt = node.find_next_sibling()
            if isinstance(node, Tag) and node.name == "p" and is_plain_paragraph(node):
                p = soup.new_tag("p")
                p["style"] = LEAD_P_STYLE
                for child in list(node.contents):
                    p.append(child)
                lead.append(p)
                node.decompose()
                count += 1
                grabbed += 1
            elif isinstance(node, Tag) and node.name in ("h2", "h3", "hr"):
                break
            node = nxt
        intro.decompose()

    if count == 0:
        return None
    ps = lead.find_all("p", recursive=False)
    if ps:
        ps[-1]["style"] = ps[-1]["style"].replace("margin:0 0 18px 0", "margin:0")
    return lead


def merge_short_paragraphs(soup: BeautifulSoup, min_chars: int = 90, max_chars: int = 190) -> None:
    node = next((n for n in soup.children if isinstance(n, Tag)), None)
    while node:
        nxt = node.find_next_sibling()
        if not is_plain_paragraph(node):
            node = nxt
            continue

        parts = 1
        while plain_len(node) < min_chars and parts < 4:
            nxt = node.find_next_sibling()
            if not is_plain_paragraph(nxt):
                break
            if plain_len(node) + plain_len(nxt) > max_chars:
                break
            for child in list(nxt.contents):
                node.append(child)
            nxt.decompose()
            parts += 1

        node = node.find_next_sibling()


def make_byline(soup: BeautifulSoup, front: dict[str, str]) -> Tag | None:
    author = front.get("author", "").strip()
    editor = front.get("editor", "").strip()
    if not author and not editor:
        return None
    sec = soup.new_tag("section")
    sec["style"] = BYLINE_STYLE
    if author:
        p = soup.new_tag("p")
        p["style"] = "margin:0;"
        p.append(BeautifulSoup("<strong style=\"font-weight:700;\">文｜</strong>", "html.parser"))
        p.append(NavigableString(author))
        sec.append(p)
    if editor:
        p = soup.new_tag("p")
        p["style"] = "margin:0;"
        p.append(BeautifulSoup("<strong style=\"font-weight:700;\">编辑｜</strong>", "html.parser"))
        p.append(NavigableString(editor))
        sec.append(p)
    return sec


def style_headings(soup: BeautifulSoup) -> None:
    for h in list(soup.find_all(["h2", "h3"])):
        text = h.get_text(" ", strip=True)
        if "资料来源" in text or "参考资料" in text:
            continue
        p = soup.new_tag("p")
        p["style"] = HEADING_STYLE if h.name == "h2" else SUBHEADING_STYLE
        p.string = bracket(text)
        h.replace_with(p)


def style_highlights(soup: BeautifulSoup) -> None:
    # Remaining blockquotes become standalone bracketed emphasis.
    for bq in list(soup.find_all("blockquote")):
        text = bq.get_text(" ", strip=True)
        p = soup.new_tag("p")
        p["style"] = KEY_STYLE
        p.string = bracket(text)
        bq.replace_with(p)

    # Inline bold becomes bracket emphasis instead of colorful/highlighter style.
    for st in soup.find_all("strong"):
        if st.find_parent(["h2", "h3"]):
            continue
        text = st.get_text("", strip=True)
        if text and not (text.startswith("「") and text.endswith("」")):
            st.clear()
            st.append(NavigableString(bracket(text)))
        st["style"] = "font-weight:500;color:#242424;"


def style_images_and_captions(soup: BeautifulSoup, asset_base: str) -> None:
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src.startswith("./assets/"):
            img["src"] = asset_base.rstrip("/") + "/" + src.split("/")[-1]
        img["style"] = IMG_STYLE
        parent = img.parent
        if parent and parent.name == "p":
            parent["style"] = "margin:0;padding:0;"

    for p in soup.find_all("p"):
        if p.find("img"):
            continue
        prev = p.find_previous_sibling()
        text = p.get_text(" ", strip=True)
        if prev and prev.name == "p" and prev.find("img") and text.startswith("图"):
            p["style"] = CAP_STYLE
            for em in p.find_all("em"):
                em.unwrap()


def build_source_box(soup: BeautifulSoup) -> None:
    heading = None
    for h in soup.find_all(["h2", "h3"]):
        text = h.get_text(" ", strip=True)
        if "资料来源" in text or "参考资料" in text:
            heading = h
            break
    if not heading:
        return

    box = soup.new_tag("section")
    box["style"] = SOURCE_BOX_STYLE
    title = soup.new_tag("p")
    title["style"] = SOURCE_TITLE_STYLE
    title.string = "参考资料："
    box.append(title)

    node = heading.find_next_sibling()
    heading.insert_before(box)
    heading.decompose()
    while node:
        nxt = node.find_next_sibling()
        box.append(node.extract())
        node = nxt

    for ol in box.find_all(["ol", "ul"]):
        ol["style"] = "margin:0 0 0 1.25em;padding:0;"
    for li in box.find_all("li"):
        li["style"] = SOURCE_LI_STYLE
    for a in box.find_all("a"):
        a["style"] = "color:#888;text-decoration:none;word-break:break-all;"


def apply_base_styles(soup: BeautifulSoup) -> None:
    for p in soup.find_all("p"):
        if "style" not in p.attrs:
            p["style"] = BODY_STYLE
    for em in soup.find_all("em"):
        em["style"] = "font-style:normal;"
    for a in soup.find_all("a"):
        if "style" not in a.attrs:
            a["style"] = "color:inherit;text-decoration:none;border-bottom:1px solid #d7d7d7;"
    for hr in soup.find_all("hr"):
        hr.decompose()
    for ul in soup.find_all("ul"):
        if "style" not in ul.attrs:
            ul["style"] = "margin:0 0 24px 1.25em;padding:0;"
    for ol in soup.find_all("ol"):
        if "style" not in ol.attrs:
            ol["style"] = "margin:0 0 24px 1.25em;padding:0;"
    for li in soup.find_all("li"):
        if "style" not in li.attrs:
            li["style"] = "margin:0 0 8px 0;font-size:16px;line-height:1.86;color:#262626;"


def render(markdown_path: Path, asset_base: str) -> str:
    raw = markdown_path.read_text(encoding="utf-8")
    front, body_md = split_frontmatter(raw)
    title = front.get("title", markdown_path.stem)

    md = mistune.create_markdown(
        escape=False, plugins=["strikethrough", "table", "url"]
    )
    soup = BeautifulSoup(md(body_md), "html.parser")

    strip_promo_tail(soup)
    lead = extract_lead(soup)
    merge_short_paragraphs(soup)
    build_source_box(soup)
    style_headings(soup)
    style_highlights(soup)
    style_images_and_captions(soup, asset_base)
    apply_base_styles(soup)

    article_parts: list[str] = []
    if lead:
        article_parts.append(str(lead))
    byline = make_byline(soup, front)
    if byline:
        article_parts.append(str(byline))
    article_parts.append(str(soup))
    article = "".join(article_parts)

    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · 微信复制版</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#f3f3f3;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:#262626}}
.toolbar{{position:sticky;top:0;z-index:99;background:#fff;border-bottom:1px solid #e8e8e8;padding:12px 16px;text-align:center}}
.toolbar button{{border:1px solid #222;background:#222;color:#fff;border-radius:2px;padding:8px 16px;font-size:14px;cursor:pointer;margin:0 4px}}
.toolbar button.secondary{{background:#fff;color:#222}}
.canvas{{max-width:677px;margin:24px auto 60px;background:#fff;padding:38px 30px 56px;box-shadow:0 2px 18px rgba(0,0,0,.05)}}
.preview-title{{max-width:677px;margin:28px auto 0}}
.preview-title h1{{margin:0;font-size:28px;line-height:1.35;color:#111}}
.hint{{font-size:12px;color:#999;margin-top:8px;line-height:1.6}}
#status{{font-size:12px;color:#777;margin-left:8px}}
</style></head><body>
<div class="toolbar">人物式编辑排版 <button onclick="copyRich()">复制正文（富文本）</button><button class="secondary" onclick="selectArticle()">手动选中</button><span id="status"></span></div>
<div class="preview-title"><h1>{html.escape(title)}</h1><div class="hint">标题不在复制区内；微信标题栏单独填写。复制后务必发一次手机预览。</div></div>
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
