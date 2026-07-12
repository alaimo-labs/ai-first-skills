#!/usr/bin/env python3
"""Structural validator for the ai-first-skills marketplace.

Checks:
- marketplace.json: required fields, every listed plugin dir exists
- each plugin.json: required fields, version matches marketplace version
- skills: SKILL.md exists, frontmatter has name + description, name matches directory
- knowledge skills (model-invoked): description has "Use when…" trigger phrases, no $ARGUMENTS
- workflow skills (disable-model-invocation: true): frontmatter has argument-hint, body contains $ARGUMENTS
- no legacy commands/ directory (commands were migrated to workflow skills)
- the exposure-plans skill is byte-identical in afpm and afpb (sync rule)
- plugin README exists

Exit code 0 = all good, 1 = errors found.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
errors: list[str] = []
warnings: list[str] = []


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"')
    return fm


def check_marketplace() -> dict:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    if not path.exists():
        errors.append("missing .claude-plugin/marketplace.json")
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    for field in ("name", "version", "description", "owner", "plugins"):
        if field not in data:
            errors.append(f"marketplace.json: missing field '{field}'")
    return data


def check_plugin(plugin_dir: Path, marketplace_version: str) -> None:
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        errors.append(f"{plugin_dir.name}: missing .claude-plugin/plugin.json")
        return
    data = json.loads(manifest.read_text(encoding="utf-8"))
    for field in ("name", "version", "description"):
        if field not in data:
            errors.append(f"{plugin_dir.name}/plugin.json: missing field '{field}'")
    if data.get("name") != plugin_dir.name:
        errors.append(f"{plugin_dir.name}/plugin.json: name '{data.get('name')}' != directory name")
    if data.get("version") != marketplace_version:
        errors.append(
            f"{plugin_dir.name}/plugin.json: version {data.get('version')} != marketplace {marketplace_version}"
        )
    if not (plugin_dir / "README.md").exists():
        errors.append(f"{plugin_dir.name}: missing README.md")

    skills_dir = plugin_dir / "skills"
    if skills_dir.is_dir():
        for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
                continue
            fm = frontmatter(skill_md)
            if not fm.get("name"):
                errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter missing 'name'")
            elif fm["name"] != skill_dir.name:
                errors.append(
                    f"{skill_md.relative_to(ROOT)}: name '{fm['name']}' != directory '{skill_dir.name}'"
                )
            if not fm.get("description"):
                errors.append(f"{skill_md.relative_to(ROOT)}: frontmatter missing 'description'")

            body = skill_md.read_text(encoding="utf-8")
            if fm.get("disable-model-invocation") == "true":
                # workflow skill (user-invoked, verb)
                if not fm.get("argument-hint"):
                    errors.append(f"{skill_md.relative_to(ROOT)}: workflow skill missing 'argument-hint'")
                if "$ARGUMENTS" not in body:
                    warnings.append(f"{skill_md.relative_to(ROOT)}: workflow skill body does not use $ARGUMENTS")
            else:
                # knowledge skill (model-invoked, noun)
                if fm.get("description") and "use when" not in fm["description"].lower():
                    warnings.append(
                        f"{skill_md.relative_to(ROOT)}: description has no 'Use when…' trigger phrases"
                    )
                if "$ARGUMENTS" in body:
                    errors.append(
                        f"{skill_md.relative_to(ROOT)}: knowledge skill uses $ARGUMENTS "
                        "(add 'disable-model-invocation: true' if this is a workflow skill)"
                    )

    if (plugin_dir / "commands").is_dir():
        errors.append(
            f"{plugin_dir.name}: legacy commands/ directory found — commands were migrated to "
            "workflow skills (skills/{name}/SKILL.md with 'disable-model-invocation: true')"
        )


def check_exposure_plans_sync() -> None:
    a = ROOT / "afpm" / "skills" / "exposure-plans" / "SKILL.md"
    b = ROOT / "afpb" / "skills" / "exposure-plans" / "SKILL.md"
    if a.exists() and b.exists() and a.read_bytes() != b.read_bytes():
        errors.append("exposure-plans SKILL.md differs between afpm and afpb (sync rule in CLAUDE.md)")


def main() -> int:
    marketplace = check_marketplace()
    version = marketplace.get("version", "")
    for entry in marketplace.get("plugins", []):
        plugin_dir = ROOT / entry.get("source", "").lstrip("./")
        if not plugin_dir.is_dir():
            errors.append(f"marketplace.json: plugin source '{entry.get('source')}' not found")
            continue
        check_plugin(plugin_dir, version)
    check_exposure_plans_sync()

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
