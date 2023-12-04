import glob
import re


def modify_date_in_files(path):
    for filename in glob.glob(path + "/*.md"):
        print(filename)
        with open(filename, encoding="utf-8") as file:
            content = file.read()

        # Modification du format de la date
        modified_content = re.sub(
            r'date: "(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"', r"date: \1", content
        )

        # Sauvegarde des modifications
        with open(filename, "w", encoding="utf-8") as file:
            file.write(modified_content)


# Utilisation de la fonction
modify_date_in_files("content/articles")
