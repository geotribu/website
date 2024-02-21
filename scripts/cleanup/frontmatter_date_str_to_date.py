import re
from pathlib import Path

for md_filepath in Path("content").glob("**/*.md"):
    with md_filepath.open(mode="r", encoding="UTF-8") as f:
        content = f.read()
        # Utiliser une expression régulière pour trouver le champ de date dans le frontmatter
        match = re.search(
            r"^---\s*\n.*?date: (\d{4}-\d{2}-\d{2}).*?\n---",
            content,
            re.DOTALL | re.MULTILINE,
        )

        if match:
            old_date = match.group(1)
            new_date = old_date  # Même format, pas besoin de conversion ici

            # Remplacer l'ancienne date par la nouvelle
            updated_content = re.sub(
                rf"^---\s*\n.*?date: {re.escape(old_date)}.*?\n---",
                f"---\ndate: {new_date}\n---",
                content,
                flags=re.DOTALL | re.MULTILINE,
            )

            # Écrire le contenu mis à jour dans le fichier
            with md_filepath.open(mode="w", encoding="UTF-8") as updated_file:
                updated_file.write(updated_content)
