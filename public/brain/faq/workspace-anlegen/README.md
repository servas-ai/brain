---
id: public.brain.faq.workspace-anlegen
owner: framework
scope: public
status: accepted
summary: Wie man einen neuen Workspace für einen Kunden, ein Projekt oder einen Auftrag anlegt und Leute hinzufügt.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [Workspace, neuer Kunde, neues Projekt, Zelle, anlegen]
---

# Wie lege ich einen neuen Workspace an?

Braucht Admin-Rechte in der GitHub-Organisation (oder ein Admin macht es).

```bash
gh repo create <org>/ws-<slug> --private --description "<ein Satz>"
gh repo edit <org>/ws-<slug> --add-topic brain-cell
gh api -X PUT orgs/<org>/teams/<team>/repos/<org>/ws-<slug> -f permission=push
```

Dann im neuen Repo `.cell.yml` (Vorlage `templates/cell.yml`) und `README.md` (Vorlage `templates/workspace-README.md`) anlegen und pushen. Jeder im Team holt ihn mit `brain clone-cell https://github.com/<org>/ws-<slug>`.
