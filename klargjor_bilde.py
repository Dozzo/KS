#!/usr/bin/env python3
"""Skalerer og komprimerer et bilde for nett, og legger det i bilder/.

    python klargjor_bilde.py ~/Desktop/kleskode.png kleskode

Bruker Pillow (pip install pillow), sa det virker pa bade Mac og Windows.
Originalen rores ikke. Gjestene apner siden pa mobil, ofte pa utenlandsk
nett, sa malet er under ca. 400 kB.
"""
import pathlib
import sys

from PIL import Image

BREDDE = 2000
KVALITET = 62


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    kilde = pathlib.Path(sys.argv[1]).expanduser()
    if not kilde.is_file():
        print(f"Fant ikke filen: {kilde}")
        return 1

    navn = sys.argv[2] if len(sys.argv) > 2 else kilde.stem
    ut = pathlib.Path("bilder") / f"{navn}.jpg"
    ut.parent.mkdir(exist_ok=True)

    with Image.open(kilde) as bilde:
        # PNG med gjennomsiktighet legges pa hvit bunn, som siden.
        if bilde.mode in ("RGBA", "LA", "P"):
            bunn = Image.new("RGB", bilde.size, "white")
            bunn.paste(bilde.convert("RGBA"), mask=bilde.convert("RGBA").split()[-1])
            bilde = bunn
        else:
            bilde = bilde.convert("RGB")
        bilde.thumbnail((BREDDE, BREDDE), Image.LANCZOS)
        bilde.save(ut, "JPEG", quality=KVALITET, optimize=True, progressive=True)
        piksler = f"{bilde.width} {bilde.height}"

    inn_kb = kilde.stat().st_size / 1024
    ut_kb = ut.stat().st_size / 1024
    print(f"{kilde.name}  {inn_kb:,.0f} kB")
    print(f"-> {ut}  {ut_kb:,.0f} kB  ({piksler} px)")
    if ut_kb > 400:
        print("Over 400 kB. Sett KVALITET lavere eller BREDDE ned til 1600.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
