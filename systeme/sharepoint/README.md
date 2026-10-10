---
id: systeme.sharepoint
owner: framework
scope: public
status: accepted
summary: SharePoint-Tenant der Firma: Tenant-ID, Client-ID für sharepointcli, wichtige Sites und das Referenzformat.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [SharePoint]
---

# SharePoint

**Beim Setup von der Harness mit dem Menschen auszufüllen.**

| | |
| --- | --- |
| Tenant | `<tenant-id oder firma.onmicrosoft.com>` |
| Client-ID für `sharepointcli` | `<app-id der Entra-App-Registrierung>` |
| Zuständig (IT) | `<rolle>` |

## Wichtige Sites

| Site | Wofür | Site-ID |
| --- | --- | --- |
| `<name>` | `<zweck>` | `<id aus sharepointcli sites>` |

Wer welche Site öffnen darf, entscheidet SharePoint mit dem Login. Vertrauliche Sites, deren Existenz nicht alle kennen sollen, stehen nicht hier, sondern im zuständigen Workspace.

Kinder: `_kinder.md`
