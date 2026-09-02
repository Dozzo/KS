"""Lager artifact-versjonen av index.html.

Artifacts wrapper sida i sin egen <!doctype>...<head></head><body>, så vi
stripper wrapper-taggene og beholder title, fonter, style og innholdet.
Én kildefil, to utganger.
"""
import base64
import mimetypes
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

# Artifact-sida er en enkelt fil uten sidefiler, sa bildene ma legges inn
# direkte. index.html beholder de vanlige stiene til bilder/.
def bygg_inn(treff: re.Match) -> str:
    sti = pathlib.Path(treff.group(1))
    if not sti.is_file():
        print(f"  advarsel: fant ikke {sti}, hopper over")
        return treff.group(0)
    type_, _ = mimetypes.guess_type(sti)
    data = base64.b64encode(sti.read_bytes()).decode("ascii")
    print(f"  bygget inn {sti} ({len(data) / 1024:,.0f} kB base64)")
    return f'src="data:{type_};base64,{data}"'


src = re.sub(r'src="(bilder/[^"]+)"', bygg_inn, src)

src = re.sub(r"\n{3,}", "\n\n", src).strip() + "\n"
pathlib.Path("artifact.html").write_text(src, encoding="utf-8")
print(f"artifact.html: {len(src)} tegn")
