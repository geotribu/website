#!/bin/bash

set -e

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <date>"
  echo "Example: $0 2022-01-07" >&2
  exit 1
fi

# FUNCTIONS ----------------------------
fn_datecheck() {
    local format="$1" d="$2"
    [[ "$(date "+$format" -d "$d" 2>/dev/null)" == "$d" ]]
}

# GLOBALS ------------------------------
RDP_DATE=$1
RDP_FOLDER_PATH="content/rdp"
RDP_TEMPLATE_PATH="content/rdp/templates/template_rdp.md"

# MAIN ---------------------------------

# check if passed date is valid
if [[ "$RDP_DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo -e "\e[32mFormat de date valide - check 1/2."
else
    echo -e "\e[31mLa date doit être du type : 'AAAA-MM-JJ' (exemple : 2022-01-07)"
    exit 1
fi

if fn_datecheck "%F" "$RDP_DATE"; then
    echo -e "\e[32mFormat de date valide - check 2/2."
else
    echo -e "\e[31mDate ou format de date invalide. La date doit être du type : 'AAAA-MM-JJ' (exemple : 2022-01-07)"
    exit 1
fi

date_formatted=$(date -d "${RDP_DATE}" '+%F')

# check if date is in the future
if [[ "$date_formatted" > "$(date '+%F')" ]]; then
    echo -e "\e[32mLa date est bien dans le futur."
else
    echo -e "\e[31mLa date de la prochaine revue de presse doit être dans le futur."
    exit 1
fi

# check if date is a friday
if [[ "$(date -d "${date_formatted}" '+%u')" == "5" ]]; then
    echo -e "\e[32mLa date est bien un vendredi."
else
    echo -e "\e[31mLa date doit être un vendredi."
    exit 1
fi

echo "Date de la prochaine revue de presse : $date_formatted"

# check if RDP branch already exists on remote
existed_in_remote=$(git ls-remote --heads origin rdp/"$date_formatted")

if [[ -z ${existed_in_remote} ]]; then
    echo -e "\e[32mLa branche de la prochaine RDP n'existe pas encore et sera créée."
else
    echo -e "\e[31mLa branche existe déjà sur le dépôt principal (GitHub).\e[33m\nPour ne pas risquer d'écraser, on bascule sur la branche distante existante et on s'arrête là."
    git checkout --progress --track origin/rdp/"$date_formatted"
    exit 1
fi

# determine final path
RDP_PATH="$RDP_FOLDER_PATH/$(date -d "${date_formatted}" '+%Y')/rdp_$date_formatted.md"
echo -e "\e[34mLe fichier de la prochaine revue de presse sera $RDP_PATH"

# make sure parent folder exists
[ -d "$RDP_PATH" ] || mkdir -p -v "$(dirname "$RDP_PATH")"

# copy template
cp -v $RDP_TEMPLATE_PATH "$RDP_PATH"

# replace default values
sed -i "s|^title:.*|title: Revue de presse du $(date -d "${date_formatted}" '+%-d %B %Y')|" "$RDP_PATH"
sed -i "s|^date:.*|date: $(date -d "${date_formatted}" '+%Y-%m-%d') 14:20|" "$RDP_PATH"
sed -i "s|^description:.*|description: \"\"|" "$RDP_PATH"
sed -i "s|^# Revue de presse du.*|# Revue de presse du $(date -d "${date_formatted}" '+%-d %B %Y')|" "$RDP_PATH"
echo -e "\e[32mValeurs par défaut remplacées."
