---
id: systeme.qdrant
owner: framework
scope: public
status: accepted
summary: Qdrant-Instanz der Firma: URL, wie Mitarbeiter ihren persönlichen Token bekommen, Embedding-Einstellung und offene Collections.
evidence: [brain v0.1]
review_by: 2027-10-10
keys: [Qdrant]
---

# Qdrant

**Beim Setup von der Harness mit dem Menschen auszufüllen.**

| | |
| --- | --- |
| URL | `<https://qdrant.firma.example:6333>` |
| Persönlicher Token | `<wie und bei wem man ihn bekommt – nie per Chat>` |
| Embedding für Textsuche | `<Modell und Endpunkt, mit dem die Collections gefüllt wurden>` |
| Zuständig | `<rolle>` |

## Collections, von denen alle wissen dürfen

| Collection | Inhalt | Payload-Felder |
| --- | --- | --- |
| `<name>` | `<quelle>` | `<felder aus qdrantcli info>` |

Welche Collections ein Token sieht, entscheidet der Token. Collections, deren Existenz vertraulich ist, stehen im zuständigen Workspace.

Kinder: `_kinder.md`
