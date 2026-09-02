#!/usr/bin/env python3
"""Skalerer og komprimerer et bilde for nett, og legger det i bilder/.

    python3 klargjor_bilde.py ~/Desktop/panorama.jpg panorama

Bruker sips, som folger med macOS. Originalen rores ikke. Gjestene apner
siden pa mobil, ofte pa utenlandsk nett, sa malet er under ca. 400 kB.
"""
import pathlib
import subprocess
import sys

BREDDE = 2000
KVALITET = 62


def kjor(*args: str) -> None:
    subprocess.run(args, check=True, capture_output=True)


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

    kjor("sips", "-Z", str(BREDDE),
         "-s", "format", "jpeg",
         "-s", "formatOptions", str(KVALITET),
         str(kilde), "--out", str(ut))

    inn_kb = kilde.stat().st_size / 1024
    ut_kb = ut.stat().st_size / 1024
    mal = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(ut)],
                         check=True, capture_output=True, text=True).stdout
    piksler = " ".join(linje.split(": ")[-1] for linje in mal.strip().splitlines()[1:])

    print(f"{kilde.name}  {inn_kb:,.0f} kB")
    print(f"-> {ut}  {ut_kb:,.0f} kB  ({piksler} px)")
    if ut_kb > 400:
        print("Over 400 kB. Sett KVALITET lavere eller BREDDE ned til 1600.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
