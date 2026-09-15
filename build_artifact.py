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
def data_uri(sti: pathlib.Path) -> str | None:
    if not sti.is_file():
        print(f"  advarsel: fant ikke {sti}, hopper over")
        return None
    type_, _ = mimetypes.guess_type(sti)
    data = base64.b64encode(sti.read_bytes()).decode("ascii")
    print(f"  bygget inn {sti} ({len(data) / 1024:,.0f} kB base64)")
    return f"data:{type_};base64,{data}"


def bygg_inn_src(treff: re.Match) -> str:
    uri = data_uri(pathlib.Path(treff.group(1)))
    return f'src="{uri}"' if uri else treff.group(0)


def bygg_inn_url(treff: re.Match) -> str:
    uri = data_uri(pathlib.Path(treff.group(1)))
    return f"url({uri})" if uri else treff.group(0)


src = re.sub(r'src="(bilder/[^"]+)"', bygg_inn_src, src)
src = re.sub(r"url\((bilder/[^)]+)\)", bygg_inn_url, src)   # bakgrunner og masker i CSS

src = re.sub(r"\n{3,}", "\n\n", src).strip() + "\n"
pathlib.Path("artifact.html").write_text(src, encoding="utf-8", newline="\n")
print(f"artifact.html: {len(src)} tegn")
