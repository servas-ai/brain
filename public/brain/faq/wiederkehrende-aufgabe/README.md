---
id: public.brain.faq.wiederkehrende-aufgabe
owner: framework
scope: public
status: accepted
summary: Wie man eine wiederkehrende Aufgabe festhält (z. B. jeden 14. Rechnungen herunterladen): Ablauf mit rhythmus und zustaendig anlegen, die Harness erinnert beim Sitzungsstart.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [wiederkehrend, regelmäßig, jeden Monat, Erinnerung, rhythmus, Termin, cron]
---

# Wie sage ich, dass ich jeden 14. eines Monats etwas erledigen muss?

Beispiel: „Jeden 14. alle Rechnungen bei Microsoft herunterladen.“

1. Die Harness legt einen **Ablauf** an (Vorlage `templates/ablauf.md`) mit:
   - `rhythmus: monatlich am 14.` (auch: `wöchentlich montags`, `quartalsweise am 5. Arbeitstag`, `jährlich am 31.01.`)
   - `zustaendig: <github-account>`
   - `ausloeser:` Sätze, mit denen man die Aufgabe anstößt („Microsoft-Rechnungen holen“)
   - Schritte mit konkreten Befehlen bzw. Klicks und wo das Ergebnis hin soll.
2. **Wohin?** Nur für dich → `personal/ablaeufe/`. Für die Firma (z. B. Buchhaltung, alle dürfen es wissen) → `public/ablaeufe/`. Für einen Kunden → in dessen Workspace.
3. **Erinnerung:** Beim Sitzungsstart sucht die Harness alle Abläufe mit `rhythmus` und `zustaendig` = dein Account und sagt dir, was heute oder in den nächsten Tagen fällig ist. Es läuft kein Server; erinnert wird, wenn du mit deiner Harness arbeitest.
4. **Soll es wirklich automatisch laufen** (ohne dass jemand die Harness öffnet), braucht es zusätzlich eine Aufgabe im Betriebssystem (Windows-Aufgabenplanung, cron) oder eine GitHub Action – der Ablauf im Brain beschreibt dann, was sie tut und was bei Fehlern zu tun ist.
