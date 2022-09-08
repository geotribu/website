from pathlib import Path

start_folder: Path = Path("build/mkdocs/site/assets/externals/")
dest_folder: Path = Path("_to_upload")
dest_folder.mkdir(parents=True, exist_ok=True)
images_extension = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")

for image in start_folder.glob("**/*"):
    if image.suffix.lower() in images_extension:
        image.rename(dest_folder / image.name)
