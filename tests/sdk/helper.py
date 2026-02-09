import hashlib
from pathlib import Path


def file_hash(path: Path, chunk_size=8192) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def folders_identical(dir1: Path, dir2: Path) -> bool:
    files1 = {p.relative_to(dir1): p for p in dir1.rglob("*") if p.is_file()}
    files2 = {p.relative_to(dir2): p for p in dir2.rglob("*") if p.is_file()}

    if files1.keys() != files2.keys():
        return False

    for rel, p1 in files1.items():
        p2 = files2[rel]
        if file_hash(p1) != file_hash(p2):
            return False

    return True
