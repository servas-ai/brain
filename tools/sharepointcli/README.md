---
id: tools.sharepointcli
owner: framework
scope: public
status: accepted
summary: sharepointcli: Zugriff auf SharePoint mit dem Microsoft-Login des Menschen – Sites finden, Ordner auflisten, Dateien holen und als Text lesen.
evidence: [servas brain v0.1]
review_by: 2027-10-10
keys: [sharepointcli, SharePoint, OneDrive, Graph]
---

# sharepointcli

Eigenständiges Programm für das Datenarchiv in SharePoint. Es arbeitet mit dem **Microsoft-Login deines Menschen** (delegierte Rechte): Was er in SharePoint öffnen darf, darfst du damit lesen, sonst nichts.

## Wann verwenden

- Eine Sammlung im Brain nennt eine SharePoint-Referenz (`site=… drive=… item=…`) und du brauchst die Dokumente.
- Dein Mensch gibt dir einen SharePoint-Link.
- Du brauchst den Text eines Word-, PowerPoint- oder Excel-Dokuments.

Nicht verwenden, um Dokumente ins Brain zu kopieren. Ins Brain kommen nur Referenzen (siehe `systeme.sharepoint.referenzformat`).

## Befehle

| Befehl | Wofür |
| --- | --- |
| `sharepointcli login` | einmalig: Anmeldung im Browser (Tenant und Client-ID stehen in `systeme.sharepoint`) |
| `sharepointcli whoami` | wer ist angemeldet |
| `sharepointcli sites "<suche>"` | Sites finden |
| `sharepointcli drives <site-id>` | Bibliotheken einer Site |
| `sharepointcli ls site=<s> drive=<d> item=<i>` | Ordner auflisten |
| `sharepointcli ls --url "<sharepoint-link>"` | Ordner zu einem Link |
| `sharepointcli resolve "<sharepoint-link>"` | Referenz zu einem Link (für Sammlungen im Brain) |
| `sharepointcli text <referenz>` | Text aus .docx/.pptx/.xlsx/.txt/.md/.csv |
| `sharepointcli get <referenz> -o <datei>` | Datei herunterladen (z. B. PDF) |
| `sharepointcli search <site-id> "<begriff>"` | Suche in einer Bibliothek |

Alle Befehle können `--json`.

## Meldungen richtig lesen

- **403 / kein Zugriff:** Dein Mensch darf das nicht sehen. Kein Fehler, nicht umgehen; sag es ihm.
- **404 bei einer Referenz:** Das Dokument wurde vermutlich über Bibliotheksgrenzen verschoben (die ID ändert sich dann). Mit `--url` neu auflösen und die Sammlung im Brain aktualisieren.
- **Login abgelaufen:** `sharepointcli login` erneut.

## Installation und Quelle

Installation: `README.md` im Repo-Root, „Setup für die Harness“. Einmalige Einrichtung durch die IT des Kunden (Entra-App-Registrierung): ebenfalls dort. Quellcode: https://github.com/servas-ai/sharepointcli

Fehlerbilder: `debugging/_kinder.md`
