---
id: tools.qdrantcli
owner: framework
scope: public
status: accepted
summary: qdrantcli: Vektorsuche in der Qdrant-Instanz der Firma mit dem eigenen Token des Menschen – Collections, Payload-Filter, Textsuche.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [qdrantcli, Qdrant, Vektorsuche]
---

# qdrantcli

Eigenständiges Programm für die Vektorsuche der Firma. Es arbeitet mit dem **persönlichen Qdrant-Token deines Menschen**: Welche Collections er sieht, entscheidet der Token. `brain sync` schreibt die sichtbaren Collections in `_perspektive.md`.

## Wann verwenden

Wenn die Landkarte (Katalog, Trampoline) und die eigenen Fundstellen in `personal/fundstellen/` nichts haben. Treffer sind Hinweise auf Dokumente, nicht die Wahrheit: maßgeblich ist das Dokument im Archiv (`tools.sharepointcli`).

## Befehle

| Befehl | Wofür |
| --- | --- |
| `qdrantcli login --url <url>` | einmalig: URL und persönlichen Token speichern (Token fragt das Programm verdeckt ab) |
| `qdrantcli whoami` | Verbindung und sichtbare Collections |
| `qdrantcli collections` | Collections mit Punktanzahl |
| `qdrantcli info <collection>` | Payload-Felder, nach denen man filtern kann |
| `qdrantcli scroll <collection> --filter projekt=25-018 --limit 10` | Punkte nach Payload filtern |
| `qdrantcli search <collection> "<frage>" --filter <feld>=<wert>` | Textsuche (Embedding-Einstellung siehe `systeme.qdrant`) |

Alle Befehle können `--json`.

## Gut suchen

1. Erst `info`, dann mit Payload-Filtern eingrenzen (Projekt, Bereich, Gewerk) – Filter schlagen freie Textsuche.
2. Kurze, fachliche Abfragen; Projektnummern und Ortsnamen gehören in den Filter, nicht in den Text.
3. Hat eine Abfrage getragen: Fundstelle in `personal/fundstellen/` schreiben (Vorlage `templates/fundstelle.md`) – nur der Weg, keine Inhalte.

## Meldungen richtig lesen

- **403 / Kein Zugriff:** Der Token deines Menschen sieht diese Collection nicht. Kein Fehler.
- **401:** Token abgelaufen oder falsch – `qdrantcli login` erneut, neuen Token bei der Qdrant-Verwaltung der Firma holen (siehe `systeme.qdrant`).

## Installation und Quelle

Installation: `README.md` im Repo-Root, „Setup für die Harness“. Quellcode: https://github.com/servas-ai/qdrantcli

Fehlerbilder: `debugging/_kinder.md`
