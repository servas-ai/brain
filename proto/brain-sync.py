#!/usr/bin/env python3
"""Phase-0-Prototyp von `brain sync` (nur lokale Erzeugung, kein Git, kein Netz).

Erzeugt im Brain-Root: _kinder.md je Knoten, _workspaces.md, _katalog/, _perspektive.md.
Aufruf: brain-sync.py <brain-root> [--perspektive <yaml>] [--no-katalog]
"""
import argparse
import os
import re
import sys
from collections import defaultdict

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
SKIP_DIRS = {".git", ".claude", ".codex", "templates", "proto", "_katalog"}


def frontmatter(path):
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return {}
    m = FM.match(text)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        k, v = line.split(":", 1)
        v = v.split(" #", 1)[0].strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        data[k.strip()] = v
    if "titel" not in data:
        t = re.search(r"^# (.+)$", text, re.M)
        data["titel"] = t.group(1).strip() if t else ""
    return data


def simple_yaml(path):
    data = {}
    for line in open(path, encoding="utf-8"):
        line = line.split("#", 1)[0].rstrip()
        if not line or ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        data[k.strip()] = v
    return data


def is_node(d):
    return os.path.isfile(os.path.join(d, "README.md"))


def child_nodes(d):
    out = []
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        if name in SKIP_DIRS or name.startswith("_") or name.startswith("."):
            continue
        if os.path.isdir(p) and is_node(p):
            out.append(p)
    return out


def write_kinder(root):
    count = 0
    for dirpath, dirnames, _ in os.walk(root):
        dirnames[:] = [x for x in dirnames if x not in SKIP_DIRS and not x.startswith(".") and not x.startswith("_")]
        if not is_node(dirpath):
            continue
        kids = child_nodes(dirpath)
        if not kids:
            continue
        rows = []
        for k in kids:
            fm = frontmatter(os.path.join(k, "README.md"))
            name = os.path.basename(k)
            summary = fm.get("summary") or "(kein summary)"
            mark = ""
            if fm.get("status") == "superseded":
                mark = f" **ÜBERHOLT** → `{fm.get('superseded_by', '?')}`."
            n_kids = len(child_nodes(k))
            more = f" ({n_kids} Kinder)" if n_kids else ""
            rows.append(f"| [{name}]({name}/README.md){more} | {summary}{mark} |")
        rel = os.path.relpath(dirpath, root)
        with open(os.path.join(dirpath, "_kinder.md"), "w", encoding="utf-8") as f:
            f.write(f"# Kinder von `{rel}`\n\nLokal erzeugt, nicht ändern.\n\n| Knoten | Worum es geht |\n| --- | --- |\n")
            f.write("\n".join(rows) + "\n")
        count += 1
    return count


def write_workspaces(root):
    ws = os.path.join(root, "workspaces")
    rows = {"aktiv": [], "ruhend": [], "archiviert": []}
    if os.path.isdir(ws):
        for name in sorted(os.listdir(ws)):
            cy = os.path.join(ws, name, ".cell.yml")
            if not os.path.isfile(cy):
                continue
            c = simple_yaml(cy)
            keys = ", ".join(c.get("keys", [])) if isinstance(c.get("keys"), list) else c.get("keys", "")
            st = c.get("status", "aktiv")
            rows.setdefault(st, []).append(
                f"| [{name}](workspaces/{name}/README.md) | {c.get('titel', '')} | {c.get('art', '')} | {c.get('phase', '')} | {keys} | {c.get('satz', '')} |")
    with open(os.path.join(root, "_workspaces.md"), "w", encoding="utf-8") as f:
        f.write("# Deine Workspaces\n\nLokal erzeugt aus den Zellen, die dein GitHub-Login lesen darf. Nicht ändern.\n")
        for st in ("aktiv", "ruhend", "archiviert"):
            if not rows.get(st):
                continue
            f.write(f"\n## {st}\n\n| Workspace | Titel | Art | Phase | Schlüssel | Worum es geht |\n| --- | --- | --- | --- | --- | --- |\n")
            f.write("\n".join(rows[st]) + "\n")


def key_kind(k):
    if re.fullmatch(r"\d{2}-\d{3}", k):
        return "projektnummern"
    if re.match(r"(DIN|VDI|VDE|EN|ISO|DVGW|TRGS|GEG|AMEV|ArbStättV|MLAR|MLüAR|HOAI)\b", k, re.I):
        return "normen-und-regelwerke"
    return "begriffe-und-kuerzel"


