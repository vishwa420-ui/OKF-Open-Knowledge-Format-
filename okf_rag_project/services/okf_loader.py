
from pathlib import Path
import yaml


def load_okf_bundle(folder):

    folder = Path(folder)
    documents = []

    for path in folder.rglob("*.md"):

        if path.name.lower() in ("index.md", "log.md"):
            continue

        content = path.read_text(encoding="utf-8")

        if not content.startswith("---"):
            print(f"Skipping {path}: Missing YAML")
            continue

        parts = content.split("---", 2)

        if len(parts) != 3:
            print(f"Skipping {path}: Invalid frontmatter")
            continue

        try:
            metadata = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            print(f"Skipping {path}: Invalid YAML")
            continue

        if not isinstance(metadata, dict):
            continue

        if not isinstance(metadata.get("type"), str):
            continue

        if not metadata["type"].strip():
            continue

        body = parts[2].strip()

        if not body:
            continue

        concept_id = path.relative_to(folder).with_suffix("").as_posix()

        documents.append({
            "id": concept_id,
            "metadata": metadata,
            "content": body
        })

    return documents
