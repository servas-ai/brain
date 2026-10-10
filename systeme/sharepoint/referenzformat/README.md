---
id: systeme.sharepoint.referenzformat
owner: framework
scope: public
status: accepted
summary: Wie das Brain auf SharePoint-Ordner und -Dokumente verweist: Graph-Referenz aus Site-, Drive- und Item-ID, nie Dateiname oder URL.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [Referenzformat]
---

# Referenzformat für SharePoint

```
site=<site-id> drive=<drive-id> item=<item-id>
```

- Ermitteln: `sharepointcli resolve "<sharepoint-link>"`.
- Nie Dateinamen oder URLs ins Brain schreiben: Namen verraten Inhalte, URLs brechen beim Umbenennen.
- Die Item-ID bleibt beim Umbenennen und Verschieben innerhalb einer Bibliothek gleich; beim Verschieben in eine andere Bibliothek oder Site ändert sie sich. Dann neu auflösen und den Knoten aktualisieren.
- Sammlungen verweisen auf Ordner, nicht auf Einzeldokumente. Einzeldokumente nur, wo ein Ablauf es verlangt (z. B. Audit), dann mit Version oder Stichtag.
