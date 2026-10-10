---
id: public.brain.konventionen
owner: framework
scope: public
status: accepted
summary: Wie ein Knoten aufgebaut ist, welche Felder Pflicht sind und wie Indizes, Katalog und Zellen entstehen.
evidence: [Brain-Template v0.3]
review_by: 2027-10-10
---

# Konventionen des Brains

## Knoten

Jeder Ordner mit einer `README.md` ist ein Knoten. Die `README.md` beginnt mit Frontmatter und beschreibt in zwei bis drei Sätzen, worum es geht. Aussagen, keine Fragen.

```
<knoten>/
  README.md          Record des Knotens
  _kinder.md         lokal erzeugt: Liste der Kinder, je ein Satz (aus deren summary)
  <unterknoten>/     beliebig tief, gleicher Aufbau
  faq/               Fragen        (je Frage ein Unterordner mit README.md)
  debugging/         Fehlerbilder  (Symptom, Ursache, Fix, Prüfen)
  runbooks/          Abläufe       (Voraussetzungen, Schritte, fertig wenn …)
```

`faq/`, `debugging/`, `runbooks/` gibt es nur, wenn sie Einträge haben. Ein Eintrag steht beim Knoten, um den es geht. Ordnernamen: Kleinbuchstaben, `-`, nach dem Problem benannt, nicht nach Ticket oder Datum.

## Frontmatter

```yaml
---
id: tools.sharepoint.debugging.403-bei-bibliothek   # aus dem Pfad, / wird ., bleibt stabil
owner: <github-account oder rolle>
scope: public | workspace/<slug> | personal
status: accepted | superseded
summary: <ein Satz: was steht hier, so dass man ohne Öffnen entscheiden kann>
evidence: [<woher das Wissen stammt, mit Datum>]
review_by: <YYYY-MM-DD>
keys: [<feste Schlüssel: Projektnummer, Norm, Tool, Kürzel, Alias>]   # optional, speist _katalog/
requires: [<ids>]                                                    # optional
superseded_by: <id>                                                  # nur bei status: superseded
---
```

- `summary` ist Pflicht und das Wichtigste: Aus ihm entsteht die Zeile in `_kinder.md` des Elternknotens. Schreib ihn so, dass eine Harness entscheiden kann, ob sie hineinspringt.
- `keys` nur für feste, exakte Schlüssel (z. B. `25-018`, `DIN 1988-300`, `LINEAR`, `Sonnenhang`).
- Höchstens 40 Kinder pro Knoten; darüber nach Sachkriterium teilen (Jahr, Gewerk, Art), nie „sonstiges“.

## Lokal erzeugt (nie committen, nie von Hand ändern)

| Datei | Inhalt |
| --- | --- |
| `_perspektive.md` | was der Login dieses Menschen sieht |
| `_workspaces.md` | sichtbare Workspaces mit Status, Phase, Satz |
| `_katalog/` | Schlüssel → Knoten, aus allen `keys` der sichtbaren Knoten |
| `**/_kinder.md` | Kinderliste je Knoten, aus den `summary` der Kinder |

## Zellen

Workspaces und `personal/` sind eigene Git-Repos, die lokal an ihren Platz geklont werden. Jede Workspace-Zelle hat eine `.cell.yml` (Vorlage `templates/cell.yml`). Zellen enthalten keine `AGENTS.md`, `CLAUDE.md`, `.claude/` oder `.codex/`.

## Verweise

Auf andere Knoten per `id` in Backticks. Richtung: `personal` → `workspaces` → `public` → `tools` → `systeme`. Ein Knoten im Hauptrepo nennt nie einen Workspace; ein Workspace nennt nie `personal`.

## Überholtes

Nicht löschen, sondern `status: superseded` und `superseded_by`. Ausnahme: personenbezogene Daten werden gelöscht.
