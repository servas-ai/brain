---
id: tools.brain
owner: framework
scope: public
status: accepted
summary: brain: hält das Brain aktuell (sync), prüft es (check), klont Workspace-Zellen und diagnostiziert die Installation (doctor).
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [brain, brain sync, brain check]
---

# brain

`brain` ist das Kommandozeilenprogramm des Brains. Es liegt im `PATH` (nicht im Repo) und wird bei jedem Sitzungsstart von der Harness ausgeführt.

## Wann verwenden

| Situation | Befehl |
| --- | --- |
| Sitzungsstart, oder du brauchst den neuesten Stand | `brain sync` |
| bevor du Änderungen einreichst | `brain check` |
| dein Mensch bekommt Zugriff auf einen neuen Workspace | `brain clone-cell <git-url>` |
| irgendetwas funktioniert nicht | `brain doctor` |
| gibt es neuere Versionen von Framework oder Tools? | `brain update-check` (macht `brain sync` automatisch, einmal am Tag) |

## Was `brain sync` tut

1. Holt den Stand des Hauptrepos und jeder Zelle (`git pull --ff-only`, offline wird nur gewarnt).
2. Erzeugt lokal: `_kinder.md` je Knoten, `_workspaces.md`, `_katalog/`, `_perspektive.md` (inkl. `qdrantcli collections` und `sharepointcli whoami`, falls installiert).

Diese Dateien sind gitignored und werden nie von Hand geändert.

## Was `brain check` prüft

Pflichtfelder im Frontmatter, höchstens 40 Kinder pro Knoten, keine Instruktionsdateien (`AGENTS.md`, `CLAUDE.md`, `.claude/`, `.codex/`) in Zellen, `superseded_by` bei überholten Records. Exit 1 bei Verstößen.

## Installation und Quelle

Installation: siehe `README.md` im Repo-Root, Abschnitt „Setup für die Harness“. Quellcode: https://github.com/servas-ai/brain-cli

Fehlerbilder: `debugging/_kinder.md`
