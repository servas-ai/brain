---
id: public.brain.faq.kollegen-einbinden
owner: framework
scope: public
status: accepted
summary: Wie bekommen meine Mitarbeiter dasselbe Brain wie ich: einladen, Link zur README an ihre Harness, Rechte über Teams.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [Mitarbeiter, Kollegen, einladen, Onboarding, Team]
---

# Wie bekommen meine Mitarbeiter dasselbe Brain wie ich?

1. **In die GitHub-Organisation einladen** (Admin): `gh api -X PUT orgs/<org>/memberships/<github-account> -f role=member` oder auf github.com unter Organisation → People → Invite.
2. **Zugriff auf das Brain geben:** Alle Mitglieder brauchen Leserecht auf `<org>/brain` (z. B. Team „alle“ mit Write-Recht für Branches/PRs).
3. **Workspaces freigeben:** pro Workspace-Repo das passende Team hinzufügen. Nur wer im Team ist, sieht den Workspace – auch lokal nicht als leeren Ordner.
4. **Dem Mitarbeiter sagen:** „Gib deiner Harness den Link `https://github.com/servas-ai/brain` und sag: Richte das Brain der Firma `<org>` ein, laut README.“ Seine Harness installiert die Tools, klont `<org>/brain`, legt sein privates `brain-personal` an und holt seine Workspaces.
5. **Seine eigenen Logins** (Microsoft, Qdrant-Token) richtet er selbst ein – er sieht damit genau das, was er darf.

Danach haben alle denselben geteilten Stand; jeder hat zusätzlich seinen eigenen `personal/`-Bereich, den nur er sieht.
