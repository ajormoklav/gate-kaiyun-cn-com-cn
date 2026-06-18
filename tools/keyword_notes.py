from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

SAMPLE_URL = "https://www.gate-kaiyun-cn.com.cn"
KEYWORD = "开云"


@dataclass
class KeywordNote:
    keyword: str
    url: str
    title: str
    content: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def summary(self, max_len: int = 40) -> str:
        summary_content = (self.content[:max_len] + "...") if len(self.content) > max_len else self.content
        return f"[{self.keyword}] {self.title}: {summary_content}"

    def to_formatted_block(self) -> str:
        tag_line = f"标签: {', '.join(self.tags)}" if self.tags else "标签: 无"
        lines = [
            f"关键词: {self.keyword}",
            f"标题: {self.title}",
            f"URL: {self.url}",
            f"时间: {self.created_at}",
            tag_line,
            f"内容:",
            self.content,
            "-" * 50
        ]
        return "\n".join(lines)


def create_demo_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword=KEYWORD,
            url=f"{SAMPLE_URL}/article/1",
            title="开云平台入门指南",
            content="本文介绍如何使用开云平台进行快速项目搭建，适合初学者参考。",
            tags=["入门", "指南", "开云"]
        ),
        KeywordNote(
            keyword=KEYWORD,
            url=f"{SAMPLE_URL}/article/2",
            title="开云高级配置详解",
            content="深入讲解开云平台的配置项与调优技巧，帮助用户发挥最大效能。",
            tags=["高级", "配置"]
        ),
        KeywordNote(
            keyword=KEYWORD,
            url=f"{SAMPLE_URL}/blog/3",
            title="开云社区最佳实践",
            content="收集自开云社区的用户经验与案例，涵盖多个行业场景。",
            tags=["社区", "实践", "案例"]
        )
    ]


def format_notes_to_text(notes: List[KeywordNote]) -> str:
    header = f"关键词笔记列表 — 关键词: {KEYWORD} (来源: {SAMPLE_URL})\n"
    header += "=" * 60 + "\n"
    body = "\n\n".join(note.to_formatted_block() for note in notes)
    return header + body


def format_notes_to_html(notes: List[KeywordNote]) -> str:
    html_parts = [
        "<!DOCTYPE html>",
        "<html><head><meta charset='utf-8'><title>关键词笔记</title></head><body>",
        f"<h1>关键词笔记 — {KEYWORD}</h1>",
        f"<p>来源: <a href='{SAMPLE_URL}'>{SAMPLE_URL}</a></p>",
        "<hr>"
    ]
    for note in notes:
        tags_html = "".join(f"<span style='background:#eef;padding:2px 6px;margin:2px;'>{tag}</span>"
                            for tag in note.tags) if note.tags else "无"
        block = f"""
        <div style='border:1px solid #ccc;padding:15px;margin:10px 0;'>
            <h3>{note.title}</h3>
            <p><strong>关键词:</strong> {note.keyword}</p>
            <p><strong>URL:</strong> <a href='{note.url}'>{note.url}</a></p>
            <p><strong>时间:</strong> {note.created_at}</p>
            <p><strong>标签:</strong> {tags_html}</p>
            <p><strong>内容:</strong><br>{note.content}</p>
        </div>
        """
        html_parts.append(block)
    html_parts.append("</body></html>")
    return "\n".join(html_parts)


def main():
    notes = create_demo_notes()
    print("【文本格式输出】")
    print(format_notes_to_text(notes))
    print("\n【HTML格式输出】（片段）")
    html_out = format_notes_to_html(notes)
    print(html_out[:500] + "\n... (截断)")
    print(f"\n共生成 {len(notes)} 条笔记。")


if __name__ == "__main__":
    main()