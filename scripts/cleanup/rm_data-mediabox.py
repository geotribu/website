#! python3  # noqa: E265

"""
Script one-shot pour nettoyer la syntaxe de la lightbox pour les images
dans le cadre de https://github.com/geotribu/website/pull/720.
"""

from pathlib import Path

# -- REGEX - Solution abandonnée finalement car pas rentable
# regex_mediabox = r"^(.*data-mediabox.*$)"

# test_str = ("[![Explication des images de références, de début et de fin de séquences](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/meteo_inegalites_traitement_avec_r/montage_images_bases_11012019.jpg \"Explication des images de références, de début et de fin de séquences\"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/meteo_inegalites_traitement_avec_r/montage_images_bases_11012019.jpg){: data-mediabox=\"lightbox-gallery\" data-title=\"Explication des images de références, de début et de fin de séquences\"}\n"
# 	"![logo météo](https://cdn.geotribu.fr/img/logos-icones/divers/weather_app.png \"logo météo\"){: .img-thumbnail-left }\n"
# 	"[![logo météo](https://cdn.geotribu.fr/img/logos-icones/divers/weather_app.png \"logo météo\"){: .img-thumbnail-left }](https://cdn.geotribu.fr/img/logos-icones/divers/weather_app.png)")

# matches = re.finditer(regex, test_str, re.MULTILINE)

# for matchNum, match in enumerate(matches, start=1):

#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1

#         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


# -- SEARCH & REPLACE des familles

for md_filepath in Path("content").glob("**/*.md"):
    # on lit le fichier, on le parcourt et on vire les parties liées à la lightbox
    with md_filepath.open(mode="r") as contenu:
        output_lines = []
        counter_mediabox = 0
        for line in contenu.readlines():
            if "data-mediabox" in line:
                counter_mediabox += 1
                # print(line)
                # on enlève le premier crochet ouvrant qui servait à ouvrir la balise de lien
                new_line = line[1:]

                # crochet_fermant_2 = line.rfind("]")  # celui qui ferme le lien qui servait pour la lightbox. Méthode fragile si jamais il y a un crochet dans la description
                crochet_fermant_1 = line.find("]")  # celui du texte alternatif
                crochet_fermant_2 = line.find(
                    "]", crochet_fermant_1 + 1
                )  # celui qui ferme le lien qui servait pour la lightbox.
                partie_a_supprimer = line[crochet_fermant_2:]
                # print(partie_a_supprimer)
                new_line = new_line.replace(partie_a_supprimer, "")
                output_lines.append(new_line + "\n")

            else:
                output_lines.append(line)

    if counter_mediabox == 0:
        print(f"Pas de balise mediabox trouvée dans {md_filepath}")
        continue

    # réécriture du fichier
    # output_filepath = md_filepath.with_name(f"{md_filepath.stem}_modified.md")  # test par sécurité
    with md_filepath.open(mode="w") as fichier:
        fichier.writelines(output_lines)
    print(f"Fichier modifié ({counter_mediabox} balises retirées) : {md_filepath}")
