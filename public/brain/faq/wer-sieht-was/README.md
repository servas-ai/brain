---
id: public.brain.faq.wer-sieht-was
owner: framework
scope: public
status: accepted
summary: Wer sieht was im Brain: Hauptrepo alle Mitglieder, Workspaces nur ihr Team, personal nur der Inhaber; Archiv und Qdrant nach eigenem Login.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [Rechte, sichtbar, Zugriff, wer sieht, Datenschutz]
---

# Wer sieht was?

| Bereich | Wer sieht es | Wie ändert man das |
| --- | --- | --- |
| Hauptrepo (`systeme/`, `tools/`, `public/`) | alle Mitglieder der GitHub-Organisation mit Zugriff auf `<org>/brain` | Mitgliedschaft in der Organisation |
| `workspaces/<slug>/` | nur das GitHub-Team des Workspace-Repos | Team des Repos ändern |
| `personal/` | nur du (privates Repo in deinem Account) | gar nicht – bleibt privat |
| SharePoint-Dokumente | wer sie mit seinem Microsoft-Login öffnen darf | Rechte in SharePoint |
| Qdrant-Collections | wer sie mit seinem Token sieht | Token bei der Qdrant-Verwaltung |

Die Harness zeigt vor jedem Einreichen, wer eine neue Information sehen wird (`public.brain.einreichen`).
