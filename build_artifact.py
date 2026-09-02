"""Lager artifact-versjonen av index.html.

Artifacts wrapper sida i sin egen <!doctype>...<head></head><body>, så vi
stripper wrapper-taggene og beholder title, fonter, style og innholdet.
Én kildefil, to utganger.
"""
import re
import pathlib

src = pathlib.Path("index.html").read_text(encoding="utf-8")

for pattern in (
    r"<!doctype[^>]*>",
    r"</?html\b[^>]*>",
    r"</?head\s*>",
    r"</?body\b[^>]*>",
    r'<meta charset[^>]*>',
    r'<meta name="viewport"[^>]*>',
):
    src = re.sub(pattern, "", src, flags=re.IGNORECASE)

src = re.sub(r"\n{3,}", "\n\n", src).strip() + "\n"
pathlib.Path("artifact.html").write_text(src, encoding="utf-8")
print(f"artifact.html: {len(src)} tegn")
