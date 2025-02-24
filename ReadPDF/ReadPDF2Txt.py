import pypdf
import os

# Chemin du fichier PDF
pdf_path = r"C:\TestPy\exemple.pdf"

# Déterminer le répertoire du PDF pour enregistrer le fichier texte au même endroit
pdf_directory = os.path.dirname(pdf_path)
output_path = os.path.join(pdf_directory, "exemple.txt")

# Création du lecteur PDF
reader = pypdf.PdfReader(pdf_path)

# Extraction et sauvegarde du texte
text_lines = []  # Liste pour stocker les lignes de texte

with open(output_path, "w", encoding="utf-8") as file:
    for page in reader.pages:
        text = page.extract_text()
        if text:  # Vérifier si du texte a été extrait
            lines = text.split("\n")  # Découper en lignes
            text_lines.extend(lines)  # Ajouter les lignes à la liste
            file.write(text + "\n")  # Écrire dans le fichier

# Affichage des résultats
print(f"Fichier enregistré ici : {output_path}")
print(f"Nombre de pages extraites : {len(reader.pages)}")
print(f"Nombre de lignes enregistrées : {len(text_lines)}")
