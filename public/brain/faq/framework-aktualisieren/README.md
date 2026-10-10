---
id: public.brain.faq.framework-aktualisieren
owner: framework
scope: public
status: accepted
summary: Wie man das Firmen-Brain auf den neuesten Stand der Vorlage (servas-ai/brain) bringt, ohne Firmeninhalte zu überschreiben.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [Update, Framework, Vorlage, Template, aktualisieren]
---

# Wie bringe ich unser Brain auf den neuesten Stand der Vorlage?

Ein aus der Vorlage erzeugtes Repo hat keine gemeinsame Git-Historie mit ihr; ein automatisches Update gibt es in Version 0.1 noch nicht. Aktualisiert werden nur die **Framework-Dateien** – Firmeninhalte bleiben unberührt.

| Framework (wird aktualisiert) | Firma (wird nie angefasst) |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md`, `README.md`, `.claude/`, `.ignore`, `.gitattributes`, `.gitignore`, `templates/`, `public/brain/`, `tools/brain/README.md`, `tools/sharepointcli/README.md`, `tools/qdrantcli/README.md` | `regeln-firma.md`, `systeme/`, `public/` (außer `public/brain/`), `tools/*/debugging/` und eigene Tools, `workspaces/`, `personal/` |

```bash
cd <brain-root>
git remote get-url template 2>/dev/null || git remote add template https://github.com/servas-ai/brain.git
git fetch template
git switch -c framework-update origin/main
git checkout template/main -- AGENTS.md CLAUDE.md README.md .claude .ignore .gitattributes .gitignore templates public/brain \
  tools/brain/README.md tools/sharepointcli/README.md tools/qdrantcli/README.md
git diff --cached --stat
```

Danach wie jede geteilte Änderung einreichen (`public.brain.einreichen`): dem Menschen die Liste der geänderten Framework-Dateien zeigen (sichtbar für alle Mitglieder), nach seinem Ja committen, pushen, Pull Request. Nach dem Merge holen alle den neuen Stand mit `brain sync`.

Die Programme (`brain`, `sharepointcli`, `qdrantcli`) aktualisiert man getrennt: `public.brain.faq.tools-aktualisieren`.
