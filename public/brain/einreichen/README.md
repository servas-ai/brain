---
id: public.brain.einreichen
owner: framework
scope: public
status: accepted
summary: Pflichtablauf, bevor eine Änderung den eigenen Rechner verlässt: Sichtbarkeits-Review mit dem Menschen in der Harness, dann Branch und Pull Request mit derselben Tabelle.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [einreichen, Pull Request, PR, Review, Freigabe, Sichtbarkeit]
---

# Änderungen einreichen: erst der Mensch, dann der Pull Request

Das Review findet **in der Harness statt, bevor irgendetwas gepusht wird**. Was einmal gepusht ist, bleibt in der Git-Historie, auch wenn der PR später geschlossen wird. Deshalb entscheidet der Mensch vorher, wer welche neue Information sehen wird.

## 1. Sichtbarkeit ermitteln (nicht raten)

Für jedes betroffene Repo (Hauptrepo, Workspace, `personal`) die tatsächlichen Leser abfragen:

```bash
gh api "repos/<owner>/<repo>/collaborators?affiliation=all&per_page=100" --jq '.[].login'
gh repo view <owner>/<repo> --json visibility --jq .visibility
```

- Hauptrepo und Workspaces: Ergebnis ist die Liste der GitHub-Accounts, die die Datei nach dem Merge lesen können. Bei `PUBLIC`: „jeder im Internet“ – dann sofort stoppen und den Menschen fragen.
- `personal/` (`brain-personal`): muss `PRIVATE` sein und darf nur den Inhaber listen. Sonst stoppen.
- Gibt `collaborators` einen Fehler (keine Rechte zum Auflisten): schreib „Leserkreis unbekannt“ – nie eine Annahme.

## 2. Dem Menschen zeigen und auf ein ausdrückliches Ja warten

Zeig genau diese Tabelle, eine Zeile pro Datei:

| Datei | neu / geändert / gelöscht | Was steht drin (ein Satz, konkret) | Sichtbar für |
| --- | --- | --- | --- |
| `workspaces/ws-kunde-a/wissen/lieferfristen/README.md` | neu | Standard-Lieferfrist für Kunde A und Ausnahmen | anna, ben, chris (3 Personen) |

Darunter: „Soll ich das so einreichen? (ja / nein / ändern)“. Ohne ausdrückliches **Ja** nichts pushen. Nennt der Mensch eine Datei, die nicht alle sehen sollen: verschieben (siehe Wohin-Tabelle in `AGENTS.md`) und die Tabelle neu zeigen.

## 3. Einreichen

- `personal/`: direkt committen und pushen (privat, kein Review nötig).
- Alles Geteilte: eigener Branch `<github-account>/<kurzer-slug>`, Commit-Message ohne Kundennamen, Pull Request mit dieser Beschreibung:

```markdown
## Was neu ist
<Tabelle aus Schritt 2, unverändert>

## Freigabe
Sichtbarkeit am <Datum> mit <Mensch> in der Harness geprüft und bestätigt.
```

Die Beschreibung enthält nur, was in der Tabelle steht – keine eigenen Annahmen über Leserkreise.

## 4. Mergen

Den Pull Request merged ein Mensch (oder später der Bot) auf GitHub. Danach holen alle Beteiligten den neuen Stand beim nächsten `brain sync`.
