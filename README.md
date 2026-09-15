# Kristoffer og Synne

Bryllupsside med praktisk informasjon til gjestene. Bled Castle, Slovenia, 17. juli 2027.

Siden er tenkt som mål for QR-koden på den trykte invitasjonen, slik at invitasjonen
kan holdes kort og all praktisk info kan oppdateres fram mot bryllupet.

## Filer

| Fil | Hva det er |
| --- | --- |
| `index.html` | Kilden, og det som publiseres. Selvstendig fil, ingen byggesteg. |
| `artifact.html` | Genereres fra `index.html`. Brukes bare til forhåndsvisning. |
| `build_artifact.py` | Lager `artifact.html`. Kjør etter endringer i `index.html`. |
| `bilder/` | Bildene som brukes på siden. |
| `klargjor_bilde.py` | Skalerer og komprimerer et bilde for nett. |

Alt innhold ligger i `index.html`. Rediger den, ikke `artifact.html`.

## Bilder

Legg store bilder gjennom skriptet før de committes, ellers vokser repoet fort.
Skriptet trenger Pillow (`pip install pillow`):

    python klargjor_bilde.py ~/Desktop/bilde.jpg navn

Illustrasjonene ligger i `<figure class="illu">` i hvert avsnitt og fjerner
seg selv (`onerror`) hvis filen mangler, så avsnittet vises uten bilde.
Plasser for bilder som ennå ikke finnes: `bilder/program.jpg`, `gaver.jpg`
og `bled.jpg`.

Panoramaet i toppen er 2048 px bredt og 184 kB. Utsnittet på mobil styres av
`object-position` på `.panorama img`, satt til 58 % for å holde både
solnedgangen og oss i bildet.

## Farger

Hvit bakgrunn og sort brødtekst. To aksentfarger hentet fra invitasjonen:
dempet rosa (`--accent`) på overskrifter, lenker og Svar-feltet, og gull
(`--script-ink`) på skriftfonten og tallene. Alle verdiene ligger som
variabler øverst i `index.html`. Siden følger med vilje ikke mørkt
systemtema.

## Konvolutt

Siden åpner som en lukket konvolutt (`bilder/konvolutt.jpg`) som animeres
i lag: klaffen med seglet vipper opp, og kortet av håndlaget papir
(`kort.jpg` + `kort-maske.png`) trekkes ut. `konvolutt-uten.jpg` er
fotoet med seglet fylt inn, `konvolutt-inn.jpg` er flatt papir til
innsiden. Konvolutten vises bare første gang i økten, og aldri når noen
kommer via en direktelenke med `#`.

## Språk

Alt innhold ligger på både norsk og engelsk i `index.html`, merket
`lang="nb"` og `lang="en"` på hvert element. Klassen `en` på `<html>`
styrer hva som vises; NO/EN-knappen i menyen bytter, og valget huskes i
localStorage. Norsk er standard. Endrer du en
tekst, husk å endre begge versjonene.

## Se siden lokalt

Åpne `index.html` direkte i nettleseren, eller start en enkel server:

    python3 -m http.server 4173

## Publisering

GitHub Pages fra `main`-branchen, med `kristofferogsynne.no` som domene.

## Gjenstår

Teksten er markert med gullbrun kursiv der informasjon mangler. Søk etter
`class="pending"` i `index.html` for å finne alle stedene.
