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

Legg store bilder gjennom skriptet før de committes, ellers vokser repoet fort:

    python3 klargjor_bilde.py ~/Desktop/bilde.jpg navn

Panoramaet i toppen er 2048 px bredt og 184 kB. Utsnittet på mobil styres av
`object-position` på `.panorama img`, satt til 58 % for å holde både
solnedgangen og oss i bildet.

## Farger

Paletten er sampla ut av `bilder/panorama.jpg`, ikke gjettet: bakgrunnen er
murens beige, og skriften er solnedgangens rustoransje. Alle verdiene ligger
som variabler oyerst i `index.html`.

Siden er lys i alle temaer, og folger med vilje ikke morkt systemtema — beigen
er en del av uttrykket. Hver tekstfarge er malt mot bakgrunnen den faktisk star
pa og ligger over WCAG AA. Endrer du en farge, mal den pa nytt.

## Se siden lokalt

Åpne `index.html` direkte i nettleseren, eller start en enkel server:

    python3 -m http.server 4173

## Publisering

GitHub Pages fra `main`-branchen, med `kristofferogsynne.no` som domene.

## Gjenstår

Teksten er markert med gullbrun kursiv der informasjon mangler. Søk etter
`class="pending"` i `index.html` for å finne alle stedene.
