#!/usr/bin/env python3
"""Create a publication folder without inventing scientific metadata."""
import argparse
import csv
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS = ROOT / "publications"
TEMPLATE = PUBLICATIONS / "_template"
REGISTER = PUBLICATIONS / "publication-register.csv"

def main():
    parser = argparse.ArgumentParser(description="Create a publication workspace.")
    parser.add_argument("publication_id", help="PUB-001, PUB-002, ...")
    args = parser.parse_args()
    publication_id = args.publication_id.upper()

    if not re.fullmatch(r"PUB-[0-9]{3,}", publication_id):
        parser.error("Gunakan format PUB-001, PUB-002, ...")
    dest = PUBLICATIONS / publication_id
    if dest.exists() and any(dest.iterdir()):
        parser.error(f"Folder berisi file sudah ada: {dest}")
    if not TEMPLATE.is_dir() or not REGISTER.is_file():
        parser.error("Publication template atau register tidak ditemukan")

    with REGISTER.open(newline="", encoding="utf-8") as handle:
        records = list(csv.DictReader(handle))
    if publication_id in {row.get("publication_id") for row in records}:
        parser.error(f"Publication ID sudah tercatat: {publication_id}")

    if dest.exists():
        dest.rmdir()  # placeholder .gitkeep harus dipindah terlebih dahulu
    shutil.copytree(TEMPLATE, dest)
    manifest = dest / "publication.yml"
    manifest.write_text(
        manifest.read_text(encoding="utf-8").replace('id: ""', f'id: "{publication_id}"', 1),
        encoding="utf-8",
    )
    header = REGISTER.read_text(encoding="utf-8").splitlines()[0].split(",")
    row = {key: "" for key in header}
    row["publication_id"] = publication_id
    row["status"] = "draft"
    with REGISTER.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=header)
        writer.writerow(row)
    print(f"Created {dest.relative_to(ROOT)} and updated publication register.")

if __name__ == "__main__":
    main()

