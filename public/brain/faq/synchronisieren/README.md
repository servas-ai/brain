---
id: public.brain.faq.synchronisieren
owner: framework
scope: public
status: accepted
summary: Wie das Synchronisieren funktioniert: GitHub ist die Quelle, brain sync holt Hauptrepo und Zellen und erzeugt die Übersichten lokal.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [sync, brain sync, aktualisieren, offline, Stand]
---

# Wie funktioniert das Synchronisieren?

- **GitHub ist die einzige Quelle.** Was auf `main` des Firmen-Repos und der Workspace-Repos steht, ist der gültige Stand.
- **`brain sync`** (bei Claude Code automatisch bei jedem Sitzungsstart) macht `git pull --ff-only` im Hauptrepo, in `personal/` und in jedem Workspace unter `workspaces/`, und erzeugt danach lokal `_perspektive.md`, `_workspaces.md`, `_katalog/` und alle `_kinder.md`.
- **Neue Inhalte von Kollegen** kommen an, sobald ihr Pull Request gemerged ist und du das nächste Mal synchronisierst.
- **Eigene Änderungen** gehen nie automatisch raus: geteilte über den Ablauf `public.brain.einreichen` (Review in der Harness, dann Pull Request), persönliche direkt in dein privates `brain-personal`.
- **Neuer Workspace freigegeben?** `brain sync` holt nur, was schon geklont ist; neue Workspaces mit `gh search repos --owner <org> --topic brain-cell` finden und `brain clone-cell <url>`.
- **Offline:** Du arbeitest mit dem letzten Stand; `brain sync` warnt nur und holt beim nächsten Mal nach.
- **Konflikt beim Pull** (lokal etwas geändert, was auch auf GitHub geändert wurde): `brain sync` überschreibt nichts; die Harness zeigt die betroffene Datei und löst es mit dir.
