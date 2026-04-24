"""Custom git hook to be used with pre-commit  to automatically remove author articles
lists from Markdown files before commit."""

from __future__ import annotations

import re
import sys
from pathlib import Path

regex_pattern = re.compile(
    r"<!--\s*--8<--\s*\[start:author-articles-autolist\]\s*-->.*?"
    r"<!--\s*--8<--\s*\[end:author-articles-autolist\]\s*-->",
    re.DOTALL,
)


def process_file(path: Path) -> bool:
    """Parses the given file and removes any block matching the pattern.
    Args:
        path (Path): file about to be committed

    Returns:
        bool: True if the file has been modified, False otherwise
    """

    original: str = path.read_text(encoding="utf-8")
    cleaned: str = re.sub(regex_pattern, "", original)

    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        print(
            f"La liste autogénérée d'articles a été retirée de la page de l'auteurice {path}"
        )
        return True

    return False


def main() -> int:
    """Entry point for the git hook.

    Returns:
        0 if no changes were needed,
        1 if files were modified or errors were detected.
    """
    changed: bool = False
    for filename in sys.argv[1:]:
        path = Path(filename)

        if path.exists():
            if process_file(path):
                print(f"Stripped autolist block(s) in {filename}")
                changed = True

    return 1 if changed else 0


if __name__ == "__main__":
    sys.exit(main())