def write_katalog(root):
    entries = defaultdict(list)
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [x for x in dirnames if x not in SKIP_DIRS and not x.startswith(".") and not x.startswith("_")]
        rel = os.path.relpath(dirpath, root)
        if "README.md" in files:
            fm = frontmatter(os.path.join(dirpath, "README.md"))
            keys = fm.get("keys") or []
            if isinstance(keys, str):
                keys = [keys]
            for k in keys:
                entries[key_kind(k)].append((k, rel + "/README.md", fm.get("summary", ""), fm.get("status", "")))
        if ".cell.yml" in files:
            c = simple_yaml(os.path.join(dirpath, ".cell.yml"))
            for k in c.get("keys", []) if isinstance(c.get("keys"), list) else []:
                entries[key_kind(k)].append((k, rel + "/README.md", c.get("satz", ""), c.get("status", "")))
    kd = os.path.join(root, "_katalog")
    os.makedirs(kd, exist_ok=True)
    for old in os.listdir(kd):
        os.remove(os.path.join(kd, old))
    for kind, items in list(entries.items()):
        if len(items) > 150:
            del entries[kind]
            for it in items:
                ch = it[0][:1].lower()
                entries[f"{kind}-{ch if ch.isalpha() else '0-9'}"].append(it)
    with open(os.path.join(kd, "README.md"), "w", encoding="utf-8") as f:
        f.write("# Katalog\n\nLokal erzeugt aus den `keys` aller Knoten, die du sehen darfst. Nicht ändern. "
                "Wähle die Datei nach der Art deines Schlüssels:\n\n")
        for kind in sorted(entries):
            f.write(f"- [{kind}]({kind}.md): {len(entries[kind])} Einträge\n")
    for kind, items in list(entries.items()):
        if len(items) > 150:
            del entries[kind]
            for it in items:
                ch = it[0][:1].lower()
                grp = ch if ch.isalpha() else "0-9"
                entries[f"{kind}-{grp}"].append(it)
    for kind, items in entries.items():
        with open(os.path.join(kd, f"{kind}.md"), "w", encoding="utf-8") as f:
            f.write(f"# Katalog: {kind}\n\n| Schlüssel | Knoten | Worum es geht |\n| --- | --- | --- |\n")
            for k, path, summ, st in sorted(items, key=lambda x: x[0].lower()):
                mark = " **ÜBERHOLT**" if st == "superseded" else ""
                f.write(f"| {k} | [{path}]({'../' + path}) | {summ}{mark} |\n")


def write_perspektive(root, src):
    with open(os.path.join(root, "_perspektive.md"), "w", encoding="utf-8") as f:
        f.write("# Deine Perspektive\n\nLokal erzeugt aus deinen Logins. Nicht ändern. "
                "Was hier fehlt, sieht dein Mensch nicht; versuch es nicht.\n\n")
        if src and os.path.isfile(src):
            f.write(open(src, encoding="utf-8").read())
        else:
            f.write("(keine Angaben zu Logins)\n")
        ws = os.path.join(root, "workspaces")
        names = sorted(n for n in os.listdir(ws) if os.path.isfile(os.path.join(ws, n, ".cell.yml"))) if os.path.isdir(ws) else []
        f.write(f"\n## GitHub-Zellen\n\n- personal/: {'vorhanden' if os.path.isdir(os.path.join(root, 'personal')) else 'fehlt'}\n"
                f"- Workspaces ({len(names)}): siehe `_workspaces.md`\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--perspektive")
    ap.add_argument("--no-katalog", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    n = write_kinder(root)
    write_workspaces(root)
    if a.no_katalog:
        kd = os.path.join(root, "_katalog")
        if os.path.isdir(kd):
            for old in os.listdir(kd):
                os.remove(os.path.join(kd, old))
            os.rmdir(kd)
    else:
        write_katalog(root)
    write_perspektive(root, a.perspektive)
    print(f"brain-sync: {n} _kinder.md, _workspaces.md, {'kein ' if a.no_katalog else ''}_katalog, _perspektive.md")


if __name__ == "__main__":
    sys.exit(main())
